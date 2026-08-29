"""Rendering engine: turns page definitions (blocks) into complete HTML documents.

A page is a dict:

    {
        "route": "/what-is-gaiish",       # canonical path, no trailing slash
        "title": "What Is Gaiish?",       # <title> gets " — Gaiish" appended unless title_full
        "description": "...",             # meta description, unique per page
        "h1": "What Is Gaiish?",
        "lede": "...",                    # optional intro paragraph under the h1
        "breadcrumbs": [("Learn", "/learn-gaiish")],
        "blocks": [ ... ],                # body content, see BLOCK TYPES below
        "schema": [ {...} ],              # optional extra JSON-LD objects
        "scripts": ["/tools/builder.js"], # optional page scripts (defer)
        "nav_key": "/learn-gaiish",       # which top-level nav item is current
        "updated": "2026-08-29",          # optional, shown in the page meta line
    }

BLOCK TYPES (tuples, first element is the type):

    ("h2", "Heading", "optional-id")
    ("h3", "Heading")
    ("p", "Paragraph <em>may</em> contain inline HTML")
    ("lede", "Larger intro paragraph")
    ("ul", ["item", ...])
    ("ol", ["item", ...])
    ("dl", [("term", "definition"), ...])
    ("code", "literal text shown in a <pre>")
    ("callout", "Label", "Body text")
    ("framework", None)                     # Intent → … → Validation flow diagram
    ("flow", ["Human", "Gaiish", "Generative AI", "Result"])
    ("steps", [("Label", "text"), ...])     # numbered card list
    ("cards", [("Title", "text", "/url"), ...])
    ("compare", "Traditional prompt text", "Gaiish prompt text", "Why this works better …")
    ("table", ["Col", ...], [[cell, ...], ...])
    ("links", [("Label", "/url"), ...])
    ("html", "<raw markup>")
"""

import html
import json
import os

from . import config


def esc(text):
    return html.escape(text, quote=True)


# --------------------------------------------------------------------------- blocks


def _framework_diagram():
    items = "".join(
        '<li><a href="%s"><span class="fw-name">%s</span>'
        '<span class="fw-q">%s</span></a></li>' % (url, esc(name), esc(question))
        for name, question, url in config.FRAMEWORK
    )
    return (
        '<ol class="framework" aria-label="The Gaiish framework: intent, context, '
        'instruction, constraints, result, validation">%s</ol>' % items
    )


def _flow(steps):
    items = "".join('<li>%s</li>' % esc(step) for step in steps)
    return '<ol class="flow">%s</ol>' % items


def _steps(entries):
    items = "".join(
        "<li><h3>%s</h3><p>%s</p></li>" % (esc(label), body) for label, body in entries
    )
    return '<ol class="steps">%s</ol>' % items


def _cards(entries):
    items = []
    for title, body, url in entries:
        if url:
            items.append(
                '<article class="card"><h3><a href="%s">%s</a></h3><p>%s</p>'
                '<a class="more" href="%s">Read more</a></article>' % (url, esc(title), body, url)
            )
        else:
            items.append('<article class="card"><h3>%s</h3><p>%s</p></article>' % (esc(title), body))
    return '<div class="grid">%s</div>' % "".join(items)


def _compare(traditional, gaiish, why):
    out = [
        '<div class="compare">',
        '<div class="compare-side"><span class="label weak">Traditional prompt</span>',
        "<pre>%s</pre></div>" % esc(traditional),
        '<div class="compare-side"><span class="label strong">Gaiish prompt</span>',
        "<pre>%s</pre></div>" % esc(gaiish),
        "</div>",
    ]
    if why:
        out.append('<div class="compare-why"><h3>Why this works better</h3><p>%s</p></div>' % why)
    return "".join(out)


def _table(headers, rows):
    head = "".join('<th scope="col">%s</th>' % esc(h) for h in headers)
    body = "".join(
        "<tr>%s</tr>" % "".join("<td>%s</td>" % cell for cell in row) for row in rows
    )
    return (
        '<div class="table-wrap"><table><thead><tr>%s</tr></thead>'
        "<tbody>%s</tbody></table></div>" % (head, body)
    )


