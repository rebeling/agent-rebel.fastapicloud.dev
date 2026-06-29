import re


WIKILINK_RE = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|([^\]]+))?\]\]")
SLUG_RE = re.compile(r"^[a-z0-9][a-z0-9/_-]*[a-z0-9]$|^[a-z0-9]$")


def normalize_slug(value: str) -> str:
    original = value.strip()
    if not original or ".." in original or original.startswith("/"):
        raise ValueError("Slug must contain lowercase letters, numbers, dashes, underscores, or slashes.")
    slug = original.lower().replace(" ", "-")
    slug = re.sub(r"[^a-z0-9/_-]+", "-", slug)
    slug = re.sub(r"-{2,}", "-", slug).strip("/-")
    slug = re.sub(r"/{2,}", "/", slug)
    if not slug or ".." in slug or not SLUG_RE.match(slug):
        raise ValueError("Slug must contain lowercase letters, numbers, dashes, underscores, or slashes.")
    return slug


def extract_wikilinks(markdown: str) -> list[dict[str, str]]:
    links = []
    for match in WIKILINK_RE.finditer(markdown):
        raw_target = match.group(1)
        label = match.group(2) or raw_target
        try:
            target_slug = normalize_slug(raw_target)
        except ValueError:
            target_slug = raw_target.strip()
        links.append({"target_slug": target_slug, "link_text": label.strip()})
    return links
