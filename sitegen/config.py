"""Site-wide configuration: identity, canonical definitions, navigation, metadata defaults."""

SITE_NAME = "Gaiish"
SITE_URL = "https://gaiish.com"
SITE_TAGLINE = "The Language of Human–AI Communication"
SITE_DESCRIPTION = (
    "Learn Gaiish, a structured language and methodology for communicating more effectively "
    "with generative AI. Build better prompts using intent, context, instructions, "
    "constraints, results, and validation."
)
DEFAULT_OG_IMAGE = "/assets/brand-board.jpg"

# Author / reviewer metadata. Placeholders — the site owner supplies the real values.
AUTHOR = "Gaiish"
AUTHOR_URL = SITE_URL + "/about"
SPEC_VERSION = "1.0"
LAST_UPDATED = "2026-08-29"

# The canonical definitions. Use these verbatim; never reword them in page content.
DEFINITION_SHORT = (
    "Gaiish is a language humans use to optimize communication with Generative AI models."
)
DEFINITION_LONG = (
    "Gaiish is the language of human–AI communication. It provides a structured methodology "
    "for expressing intent, context, instructions, constraints, and desired results so humans "
    "can communicate more effectively with generative AI systems."
)

# Core framework — the canonical six components, in order.
FRAMEWORK = [
    ("Intent", "What are you trying to accomplish?", "/gaiish-method#intent"),
    ("Context", "What does the AI need to know?", "/gaiish-method#context"),
    ("Instruction", "What should the AI do?", "/gaiish-method#instruction"),
    (
        "Constraints",
        "What rules, limits, tone, format, requirements or exclusions apply?",
        "/gaiish-method#constraints",
    ),
    ("Result", "What should the finished output look like?", "/gaiish-method#result"),
    (
        "Validation",
        "How should the AI verify the result satisfies the request?",
        "/gaiish-method#validation",
    ),
]

BASIC_FRAMEWORK = ["Goal", "Context", "Action", "Output"]

PRO_FRAMEWORK = [
    "Role",
    "Intent",
    "Context",
    "Knowledge",
    "Constraints",
    "Process",
    "Output",
    "Validation",
]

# Primary navigation: (label, url, [(label, url), ...])
NAV = [
    ("Learn", "/learn-gaiish", [
        ("What Is Gaiish?", "/what-is-gaiish"),
        ("Learn Gaiish", "/learn-gaiish"),
        ("The Gaiish Method", "/gaiish-method"),
        ("Gaiish BASIC", "/gaiish-basic"),
        ("Gaiish PRO", "/gaiish-pro"),
        ("Gaiish Syntax", "/gaiish-syntax"),
    ]),
    ("Language", "/gaiish-language", [
        ("Gaiish Language", "/gaiish-language"),
        ("Specification v%s" % SPEC_VERSION, "/gaiish-language/specification"),
        ("Dictionary", "/dictionary"),
        ("Changelog", "/changelog"),
    ]),
    ("Examples", "/examples", [
        ("Examples", "/examples"),
        ("Prompt Library", "/prompt-library"),
    ]),
    ("Tools", "/tools", [
        ("Prompt Builder", "/tools/prompt-builder"),
        ("Prompt Analyzer", "/tools/prompt-analyzer"),
    ]),
    ("Context", "/prompt-engineering", [
        ("Prompt Engineering", "/prompt-engineering"),
        ("Gaiish vs Prompt Engineering", "/gaiish-vs-prompt-engineering"),
        ("Generative AI", "/generative-ai"),
    ]),
    ("Use", "/gaiish-for-business", [
        ("Gaiish for Business", "/gaiish-for-business"),
        ("Gaiish for Education", "/gaiish-for-education"),
        ("Research", "/research"),
        ("About", "/about"),
        ("Origin of Gaiish", "/origin-of-gaiish"),
    ]),
]

FOOTER_LINKS = [
    ("Learn", [
        ("What Is Gaiish?", "/what-is-gaiish"),
        ("Learn Gaiish", "/learn-gaiish"),
        ("The Gaiish Method", "/gaiish-method"),
        ("Gaiish BASIC", "/gaiish-basic"),
        ("Gaiish PRO", "/gaiish-pro"),
        ("Gaiish Syntax", "/gaiish-syntax"),
    ]),
    ("Reference", [
        ("Gaiish Language", "/gaiish-language"),
        ("Specification", "/gaiish-language/specification"),
        ("Dictionary", "/dictionary"),
        ("Examples", "/examples"),
        ("Prompt Library", "/prompt-library"),
        ("Interactive Gaiish Map", "/gaiish-map"),
        ("Changelog", "/changelog"),
    ]),
    ("Tools", [
        ("Prompt Builder", "/tools/prompt-builder"),
        ("Prompt Analyzer", "/tools/prompt-analyzer"),
    ]),
    ("Background", [
        ("Prompt Engineering", "/prompt-engineering"),
        ("Gaiish vs Prompt Engineering", "/gaiish-vs-prompt-engineering"),
        ("Generative AI", "/generative-ai"),
        ("Research", "/research"),
        ("About", "/about"),
        ("Origin of Gaiish", "/origin-of-gaiish"),
    ]),
]

# Permanent redirects (written into vercel.json by the build).
#
# The existing /principles/*, /outcomes/* and /topics/* pages are NOT redirected — they are
# preserved as supporting articles and linked from the new pages that supersede them, so no
# indexed URL is broken. Only convenience aliases and legacy shortcuts live here.
REDIRECTS = [
    ("/prompt-builder", "/tools/prompt-builder"),
    ("/prompt-analyzer", "/tools/prompt-analyzer"),
    ("/specification", "/gaiish-language/specification"),
    ("/method", "/gaiish-method"),
    ("/basic", "/gaiish-basic"),
    ("/pro", "/gaiish-pro"),
    ("/learn", "/learn-gaiish"),
    ("/glossary", "/dictionary"),
]
