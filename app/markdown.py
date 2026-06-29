import html
import re

from app.wikilinks import WIKILINK_RE, normalize_slug

BARE_URL_RE = re.compile(r'(?<!["\'=])(https?://[^\s<>\]]+)')


def render_markdown(markdown: str, known_slugs: set[str]) -> str:
    lines = markdown.splitlines()
    output: list[str] = []
    paragraph: list[str] = []
    in_list = False
    in_code = False
    code_lines: list[str] = []

    def flush_paragraph() -> None:
        if paragraph:
            output.append(f"<p>{render_inline(' '.join(paragraph), known_slugs)}</p>")
            paragraph.clear()

    def close_list() -> None:
        nonlocal in_list
        if in_list:
            output.append("</ul>")
            in_list = False

    for line in lines:
        stripped = line.strip()
        if stripped.startswith("```"):
            flush_paragraph()
            close_list()
            if in_code:
                output.append(f"<pre><code>{html.escape(chr(10).join(code_lines))}</code></pre>")
                code_lines.clear()
                in_code = False
            else:
                in_code = True
            continue
        if in_code:
            code_lines.append(line)
            continue
        if not stripped:
            flush_paragraph()
            close_list()
            continue
        if stripped.startswith("#"):
            flush_paragraph()
            close_list()
            level = min(len(stripped) - len(stripped.lstrip("#")), 4)
            text = stripped[level:].strip()
            output.append(f"<h{level}>{render_inline(text, known_slugs)}</h{level}>")
            continue
        if stripped.startswith("- "):
            flush_paragraph()
            if not in_list:
                output.append("<ul>")
                in_list = True
            output.append(f"<li>{render_inline(stripped[2:], known_slugs)}</li>")
            continue
        paragraph.append(stripped)

    flush_paragraph()
    close_list()
    if in_code:
        output.append(f"<pre><code>{html.escape(chr(10).join(code_lines))}</code></pre>")
    return "\n".join(output)


def render_inline(text: str, known_slugs: set[str]) -> str:
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
        return f'<a class="{class_name}" href="/wiki/{html.escape(slug)}">{html.escape(label)}</a>'

    escaped = re.sub(r"`([^`]+)`", lambda match: stash(f"<code>{match.group(1)}</code>"), escaped)
    escaped = WIKILINK_RE.sub(lambda match: stash(wikilink(match)), escaped)
    escaped = re.sub(
        r"\[([^\]]+)\]\((https?://[^)\s]+)\)",
        lambda match: stash(
            f'<a href="{html.escape(match.group(2))}" rel="noreferrer">{html.escape(match.group(1))}</a>'
        ),
        escaped,
    )
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
