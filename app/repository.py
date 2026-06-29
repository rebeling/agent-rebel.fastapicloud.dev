import difflib
import json
import sqlite3
from collections import defaultdict
from typing import Any

from app.wikilinks import extract_wikilinks, normalize_slug


def row_to_page(row: sqlite3.Row) -> dict[str, Any]:
    page = dict(row)
    page["tags"] = json.loads(page.pop("tags_json"))
    return page


def encode_tags(tags: list[str] | str) -> str:
    if isinstance(tags, str):
        values = [part.strip() for part in tags.split(",") if part.strip()]
    else:
        values = [str(tag).strip() for tag in tags if str(tag).strip()]
    deduped = list(dict.fromkeys(values))
    return json.dumps(deduped)


def list_pages(conn: sqlite3.Connection) -> list[dict[str, Any]]:
    rows = conn.execute("SELECT * FROM pages ORDER BY slug").fetchall()
    return [row_to_page(row) for row in rows]


def grouped_pages(conn: sqlite3.Connection) -> dict[str, list[dict[str, Any]]]:
    groups: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for page in list_pages(conn):
        group = page["slug"].split("/", 1)[0] if "/" in page["slug"] else page["page_type"]
        groups[group].append(page)
    return dict(sorted(groups.items()))


def get_page(conn: sqlite3.Connection, slug: str) -> dict[str, Any] | None:
    normalized = normalize_slug(slug)
    row = conn.execute("SELECT * FROM pages WHERE slug = ?", (normalized,)).fetchone()
    return row_to_page(row) if row else None


def known_slugs(conn: sqlite3.Connection) -> set[str]:
    return {row["slug"] for row in conn.execute("SELECT slug FROM pages")}


def save_page(
    conn: sqlite3.Connection,
    *,
    slug: str,
    title: str,
    page_type: str,
    description: str,
    body_markdown: str,
    tags: list[str] | str,
    change_summary: str,
    actor: str = "human",
) -> dict[str, Any]:
    normalized = normalize_slug(slug)
    tags_json = encode_tags(tags)
    existing = conn.execute("SELECT * FROM pages WHERE slug = ?", (normalized,)).fetchone()
    if existing:
        page_id = existing["id"]
        conn.execute(
            """
            UPDATE pages
            SET title = ?, page_type = ?, description = ?, body_markdown = ?,
                tags_json = ?, updated_at = datetime('now')
            WHERE id = ?
            """,
            (title.strip(), page_type.strip(), description.strip(), body_markdown, tags_json, page_id),
        )
        operation = "edit"
    else:
        cursor = conn.execute(
            """
            INSERT INTO pages (slug, title, page_type, description, body_markdown, tags_json)
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (normalized, title.strip(), page_type.strip(), description.strip(), body_markdown, tags_json),
        )
        page_id = cursor.lastrowid
        operation = "create"

    next_revision = next_revision_number(conn, page_id)
    conn.execute(
        """
        INSERT INTO page_revisions (
            page_id, revision_number, title, page_type, description,
            body_markdown, tags_json, change_summary
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            page_id,
            next_revision,
            title.strip(),
            page_type.strip(),
            description.strip(),
            body_markdown,
            tags_json,
            change_summary.strip() or "Saved page.",
        ),
    )
    rebuild_links(conn, page_id, body_markdown)
    log_operation(
        conn,
        operation=operation,
        target_type="page",
        target_slug=normalized,
        actor=actor,
        summary=change_summary.strip() or f"{operation.title()} page.",
    )
    return get_page(conn, normalized) or {}


def next_revision_number(conn: sqlite3.Connection, page_id: int) -> int:
    row = conn.execute(
        "SELECT COALESCE(MAX(revision_number), 0) + 1 AS next_number FROM page_revisions WHERE page_id = ?",
        (page_id,),
    ).fetchone()
    return int(row["next_number"])