def _dl(entries):
    items = "".join(
        "<dt>%s</dt><dd>%s</dd>" % (esc(term), definition) for term, definition in entries
    )
    return '<dl class="defs">%s</dl>' % items


def render_block(block):
    kind = block[0]
    if kind == "h2":
        anchor = block[2] if len(block) > 2 else None
        if anchor:
            return '<h2 id="%s">%s</h2><span class="rule"></span>' % (anchor, esc(block[1]))
        return "<h2>%s</h2><span class=\"rule\"></span>" % esc(block[1])
    if kind == "h3":
        return "<h3>%s</h3>" % esc(block[1])
    if kind == "p":
        return "<p>%s</p>" % block[1]
    if kind == "lede":
        return '<p class="lede">%s</p>' % block[1]
    if kind == "ul":
        return "<ul class=\"detail\">%s</ul>" % "".join("<li>%s</li>" % i for i in block[1])
    if kind == "ol":
        return "<ol class=\"detail\">%s</ol>" % "".join("<li>%s</li>" % i for i in block[1])
    if kind == "dl":
        return _dl(block[1])
    if kind == "code":
        return "<pre>%s</pre>" % esc(block[1])
    if kind == "callout":
        return '<aside class="callout"><span class="label">%s</span><p>%s</p></aside>' % (
            esc(block[1]),
            block[2],
        )
    if kind == "framework":
        return _framework_diagram()
    if kind == "flow":
        return _flow(block[1])
    if kind == "steps":
        return _steps(block[1])
    if kind == "cards":
        return _cards(block[1])
    if kind == "compare":
        return _compare(block[1], block[2], block[3] if len(block) > 3 else None)
    if kind == "table":
        return _table(block[1], block[2])
    if kind == "links":
        return '<p class="links">%s</p>' % "".join(
            '<a href="%s">%s</a>' % (url, esc(label)) for label, url in block[1]
        )
    if kind == "html":
        return block[1]
    raise ValueError("unknown block type: %r" % (kind,))


# --------------------------------------------------------------------------- chrome


def _nav(nav_key):
    items = []
    for label, url, children in config.NAV:
        current = ' class="current"' if url == nav_key else ""
        sub = "".join(
            '<li><a href="%s">%s</a></li>' % (child_url, esc(child_label))
            for child_label, child_url in children
        )
        items.append(
            '<li class="nav-group"><a href="%s"%s>%s</a><ul class="nav-sub">%s</ul></li>'
            % (url, current, esc(label), sub)
        )
    return (
        '<nav class="sitenav" aria-label="Primary">'
        '<a class="brand" href="/">gaiish</a>'
        '<button class="nav-toggle" type="button" aria-expanded="false" '
        'aria-controls="sitenav-list">Menu</button>'
        '<ul id="sitenav-list">%s</ul>'
        "</nav>" % "".join(items)
    )


def _breadcrumbs(crumbs, title):
    if not crumbs:
        return ""
    parts = ['<a href="/">Home</a>']
    for label, url in crumbs:
        parts.append('<a href="%s">%s</a>' % (url, esc(label)))
    parts.append("<span aria-current=\"page\">%s</span>" % esc(title))
    return '<nav class="breadcrumbs" aria-label="Breadcrumb">%s</nav>' % "".join(parts)


def _breadcrumb_schema(crumbs, title, route):
    if not crumbs:
        return None
    items = [{"@type": "ListItem", "position": 1, "name": "Home", "item": config.SITE_URL + "/"}]
    position = 2
    for label, url in crumbs:
        items.append(
            {
                "@type": "ListItem",
                "position": position,
                "name": label,
                "item": config.SITE_URL + url,
            }
        )
        position += 1
    items.append(
        {
            "@type": "ListItem",
            "position": position,
            "name": title,
            "item": config.SITE_URL + route,
        }
    )
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": items}


