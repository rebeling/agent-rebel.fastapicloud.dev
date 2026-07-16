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
        group = sidebar_group_title(page)
        groups[group].append(page)
    sorted_groups = sorted(
        groups.items(),
        key=lambda item: (
            min(sidebar_order_value(page.get("section_order")) for page in item[1]),
            item[0].casefold(),
        ),
    )
    return {
        group: sorted(
            pages,
            key=lambda page: (
                sidebar_order_value(page.get("nav_order")),
                page["title"].casefold(),
                page["slug"],
            ),
        )
        for group, pages in sorted_groups
    }


def sidebar_group_title(page: dict[str, Any]) -> str:
    section_title = str(page.get("section_title") or "").strip()
    if section_title:
        return section_title
    section = str(page.get("section") or "").strip()
    if section:
        return section
    return page["slug"].split("/", 1)[0] if "/" in page["slug"] else page["page_type"]


def sidebar_order_value(value: Any) -> int:
    try:
        return int(value)
    except (TypeError, ValueError):
        return 999


def get_page(conn: sqlite3.Connection, slug: str) -> dict[str, Any] | None:
    normalized = normalize_slug(slug)
    from app.config import wiki_directory
    from app.okf import parse_okf

    file_path = wiki_directory() / f"{normalized}.md"
    if not file_path.exists():
        return None

    try:
        content = file_path.read_text(encoding="utf-8")
        okf = parse_okf(content)
    except Exception as e:
        print(f"Error reading {file_path} from disk: {e}")
        row = conn.execute(
            "SELECT * FROM pages WHERE slug = ?", (normalized,)
        ).fetchone()
        return row_to_page(row) if row else None

    row = conn.execute("SELECT * FROM pages WHERE slug = ?", (normalized,)).fetchone()
    if not row:
        saved = save_page(
            conn,
            slug=normalized,
            title=okf.title,
            page_type=okf.page_type,
            section=okf.section,
            section_title=okf.section_title,
            section_order=okf.section_order,
            nav_order=okf.nav_order,
            description=okf.description,
            body_markdown=okf.body_markdown,
            tags=okf.tags,
            change_summary="Imported new file from disk on request.",
            actor="system",
            write_to_disk=False,
        )
        conn.commit()
        return saved

    db_page = row_to_page(row)
    if (
        db_page["title"] != okf.title
        or db_page["page_type"] != okf.page_type
        or db_page.get("section") != okf.section
        or db_page.get("section_title") != okf.section_title
        or db_page.get("section_order") != okf.section_order
        or db_page.get("nav_order") != okf.nav_order
        or db_page["description"] != okf.description
        or db_page["body_markdown"] != okf.body_markdown
        or db_page["tags"] != okf.tags
    ):
        saved = save_page(
            conn,
            slug=normalized,
            title=okf.title,
            page_type=okf.page_type,
            section=okf.section,
            section_title=okf.section_title,
            section_order=okf.section_order,
            nav_order=okf.nav_order,
            description=okf.description,
            body_markdown=okf.body_markdown,
            tags=okf.tags,
            change_summary="Synced disk file modification on request.",
            actor="system",
            write_to_disk=False,
        )
        conn.commit()
        return saved

    return db_page


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
    section: str | None = None,
    section_title: str | None = None,
    section_order: int | None = None,
    nav_order: int | None = None,
    actor: str = "human",
    write_to_disk: bool = True,
) -> dict[str, Any]:
    normalized = normalize_slug(slug)
    tags_json = encode_tags(tags)

    if write_to_disk:
        from app.config import wiki_directory
        from app.okf import page_to_okf

        tags_list = json.loads(tags_json)
        page_dict = {
            "title": title,
            "page_type": page_type,
            "section": clean_optional_string(section),
            "section_title": clean_optional_string(section_title),
            "section_order": clean_optional_int(section_order),
            "nav_order": clean_optional_int(nav_order),
            "description": description,
            "tags": tags_list,
            "body_markdown": body_markdown,
        }
        okf_str = page_to_okf(page_dict)
        file_path = wiki_directory() / f"{normalized}.md"
        file_path.parent.mkdir(parents=True, exist_ok=True)
        file_path.write_text(okf_str, encoding="utf-8")
    existing = conn.execute(
        "SELECT * FROM pages WHERE slug = ?", (normalized,)
    ).fetchone()
    if existing:
        page_id = int(existing["id"])
        conn.execute(
            """
            UPDATE pages
            SET title = ?, page_type = ?, section = ?, section_title = ?,
                section_order = ?, nav_order = ?, description = ?, body_markdown = ?,
                tags_json = ?, updated_at = datetime('now')
            WHERE id = ?
            """,
            (
                title.strip(),
                page_type.strip(),
                clean_optional_string(section),
                clean_optional_string(section_title),
                clean_optional_int(section_order),
                clean_optional_int(nav_order),
                description.strip(),
                body_markdown,
                tags_json,
                page_id,
            ),
        )
        operation = "edit"
    else:
        cursor = conn.execute(
            """
            INSERT INTO pages (
                slug, title, page_type, section, section_title, section_order,
                nav_order, description, body_markdown, tags_json
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                normalized,
                title.strip(),
                page_type.strip(),
                clean_optional_string(section),
                clean_optional_string(section_title),
                clean_optional_int(section_order),
                clean_optional_int(nav_order),
                description.strip(),
                body_markdown,
                tags_json,
            ),
        )
        if cursor.lastrowid is None:
            raise RuntimeError("SQLite did not return an id for the inserted page.")
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


def clean_optional_string(value: str | None) -> str | None:
    if value is None:
        return None
    cleaned = str(value).strip()
    return cleaned or None


def clean_optional_int(value: int | str | None) -> int | None:
    if value is None:
        return None
    try:
        return int(value)
    except (TypeError, ValueError):
        return None


def next_revision_number(conn: sqlite3.Connection, page_id: int) -> int:
    row = conn.execute(
        "SELECT COALESCE(MAX(revision_number), 0) + 1 AS next_number FROM page_revisions WHERE page_id = ?",
        (page_id,),
    ).fetchone()
    return int(row["next_number"])


def rebuild_links(conn: sqlite3.Connection, page_id: int, body_markdown: str) -> None:
    conn.execute("DELETE FROM links WHERE from_page_id = ?", (page_id,))
    for link in extract_wikilinks(body_markdown):
        target = conn.execute(
            "SELECT id FROM pages WHERE slug = ?", (link["target_slug"],)
        ).fetchone()
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
        SELECT
            MIN(links.id) AS id,
            links.from_page_id,
            links.target_slug,
            MIN(links.target_page_id) AS target_page_id,
            MIN(links.link_text) AS link_text,
            MAX(links.is_broken) AS is_broken,
            pages.title AS target_title,
            COUNT(*) AS link_count
        FROM links
        LEFT JOIN pages ON pages.id = links.target_page_id
        WHERE links.from_page_id = ?
        GROUP BY links.from_page_id, links.target_slug, pages.title
        ORDER BY links.target_slug
        """,
        (page_id,),
    ).fetchall()
    return [dict(row) for row in rows]


