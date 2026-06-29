import json
import sqlite3
from typing import Any

from app.schema import PAGE_TYPES
from app.wikilinks import normalize_slug


def lint_all(conn: sqlite3.Connection) -> list[dict[str, Any]]:
    conn.execute("DELETE FROM lint_results")
    results: list[dict[str, Any]] = []
    pages = conn.execute("SELECT * FROM pages ORDER BY slug").fetchall()
    linked_targets = {
        row["target_page_id"]
        for row in conn.execute("SELECT target_page_id FROM links WHERE target_page_id IS NOT NULL")
    }
    for page in pages:
        results.extend(lint_page(page, linked_targets))
    results.extend(lint_links(conn))
    for result in results:
        conn.execute(
            """
            INSERT INTO lint_results (target_type, target_slug, severity, code, message, metadata_json)
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (
                result["target_type"],
                result["target_slug"],
                result["severity"],
                result["code"],
                result["message"],
                json.dumps(result.get("metadata", {})),
            ),
        )
    return results


def lint_page(page: sqlite3.Row, linked_targets: set[int]) -> list[dict[str, Any]]:
    results = []
    slug = page["slug"]
    try:
        normalize_slug(slug)
    except ValueError as exc:
        results.append(error(slug, "invalid-slug", str(exc)))
    for field in ["title", "page_type", "description", "body_markdown"]:
        if not page[field].strip():
            results.append(error(slug, "missing-field", f"{field} is required."))
    if page["page_type"] not in PAGE_TYPES:
        results.append(error(slug, "invalid-type", f"{page['page_type']} is not an allowed page type."))
    try:
        tags = json.loads(page["tags_json"])
    except json.JSONDecodeError:
        results.append(error(slug, "invalid-tags", "tags must be stored as a JSON list."))
        tags = []
    if not isinstance(tags, list) or not all(isinstance(tag, str) for tag in tags):
        results.append(error(slug, "invalid-tags", "tags must be a list of strings."))
    if page["slug"] != "index" and page["id"] not in linked_targets:
        results.append(warning(slug, "orphan-page", "No other page links here yet."))
    return results


def lint_links(conn: sqlite3.Connection) -> list[dict[str, Any]]:
    rows = conn.execute(
        """
        SELECT links.*, pages.slug AS from_slug
        FROM links
        JOIN pages ON pages.id = links.from_page_id
        WHERE links.is_broken = 1
        ORDER BY pages.slug, links.target_slug
        """
    ).fetchall()
    return [
        warning(
            row["from_slug"],
            "broken-link",
            f"Broken link to [[{row['target_slug']}]].",
            {"target_slug": row["target_slug"]},
        )
        for row in rows
    ]


def lint_results(conn: sqlite3.Connection) -> list[dict[str, Any]]:
    rows = conn.execute(
        """
        SELECT * FROM lint_results
        ORDER BY CASE severity WHEN 'error' THEN 0 ELSE 1 END, target_slug, code
        """
    ).fetchall()
    return [dict(row) for row in rows]


def lint_for_page(conn: sqlite3.Connection, slug: str) -> list[dict[str, Any]]:
    rows = conn.execute(
        """
        SELECT * FROM lint_results
        WHERE target_slug = ?
        ORDER BY CASE severity WHEN 'error' THEN 0 ELSE 1 END, code
        """,
        (slug,),
    ).fetchall()
    return [dict(row) for row in rows]


def error(slug: str, code: str, message: str, metadata: dict[str, Any] | None = None) -> dict[str, Any]:
    return result(slug, "error", code, message, metadata)


def warning(slug: str, code: str, message: str, metadata: dict[str, Any] | None = None) -> dict[str, Any]:
    return result(slug, "warning", code, message, metadata)


def result(
    slug: str,
    severity: str,
    code: str,
    message: str,
    metadata: dict[str, Any] | None = None,
) -> dict[str, Any]:
    return {
        "target_type": "page",
        "target_slug": slug,
        "severity": severity,
        "code": code,
        "message": message,
        "metadata": metadata or {},
    }