def _footer():
    columns = "".join(
        '<div><h2>%s</h2><ul>%s</ul></div>'
        % (
            esc(heading),
            "".join('<li><a href="%s">%s</a></li>' % (url, esc(label)) for label, url in links),
        )
        for heading, links in config.FOOTER_LINKS
    )
    return (
        '<footer class="sitefooter">'
        '<div class="footer-cols">%s</div>'
        '<p class="footer-note">%s · '
        '<a href="https://github.com/kcmacneil/gaiish.com-site">Source</a> · '
        "Deployed on Vercel</p>"
        "</footer>" % (columns, esc(config.DEFINITION_SHORT))
    )


DOCUMENT = """<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>%(title)s</title>
    <meta name="description" content="%(description)s" />
    <link rel="canonical" href="%(canonical)s" />
    <meta property="og:type" content="website" />
    <meta property="og:site_name" content="Gaiish" />
    <meta property="og:title" content="%(title)s" />
    <meta property="og:description" content="%(description)s" />
    <meta property="og:url" content="%(canonical)s" />
    <meta property="og:image" content="%(image)s" />
    <meta name="twitter:card" content="summary_large_image" />
    <meta name="twitter:title" content="%(title)s" />
    <meta name="twitter:description" content="%(description)s" />
    <meta name="twitter:image" content="%(image)s" />
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link
      href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;500&family=Montserrat:wght@400;600;700&display=swap"
      rel="stylesheet"
    />
    <link rel="stylesheet" href="/styles.css" />
%(schema)s  </head>
  <body class="%(body_class)s">
%(nav)s
%(header)s
    <main id="main">
%(body)s
    </main>
%(footer)s
%(scripts)s  </body>
</html>
"""


def render_page(page):
    route = page["route"]
    title = page.get("title_full") or "%s — Gaiish" % page["title"]
    canonical = config.SITE_URL + ("/" if route == "/" else route)

    schema_objects = list(page.get("schema", []))
    crumb_schema = _breadcrumb_schema(page.get("breadcrumbs"), page["title"], route)
    if crumb_schema:
        schema_objects.append(crumb_schema)
    schema = "".join(
        '    <script type="application/ld+json">%s</script>\n'
        % json.dumps(obj, separators=(",", ":"))
        for obj in schema_objects
    )

    header_parts = []
    if page.get("breadcrumbs"):
        header_parts.append(_breadcrumbs(page["breadcrumbs"], page["title"]))
    if page.get("eyebrow"):
        header_parts.append('<p class="eyebrow">%s</p>' % esc(page["eyebrow"]))
    header_parts.append("<h1>%s</h1>" % esc(page["h1"]))
    if page.get("lede"):
        header_parts.append('<p class="page-lede">%s</p>' % page["lede"])
    if page.get("cta"):
        header_parts.append(
            '<p class="cta-row">%s</p>'
            % "".join(
                '<a class="cta%s" href="%s">%s</a>'
                % (" cta-primary" if primary else "", url, esc(label))
                for label, url, primary in page["cta"]
            )
        )
    if page.get("updated"):
        header_parts.append(
            '<p class="page-meta">Last updated %s · <a href="/about">Author</a></p>'
            % esc(page["updated"])
        )
    header = '    <header class="pagehead">%s</header>' % "".join(header_parts)

    body = "\n".join(
        "      <section class=\"prose\">%s</section>" % render_block(block)
        for block in page["blocks"]
    )

    scripts = '    <script src="/site.js" defer></script>\n'
    scripts += "".join(
        '    <script src="%s" defer></script>\n' % src for src in page.get("scripts", [])
    )

    return DOCUMENT % {
        "title": esc(title),
        "description": esc(page["description"]),
        "canonical": canonical,
        "image": config.SITE_URL + page.get("image", config.DEFAULT_OG_IMAGE),
        "schema": schema,
        "body_class": page.get("body_class", "doc"),
        "nav": _nav(page.get("nav_key")),
        "header": header,
        "body": body,
        "footer": _footer(),
        "scripts": scripts,
    }


def output_path(root, route):
    if route == "/":
        return os.path.join(root, "index.html")
    return os.path.join(root, route.strip("/") + ".html")


def write_page(root, page):
    path = output_path(root, page["route"])
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(render_page(page))
    return path
