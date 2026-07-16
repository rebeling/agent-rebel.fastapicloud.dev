import html
import re

from app.wikilinks import WIKILINK_RE, normalize_slug

BARE_URL_RE = re.compile(r'(?<!["\'=])(https?://[^\s<>\]]+)')


TABLE_SEPARATOR_RE = re.compile(r"^\|?\s*:?-{3,}:?\s*(\|\s*:?-{3,}:?\s*)*\|?$")


def split_table_row(line: str) -> list[str]:
    stripped = line.strip()
    if stripped.startswith("|"):
        stripped = stripped[1:]
    if stripped.endswith("|"):
        stripped = stripped[:-1]
    return [cell.strip() for cell in stripped.split("|")]


def table_alignments(separator: str) -> list[str]:
    alignments = []
    for cell in split_table_row(separator):
        left = cell.startswith(":")
        right = cell.endswith(":")
        if left and right:
            alignments.append("center")
        elif right:
            alignments.append("right")
        else:
            alignments.append("left")
    return alignments


def render_markdown(markdown: str, known_slugs: set[str], base_slug: str = "") -> str:
    lines = markdown.splitlines()
    output: list[str] = []
    paragraph: list[str] = []
    in_list = False
    in_code = False
    code_language = ""
    code_lines: list[str] = []

    def flush_paragraph() -> None:
        if paragraph:
            output.append(
                f"<p>{render_inline(' '.join(paragraph), known_slugs, base_slug)}</p>"
            )
            paragraph.clear()

    def close_list() -> None:
        nonlocal in_list
        if in_list:
            output.append("</ul>")
            in_list = False

    def flush_code() -> None:
        nonlocal in_code, code_language
        code_text = html.escape(chr(10).join(code_lines))
        if code_language == "mermaid":
            output.append(f'<pre class="mermaid">{code_text}</pre>')
        else:
            output.append(f"<pre><code>{code_text}</code></pre>")
        code_lines.clear()
        in_code = False
        code_language = ""

    def emit_table(rows: list[str]) -> None:
        header = split_table_row(rows[0])
        alignments = table_alignments(rows[1])
        parts = ['<div class="table-wrap"><table>', "<thead><tr>"]
        for index, cell in enumerate(header):
            align = alignments[index] if index < len(alignments) else "left"
            parts.append(
                f'<th style="text-align:{align}">{render_inline(cell, known_slugs, base_slug)}</th>'
            )
        parts.append("</tr></thead><tbody>")
        for row in rows[2:]:
            parts.append("<tr>")
            for index, cell in enumerate(split_table_row(row)):
                align = alignments[index] if index < len(alignments) else "left"
                parts.append(
                    f'<td style="text-align:{align}">{render_inline(cell, known_slugs, base_slug)}</td>'
                )
            parts.append("</tr>")
        parts.append("</tbody></table></div>")
        output.append("".join(parts))

    index = 0
    while index < len(lines):
        line = lines[index]
        stripped = line.strip()
        if stripped.startswith("```"):
            flush_paragraph()
            close_list()
            if in_code:
                flush_code()
            else:
                in_code = True
                code_language = stripped[3:].strip().lower()
            index += 1
            continue
        if in_code:
            code_lines.append(line)
            index += 1
            continue
        if (
            stripped.startswith("|")
            and index + 1 < len(lines)
            and TABLE_SEPARATOR_RE.match(lines[index + 1].strip())
        ):
            flush_paragraph()
            close_list()
            rows = [stripped, lines[index + 1].strip()]
            index += 2
            while index < len(lines) and lines[index].strip().startswith("|"):
                rows.append(lines[index].strip())
                index += 1
            emit_table(rows)
            continue
        if not stripped:
            flush_paragraph()
            close_list()
            index += 1
            continue
        if stripped.startswith("#"):
            flush_paragraph()
            close_list()
            level = min(len(stripped) - len(stripped.lstrip("#")), 4)
            text = stripped[level:].strip()
            output.append(
                f"<h{level}>{render_inline(text, known_slugs, base_slug)}</h{level}>"
            )
            index += 1
            continue
        if stripped.startswith("- "):
            flush_paragraph()
            if not in_list:
                output.append("<ul>")
                in_list = True
            output.append(
                f"<li>{render_inline(stripped[2:], known_slugs, base_slug)}</li>"
            )
            index += 1
            continue
        paragraph.append(stripped)
        index += 1

    flush_paragraph()
    close_list()
    if in_code:
        flush_code()
    return "\n".join(output)


