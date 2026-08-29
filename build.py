#!/usr/bin/env python3
"""Build the Gaiish site.

Renders every page defined under sitegen/content/ into static HTML at the repository root,
and regenerates robots.txt, sitemap.xml and the redirect table in vercel.json.

    python3 build.py

The generated HTML is committed, so Vercel serves the repository as-is with no build step.
"""

import json
import os
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ROOT)

from sitegen import config, render  # noqa: E402
from sitegen.content import collect_pages  # noqa: E402

# Hand-written pages that are not generated but must appear in the sitemap.
STATIC_ROUTES = [
    "/gaiish-map",
    "/generative-ai",
    "/topics/transformers",
    "/topics/diffusion",
    "/topics/multimodal",
    "/topics/embeddings-rag",
    "/topics/fine-tuning",
    "/topics/agents",
    "/principles/clarity",
    "/principles/context",
    "/principles/intent",
    "/principles/precision",
    "/principles/result",
    "/outcomes/communicate",
    "/outcomes/collaborate",
    "/outcomes/optimize",
    "/outcomes/empower",
]

NOINDEX_ROUTES = {"/404"}


def write_sitemap(routes):
    urls = []
    for route in routes:
        loc = config.SITE_URL + ("/" if route == "/" else route)
        priority = "1.0" if route == "/" else "0.7"
        urls.append(
            "  <url><loc>%s</loc><lastmod>%s</lastmod><priority>%s</priority></url>"
            % (loc, config.LAST_UPDATED, priority)
        )
    document = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n%s\n</urlset>\n'
        % "\n".join(urls)
    )
    with open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8") as handle:
        handle.write(document)


def write_robots():
    document = (
        "User-agent: *\n"
        "Allow: /\n"
        "\n"
        "Sitemap: %s/sitemap.xml\n" % config.SITE_URL
    )
    with open(os.path.join(ROOT, "robots.txt"), "w", encoding="utf-8") as handle:
        handle.write(document)


def write_vercel_config():
    document = {
        "$schema": "https://openapi.vercel.sh/vercel.json",
        "cleanUrls": True,
        "trailingSlash": False,
        "redirects": [
            {"source": source, "destination": destination, "permanent": True}
            for source, destination in config.REDIRECTS
        ],
        "headers": [
            {
                "source": "/(.*)",
                "headers": [
                    {"key": "X-Content-Type-Options", "value": "nosniff"},
                    {"key": "Referrer-Policy", "value": "strict-origin-when-cross-origin"},
                    {"key": "X-Frame-Options", "value": "SAMEORIGIN"},
                ],
            }
        ],
    }
    with open(os.path.join(ROOT, "vercel.json"), "w", encoding="utf-8") as handle:
        json.dump(document, handle, indent=2)
        handle.write("\n")


def main():
    pages = collect_pages()
    routes = []
    seen = set()
    for page in pages:
        if page["route"] in seen:
            raise SystemExit("duplicate route: %s" % page["route"])
        seen.add(page["route"])
        render.write_page(ROOT, page)
        if page["route"] not in NOINDEX_ROUTES:
            routes.append(page["route"])
    routes.extend(STATIC_ROUTES)
    write_sitemap(routes)
    write_robots()
    write_vercel_config()
    print("built %d pages, %d sitemap entries" % (len(pages), len(routes)))


if __name__ == "__main__":
    main()
