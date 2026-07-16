import sqlite3
from pathlib import Path

from app.config import database_path
from app.schema import seed_schema_rules


def connect(path: Path | None = None) -> sqlite3.Connection:
    db_path = path or database_path()
    db_path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(db_path, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def init_db(conn: sqlite3.Connection) -> None:
    conn.executescript(
        """
        CREATE TABLE IF NOT EXISTS pages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            slug TEXT NOT NULL UNIQUE,
            title TEXT NOT NULL,
            page_type TEXT NOT NULL,
            section TEXT,
            section_title TEXT,
            section_order INTEGER,
            nav_order INTEGER,
            description TEXT NOT NULL,
            body_markdown TEXT NOT NULL,
            tags_json TEXT NOT NULL,
            created_at TEXT NOT NULL DEFAULT (datetime('now')),
            updated_at TEXT NOT NULL DEFAULT (datetime('now'))
        );

        CREATE TABLE IF NOT EXISTS page_revisions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            page_id INTEGER NOT NULL REFERENCES pages(id) ON DELETE CASCADE,
            revision_number INTEGER NOT NULL,
            title TEXT NOT NULL,
            page_type TEXT NOT NULL,
            description TEXT NOT NULL,
            body_markdown TEXT NOT NULL,
            tags_json TEXT NOT NULL,
            change_summary TEXT NOT NULL,
            created_at TEXT NOT NULL DEFAULT (datetime('now')),
            UNIQUE(page_id, revision_number)
        );

        CREATE TABLE IF NOT EXISTS links (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            from_page_id INTEGER NOT NULL REFERENCES pages(id) ON DELETE CASCADE,
            target_slug TEXT NOT NULL,
            target_page_id INTEGER REFERENCES pages(id) ON DELETE SET NULL,
            link_text TEXT NOT NULL,
            is_broken INTEGER NOT NULL DEFAULT 0
        );

        CREATE TABLE IF NOT EXISTS sources (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            slug TEXT NOT NULL UNIQUE,
            title TEXT NOT NULL,
            source_type TEXT NOT NULL,
            content TEXT NOT NULL,
            metadata_json TEXT NOT NULL DEFAULT '{}',
            created_at TEXT NOT NULL DEFAULT (datetime('now'))
        );

        CREATE TABLE IF NOT EXISTS operation_log (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            created_at TEXT NOT NULL DEFAULT (datetime('now')),
            operation TEXT NOT NULL,
            target_type TEXT NOT NULL,
            target_slug TEXT NOT NULL,
            actor TEXT NOT NULL,
            summary TEXT NOT NULL,
            metadata_json TEXT NOT NULL DEFAULT '{}'
        );

        CREATE TABLE IF NOT EXISTS lint_results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            created_at TEXT NOT NULL DEFAULT (datetime('now')),
            target_type TEXT NOT NULL,
            target_slug TEXT NOT NULL,
            severity TEXT NOT NULL,
            code TEXT NOT NULL,
            message TEXT NOT NULL,
            metadata_json TEXT NOT NULL DEFAULT '{}'
        );

        CREATE TABLE IF NOT EXISTS schema_rules (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            key TEXT NOT NULL UNIQUE,
            value_json TEXT NOT NULL,
            updated_at TEXT NOT NULL DEFAULT (datetime('now'))
        );
        """
    )
    ensure_page_nav_columns(conn)
    seed_schema_rules(conn)
    conn.commit()


def ensure_page_nav_columns(conn: sqlite3.Connection) -> None:
    existing_columns = {
        row["name"] for row in conn.execute("PRAGMA table_info(pages)").fetchall()
    }
    nav_columns = {
        "section": "TEXT",
        "section_title": "TEXT",
        "section_order": "INTEGER",
        "nav_order": "INTEGER",
    }
    for column, column_type in nav_columns.items():
        if column not in existing_columns:
            conn.execute(f"ALTER TABLE pages ADD COLUMN {column} {column_type}")
