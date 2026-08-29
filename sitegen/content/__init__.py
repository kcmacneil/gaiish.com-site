"""Content modules. Each module exposes a PAGES list of page dicts (see sitegen/render.py)."""

import importlib

# Order matters only for readability; routes must be unique across modules.
MODULES = [
    "core",
    "frameworks",
    "language",
    "knowledge",
    "tools",
    "applied",
    "authority",
]


def collect_pages():
    pages = []
    for name in MODULES:
        module = importlib.import_module("sitegen.content." + name)
        pages.extend(module.PAGES)
    return pages
