from dataclasses import dataclass
from typing import Any

from app.schema import PAGE_TYPES


class OKFError(ValueError):
    pass


@dataclass(frozen=True)
class OKFDocument:
    title: str
    page_type: str
    description: str
    tags: list[str]
    body_markdown: str


@dataclass(frozen=True)
class OKFSource:
    title: str
    source_type: str
    content: str


def page_to_okf(page: dict[str, Any]) -> str:
    tags = page.get("tags", [])
    tag_lines = "\n".join(f"  - {tag}" for tag in tags)
    return "\n".join(
        [
            "---",
            f"title: {page.get('title', '')}",
            f"type: {page.get('page_type', '')}",
            f"description: {page.get('description', '')}",
            "tags:",
            tag_lines,
            "---",
            "",
            page.get("body_markdown", "").rstrip(),
            "",
        ]
    )


def new_page_okf(slug: str) -> str:
    title = slug.rsplit("/", 1)[-1].replace("-", " ").replace("_", " ").title()
    return "\n".join(
        [
            "---",
            f"title: {title}",
            "type: concept",
            "description: ",
            "tags:",
            "  - draft",
            "---",
            "",
            f"# {title}",
            "",
        ]
    )


def parse_okf(document: str) -> OKFDocument:
    frontmatter, body = split_okf(document)
    metadata = parse_frontmatter(frontmatter)
    required = ["title", "type", "description", "tags"]
    missing = [field for field in required if field not in metadata or metadata[field] in ("", [])]
    if missing:
        raise OKFError(f"Missing required OKF field: {', '.join(missing)}.")
    page_type = str(metadata["type"]).strip()
    if page_type not in PAGE_TYPES:
        raise OKFError(f"Unknown OKF type '{page_type}'.")
    tags = metadata["tags"]
    if not isinstance(tags, list) or not all(isinstance(tag, str) and tag.strip() for tag in tags):
        raise OKFError("OKF field 'tags' must be a list of strings.")
    return OKFDocument(
        title=str(metadata["title"]).strip(),
        page_type=page_type,
        description=str(metadata["description"]).strip(),
        tags=[tag.strip() for tag in tags],
        body_markdown=body.strip(),
    )


def parse_source_okf(document: str) -> OKFSource:
    frontmatter, body = split_okf(document)
    metadata = parse_frontmatter(frontmatter)
    required = ["title", "type"]
    missing = [field for field in required if field not in metadata or metadata[field] in ("", [])]
    if missing:
        raise OKFError(f"Missing required source OKF field: {', '.join(missing)}.")
    if not body.strip():
        raise OKFError("Source OKF body cannot be empty.")
    return OKFSource(
        title=str(metadata["title"]).strip(),
        source_type=str(metadata["type"]).strip(),
        content=body.strip(),
    )


def split_okf(document: str) -> tuple[str, str]:
    normalized = document.replace("\r\n", "\n")
    lines = normalized.split("\n")
    if not lines or lines[0].strip() != "---":
        raise OKFError("OKF document must start with a frontmatter fence: ---.")
    for index, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            return "\n".join(lines[1:index]), "\n".join(lines[index + 1 :])
    raise OKFError("OKF frontmatter must be closed with ---.")


def parse_frontmatter(frontmatter: str) -> dict[str, Any]:
    metadata: dict[str, Any] = {}
    current_list_key: str | None = None
    for raw_line in frontmatter.splitlines():
        line = raw_line.rstrip()
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if line.startswith("  - "):
            if current_list_key is None:
                raise OKFError("List item found before a list field.")
            metadata[current_list_key].append(clean_scalar(line[4:]))
            continue
        current_list_key = None
        if ":" not in line:
            raise OKFError(f"Invalid OKF frontmatter line: {line}")
        key, raw_value = line.split(":", 1)
        key = key.strip()
        value = raw_value.strip()
        if not key:
            raise OKFError("OKF frontmatter contains an empty key.")
        if value == "":
            metadata[key] = []
            current_list_key = key
        elif value.startswith("[") and value.endswith("]"):
            metadata[key] = parse_inline_list(value)
        else:
            metadata[key] = clean_scalar(value)
    return metadata


def parse_inline_list(value: str) -> list[str]:
    inner = value[1:-1].strip()
    if not inner:
        return []
    return [clean_scalar(part.strip()) for part in inner.split(",") if part.strip()]


def clean_scalar(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        return value[1:-1]
    return value
