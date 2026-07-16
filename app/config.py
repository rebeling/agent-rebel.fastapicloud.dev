from contextvars import ContextVar
from pathlib import Path
import os


BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

WIKIS: dict[str, dict] = {
    "agent": {
        "title": "The Agent Wiki",
        "subtitle": "A practical map of agent concepts, types, capabilities, memory, protocols, evaluation, and failure modes.",
        "wiki_dir": BASE_DIR / "wiki",
        "db_path": DATA_DIR / "agent_rebel.db",
        "db_env": "AGENT_REBEL_DB_PATH",
        "wiki_dir_env": "AGENT_REBEL_WIKI_DIR",
        "zip_name": "the_agent_knowledge_base.zip",
    },
    "llm-proxy": {
        "title": "The LLM Proxy Wiki",
        "subtitle": "An inspectable knowledge base on LLM proxies, gateways, routing, governance, and provider trade-offs.",
        "wiki_dir": BASE_DIR / "llm-proxy-wiki" / "wiki",
        "db_path": DATA_DIR / "llm_proxy.db",
        "db_env": "LLM_PROXY_DB_PATH",
        "wiki_dir_env": "LLM_PROXY_WIKI_DIR",
        "zip_name": "the_llm_proxy_knowledge_base.zip",
    },
}

DEFAULT_WIKI_ID = "agent"

_current_wiki_id: ContextVar[str] = ContextVar(
    "current_wiki_id", default=DEFAULT_WIKI_ID
)


def set_current_wiki(wiki_id: str) -> None:
    if wiki_id not in WIKIS:
        raise KeyError(f"Unknown wiki: {wiki_id}")
    _current_wiki_id.set(wiki_id)


def current_wiki_id() -> str:
    return _current_wiki_id.get()


def current_wiki() -> dict:
    return WIKIS[current_wiki_id()]


def database_path() -> Path:
    wiki = current_wiki()
    configured = os.getenv(wiki["db_env"])
    if configured:
        return Path(configured)
    return wiki["db_path"]


def edits_enabled() -> bool:
    value = os.getenv("AGENT_REBEL_EDITABLE", "false").strip().lower()
    return value in {"1", "true", "yes", "on"}


def docs_enabled() -> bool:
    value = os.getenv("AGENT_REBEL_SHOW_DOCS", "false").strip().lower()
    return value in {"1", "true", "yes", "on"}


def wiki_directory() -> Path:
    wiki = current_wiki()
    configured = os.getenv(wiki["wiki_dir_env"])
    if configured:
        return Path(configured)
    return wiki["wiki_dir"]
