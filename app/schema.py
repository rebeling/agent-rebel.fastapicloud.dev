import json


PAGE_TYPES = [
    "concept",
    "strategy",
    "pattern",
    "tool",
    "protocol",
    "capability",
    "memory",
    "failure-mode",
    "evaluation",
    "decision",
    "example",
    "guide",
    "catalog",
    "log",
    "meta",
]

REQUIRED_PAGE_FIELDS = ["slug", "title", "page_type", "description", "tags", "body_markdown"]


def seed_schema_rules(conn) -> None:
    rules = {
        "page_types": PAGE_TYPES,
        "required_page_fields": REQUIRED_PAGE_FIELDS,
        "link_syntax": "[[slug]] or [[slug|label]]",
        "storage": "sqlite",
    }
    for key, value in rules.items():
        conn.execute(
            """
            INSERT INTO schema_rules (key, value_json, updated_at)
            VALUES (?, ?, datetime('now'))
            ON CONFLICT(key) DO UPDATE SET
                value_json = excluded.value_json,
                updated_at = excluded.updated_at
            """,
            (key, json.dumps(value)),
        )
