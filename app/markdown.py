import html
import re

from app.wikilinks import WIKILINK_RE, normalize_slug


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

    def wikilink(match: re.Match[str]) -> str:
        raw_target = html.unescape(match.group(1))
        label = html.unescape(match.group(2) or match.group(1))
        try:
            slug = normalize_slug(raw_target)
        except ValueError:
            return f'<span class="broken-link">{html.escape(label)}</span>'
        class_name = "wiki-link" if slug in known_slugs else "wiki-link broken-link"
        return f'<a class="{class_name}" href="/wiki/{html.escape(slug)}">{html.escape(label)}</a>'

    escaped = WIKILINK_RE.sub(wikilink, escaped)
    escaped = re.sub(r"`([^`]+)`", r"<code>\1</code>", escaped)
    escaped = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", escaped)
    escaped = re.sub(
        r"\[([^\]]+)\]\((https?://[^)\s]+)\)",
        r'<a href="\2" rel="noreferrer">\1</a>',
        escaped,
    )
    return escaped
