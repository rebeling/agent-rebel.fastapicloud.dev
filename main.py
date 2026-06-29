from contextlib import asynccontextmanager

from fastapi import Depends, FastAPI, Form, HTTPException, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.config import BASE_DIR, edits_enabled
from app.db import connect, init_db
from app.graph import graph_json
from app.lint import lint_all, lint_for_page, lint_results
from app.markdown import render_markdown
from app.okf import OKFError, new_page_okf, page_to_okf, parse_okf, parse_source_okf
from app.repository import (
    backlinks,
    create_source,
    get_page,
    grouped_pages,
    known_slugs,
    list_sources,
    operation_log,
    outgoing_links,
    revision_diff,
    revisions,
    save_page,
    search_pages,
)
from app.seed import seed_if_empty
from app.wikilinks import normalize_slug
from utils import get_title, get_version


templates = Jinja2Templates(directory=BASE_DIR / "app" / "templates")


@asynccontextmanager
async def lifespan(app: FastAPI):
    with connect() as conn:
        init_db(conn)
        seed_if_empty(conn)
    yield


app = FastAPI(title=get_title(), version=get_version(), lifespan=lifespan)
app.mount("/static", StaticFiles(directory=BASE_DIR / "app" / "static"), name="static")


def db():
    with connect() as conn:
        yield conn


def sidebar_context(conn) -> dict:
    return {
        "groups": grouped_pages(conn),
        "edits_enabled": edits_enabled(),
    }


def render_page_context(conn, slug: str) -> dict:
    page = get_page(conn, slug)
    if not page:
        raise HTTPException(status_code=404, detail="Page not found.")
    html = render_markdown(page["body_markdown"], known_slugs(conn))
    return {
        "page": page,
        "body_html": html,
        "outgoing_links": outgoing_links(conn, page["id"]),
        "backlinks": backlinks(conn, page["id"]),
        "lint": lint_for_page(conn, page["slug"]),
        **sidebar_context(conn),
    }


@app.get("/", response_class=HTMLResponse)
def home(request: Request, q: str = "", conn=Depends(db)):
    if q.strip():
        results = search_pages(conn, q)
        return templates.TemplateResponse(
            request,
            "search.html",
            {"q": q, "results": results, **sidebar_context(conn)},
        )
    context = render_page_context(conn, "index")
    return templates.TemplateResponse(request, "page.html", context)


@app.get("/wiki/{slug:path}", response_class=HTMLResponse)
def wiki_page(request: Request, slug: str, conn=Depends(db)):
    context = render_page_context(conn, slug)
    return templates.TemplateResponse(request, "page.html", context)


@app.get("/edit/{slug:path}", response_class=HTMLResponse)
def edit_page(request: Request, slug: str, conn=Depends(db)):
    if not edits_enabled():
        raise HTTPException(status_code=403, detail="Editing is disabled.")
    try:
        normalized = normalize_slug(slug)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    page = get_page(conn, normalized) or {
        "slug": normalized,
        "title": "",
        "page_type": "concept",
        "description": "",
        "tags": [],
        "body_markdown": "",
    }
    document = page_to_okf(page) if page["title"] else new_page_okf(normalized)
    return templates.TemplateResponse(
        request,
        "edit.html",
        {"page": page, "document": document, "errors": [], **sidebar_context(conn)},
    )


@app.post("/edit/{slug:path}")
def save_edited_page(
    request: Request,
    slug: str,
    document: str = Form(...),
    conn=Depends(db),
):
    if not edits_enabled():
        raise HTTPException(status_code=403, detail="Editing is disabled.")
    normalized = normalize_slug(slug)
    try:
        okf = parse_okf(document)
        page = save_page(
            conn,
            slug=normalized,
            title=okf.title,
            page_type=okf.page_type,
            description=okf.description,
            tags=okf.tags,
            body_markdown=okf.body_markdown,
            change_summary=f"Updated {normalized}.",
        )
    except (ValueError, OKFError) as exc:
        page = get_page(conn, normalized) or {
            "slug": normalized,
            "title": normalized,
            "page_type": "concept",
            "description": "",
            "tags": [],
            "body_markdown": "",
        }
        return templates.TemplateResponse(
            request,
            "edit.html",
            {"page": page, "document": document, "errors": [str(exc)], **sidebar_context(conn)},
            status_code=400,
        )
    except Exception as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    lint_all(conn)
    conn.commit()
    return RedirectResponse(f"/wiki/{page['slug']}", status_code=303)


@app.get("/history/{slug:path}", response_class=HTMLResponse)
def history(request: Request, slug: str, conn=Depends(db)):
    page = get_page(conn, slug)
    if not page:
        raise HTTPException(status_code=404, detail="Page not found.")
    return templates.TemplateResponse(
        request,
        "history.html",
        {"page": page, "revisions": revisions(conn, page["id"]), **sidebar_context(conn)},
    )


@app.get("/diff/{revision_number:int}/{slug:path}", response_class=HTMLResponse)
def diff(request: Request, revision_number: int, slug: str, conn=Depends(db)):
    page = get_page(conn, slug)
    if not page:
        raise HTTPException(status_code=404, detail="Page not found.")
    diff_text = revision_diff(conn, page["id"], revision_number)
    if diff_text is None:
        raise HTTPException(status_code=404, detail="Revision not found.")
    return templates.TemplateResponse(
        request,
        "diff.html",
        {"page": page, "revision_number": revision_number, "diff": diff_text, **sidebar_context(conn)},
    )


@app.get("/lint", response_class=HTMLResponse)
def lint_report(request: Request, conn=Depends(db)):
    lint_all(conn)
    conn.commit()
    return templates.TemplateResponse(
        request,
        "lint.html",
        {"results": lint_results(conn), **sidebar_context(conn)},
    )


@app.get("/log", response_class=HTMLResponse)
def log_view(request: Request, conn=Depends(db)):
    return templates.TemplateResponse(
        request,
        "log.html",
        {"entries": operation_log(conn), **sidebar_context(conn)},
    )


@app.get("/sources", response_class=HTMLResponse)
def sources_view(request: Request, conn=Depends(db)):
    source_document = "\n".join(
        [
            "---",
            "title: Source Title",
            "type: note",
            "---",
            "",
            "Raw source material.",
            "",
        ]
    )
    return templates.TemplateResponse(
        request,
        "sources.html",
        {"sources": list_sources(conn), "source_document": source_document, "errors": [], **sidebar_context(conn)},
    )


@app.post("/sources")
def ingest_source(
    request: Request,
    document: str = Form(...),
    conn=Depends(db),
):
    if not edits_enabled():
        raise HTTPException(status_code=403, detail="Editing is disabled.")
    try:
        source = parse_source_okf(document)
        slug = normalize_slug(f"{source.source_type}/{source.title}")
        create_source(
            conn,
            slug=slug,
            title=source.title,
            source_type=source.source_type,
            content=source.content,
        )
    except (ValueError, OKFError) as exc:
        return templates.TemplateResponse(
            request,
            "sources.html",
            {"sources": list_sources(conn), "source_document": document, "errors": [str(exc)], **sidebar_context(conn)},
            status_code=400,
        )
    conn.commit()
    return RedirectResponse("/sources", status_code=303)


@app.get("/graph.json")
def graph(conn=Depends(db)):
    return graph_json(conn)


@app.get("/graph", response_class=HTMLResponse)
def graph_view(request: Request, conn=Depends(db)):
    data = graph_json(conn)
    return templates.TemplateResponse(
        request,
        "graph.html",
        {"graph": data, **sidebar_context(conn)},
    )