def backlinks(conn: sqlite3.Connection, page_id: int) -> list[dict[str, Any]]:
    rows = conn.execute(
        """
        SELECT
            MIN(links.id) AS id,
            links.from_page_id,
            links.target_slug,
            links.target_page_id,
            MIN(links.link_text) AS link_text,
            MAX(links.is_broken) AS is_broken,
            pages.slug AS from_slug,
            pages.title AS from_title,
            COUNT(*) AS link_count
        FROM links
        JOIN pages ON pages.id = links.from_page_id
        WHERE links.target_page_id = ?
        GROUP BY links.target_page_id, pages.id, pages.slug, pages.title
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


def revision_diff(
    conn: sqlite3.Connection, page_id: int, revision_number: int
) -> str | None:
    current = conn.execute(
        "SELECT body_markdown FROM pages WHERE id = ?", (page_id,)
    ).fetchone()
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
        (
            normalized,
            title.strip(),
            source_type.strip(),
            content,
            json.dumps(metadata or {}),
        ),
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
        (
            operation,
            target_type,
            target_slug,
            actor,
            summary,
            json.dumps(metadata or {}),
        ),
    )


def operation_log(conn: sqlite3.Connection, limit: int = 100) -> list[dict[str, Any]]:
    rows = conn.execute(
        "SELECT * FROM operation_log ORDER BY id DESC LIMIT ?",
        (limit,),
    ).fetchall()
    return [dict(row) for row in rows]