def rebuild_links(conn: sqlite3.Connection, page_id: int, body_markdown: str) -> None:
    conn.execute("DELETE FROM links WHERE from_page_id = ?", (page_id,))
    for link in extract_wikilinks(body_markdown):
        target = conn.execute("SELECT id FROM pages WHERE slug = ?", (link["target_slug"],)).fetchone()
        conn.execute(
            """
            INSERT INTO links (from_page_id, target_slug, target_page_id, link_text, is_broken)
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                page_id,
                link["target_slug"],
                target["id"] if target else None,
                link["link_text"],
                0 if target else 1,
            ),
        )


def rebuild_all_links(conn: sqlite3.Connection) -> None:
    pages = conn.execute("SELECT id, body_markdown FROM pages").fetchall()
    for page in pages:
        rebuild_links(conn, page["id"], page["body_markdown"])


def outgoing_links(conn: sqlite3.Connection, page_id: int) -> list[dict[str, Any]]:
    rows = conn.execute(
        """
        SELECT links.*, pages.title AS target_title
        FROM links
        LEFT JOIN pages ON pages.id = links.target_page_id
        WHERE from_page_id = ?
        ORDER BY target_slug
        """,
        (page_id,),
    ).fetchall()
    return [dict(row) for row in rows]


def backlinks(conn: sqlite3.Connection, page_id: int) -> list[dict[str, Any]]:
    rows = conn.execute(
        """
        SELECT links.*, pages.slug AS from_slug, pages.title AS from_title
        FROM links
        JOIN pages ON pages.id = links.from_page_id
        WHERE target_page_id = ?
        ORDER BY pages.slug
        """,
        (page_id,),
    ).fetchall()
    return [dict(row) for row in rows]


def revisions(conn: sqlite3.Connection, page_id: int) -> list[dict[str, Any]]:
    rows = conn.execute(
        """
        SELECT * FROM page_revisions
        WHERE page_id = ?
        ORDER BY revision_number DESC
        """,
        (page_id,),
    ).fetchall()
    return [dict(row) for row in rows]


def revision_diff(conn: sqlite3.Connection, page_id: int, revision_number: int) -> str | None:
    current = conn.execute("SELECT body_markdown FROM pages WHERE id = ?", (page_id,)).fetchone()
    revision = conn.execute(
        """
        SELECT body_markdown FROM page_revisions
        WHERE page_id = ? AND revision_number = ?
        """,
        (page_id, revision_number),
    ).fetchone()
    if not current or not revision:
        return None
    diff = difflib.unified_diff(
        revision["body_markdown"].splitlines(),
        current["body_markdown"].splitlines(),
        fromfile=f"revision-{revision_number}",
        tofile="current",
        lineterm="",
    )
    return "\n".join(diff)


def create_source(
    conn: sqlite3.Connection,
    *,
    slug: str,
    title: str,
    source_type: str,
    content: str,
    metadata: dict[str, Any] | None = None,
) -> dict[str, Any]:
    normalized = normalize_slug(slug)
    conn.execute(
        """
        INSERT INTO sources (slug, title, source_type, content, metadata_json)
        VALUES (?, ?, ?, ?, ?)
        ON CONFLICT(slug) DO UPDATE SET
            title = excluded.title,
            source_type = excluded.source_type,
            content = excluded.content,
            metadata_json = excluded.metadata_json
        """,
        (normalized, title.strip(), source_type.strip(), content, json.dumps(metadata or {})),
    )
    log_operation(
        conn,
        operation="ingest",
        target_type="source",
        target_slug=normalized,
        actor="human",
        summary=f"Stored source: {title.strip()}",
    )
    row = conn.execute("SELECT * FROM sources WHERE slug = ?", (normalized,)).fetchone()
    return dict(row)


def list_sources(conn: sqlite3.Connection) -> list[dict[str, Any]]:
    return [dict(row) for row in conn.execute("SELECT * FROM sources ORDER BY slug")]


def search_pages(conn: sqlite3.Connection, query: str) -> list[dict[str, Any]]:
    like = f"%{query.strip()}%"
    rows = conn.execute(
        """
        SELECT * FROM pages
        WHERE title LIKE ? OR description LIKE ? OR body_markdown LIKE ? OR slug LIKE ?
        ORDER BY slug
        """,
        (like, like, like, like),
    ).fetchall()
    return [row_to_page(row) for row in rows]


def log_operation(
    conn: sqlite3.Connection,
    *,
    operation: str,
    target_type: str,
    target_slug: str,
    actor: str,
    summary: str,
    metadata: dict[str, Any] | None = None,
) -> None:
    conn.execute(
        """
        INSERT INTO operation_log (operation, target_type, target_slug, actor, summary, metadata_json)
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (operation, target_type, target_slug, actor, summary, json.dumps(metadata or {})),
    )


def operation_log(conn: sqlite3.Connection, limit: int = 100) -> list[dict[str, Any]]:
    rows = conn.execute(
        "SELECT * FROM operation_log ORDER BY id DESC LIMIT ?",
        (limit,),
    ).fetchall()
    return [dict(row) for row in rows]