def resolve_relative_md_link(target: str, base_slug: str) -> str | None:
    """Resolve a relative .md link (e.g. ../providers/litellm.md) against the
    slug of the page being rendered. Returns a wiki slug or None."""
    if not target.endswith(".md") or target.startswith(("http://", "https://", "/")):
        return None
    base_parts = base_slug.split("/")[:-1]
    parts = target[: -len(".md")].split("/")
    resolved: list[str] = list(base_parts)
    for part in parts:
        if part in ("", "."):
            continue
        if part == "..":
            if resolved:
                resolved.pop()
            continue
        resolved.append(part)
    return "/".join(resolved) if resolved else None


def render_inline(text: str, known_slugs: set[str], base_slug: str = "") -> str:
    escaped = html.escape(text)
    placeholders: list[tuple[str, str]] = []

    def stash(rendered: str) -> str:
        token = f"@@INLINE_{len(placeholders)}@@"
        placeholders.append((token, rendered))
        return token

    def wikilink(match: re.Match[str]) -> str:
        raw_target = html.unescape(match.group(1))
        label = html.unescape(match.group(2) or match.group(1))
        try:
            slug = normalize_slug(raw_target)
        except ValueError:
            return f'<span class="broken-link">{html.escape(label)}</span>'
        class_name = "wiki-link" if slug in known_slugs else "wiki-link broken-link"
        from app.config import current_wiki_id

        return f'<a class="{class_name}" href="/{current_wiki_id()}/wiki/{html.escape(slug)}">{html.escape(label)}</a>'

    def md_link(match: re.Match[str]) -> str:
        label = match.group(1)
        target = html.unescape(match.group(2))
        slug = resolve_relative_md_link(target, base_slug)
        if slug is None:
            return match.group(0)
        from app.config import current_wiki_id

        class_name = "wiki-link" if slug in known_slugs else "wiki-link broken-link"
        return stash(
            f'<a class="{class_name}" href="/{current_wiki_id()}/wiki/{html.escape(slug)}">{label}</a>'
        )

    escaped = re.sub(
        r"`([^`]+)`", lambda match: stash(f"<code>{match.group(1)}</code>"), escaped
    )
    escaped = WIKILINK_RE.sub(lambda match: stash(wikilink(match)), escaped)
    escaped = re.sub(
        r"\[([^\]]+)\]\((https?://[^)\s]+)\)",
        lambda match: stash(
            f'<a href="{html.escape(match.group(2))}" rel="noreferrer">{html.escape(match.group(1))}</a>'
        ),
        escaped,
    )
    escaped = re.sub(r"\[([^\]]+)\]\(([^)\s]+\.md)\)", md_link, escaped)
    escaped = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", escaped)
    escaped = BARE_URL_RE.sub(lambda match: linkify_bare_url(match.group(1)), escaped)

    for token, rendered in placeholders:
        escaped = escaped.replace(token, rendered)

    return escaped


def linkify_bare_url(url: str) -> str:
    trailing = ""
    while url and url[-1] in ".,;:!?":
        trailing = url[-1] + trailing
        url = url[:-1]
    while url.endswith(")") and url.count("(") < url.count(")"):
        trailing = ")" + trailing
        url = url[:-1]
    return f'<a href="{html.escape(url)}" rel="noreferrer">{html.escape(url)}</a>{trailing}'
