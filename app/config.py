from pathlib import Path
import os


BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
DEFAULT_DB_PATH = DATA_DIR / "agent_rebel.db"


def database_path() -> Path:
    configured = os.getenv("AGENT_REBEL_DB_PATH")
    if configured:
        return Path(configured)
    return DEFAULT_DB_PATH


def edits_enabled() -> bool:
    value = os.getenv("AGENT_REBEL_EDITABLE", "false").strip().lower()
    return value in {"1", "true", "yes", "on"}


def docs_enabled() -> bool:
    value = os.getenv("AGENT_REBEL_SHOW_DOCS", "false").strip().lower()
    return value in {"1", "true", "yes", "on"}


def wiki_directory() -> Path:
    configured = os.getenv("AGENT_REBEL_WIKI_DIR")
    if configured:
        return Path(configured)
    return BASE_DIR / "wiki"
