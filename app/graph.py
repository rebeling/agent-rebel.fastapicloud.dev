import sqlite3


def graph_json(conn: sqlite3.Connection) -> dict:
    rows = conn.execute("SELECT slug, title, page_type FROM pages ORDER BY slug").fetchall()
    nodes = [
        {
            "id": row["slug"],
            "title": row["title"],
            "type": row["page_type"],
        }
        for row in rows
    ]
    edges = [
        {
            "source": row["from_slug"],
            "target": row["target_slug"],
            "broken": bool(row["is_broken"]),
        }
        for row in conn.execute(
            """
            SELECT DISTINCT source.slug AS from_slug, links.target_slug, links.is_broken
            FROM links
            JOIN pages AS source ON source.id = links.from_page_id
            ORDER BY source.slug, links.target_slug
            """
        )
    ]
    return {"nodes": nodes, "edges": edges}
