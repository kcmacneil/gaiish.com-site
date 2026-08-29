"""Build a two-page Gaiish reference PDF from the site's own content data.

Page 1: key Gaiish concepts. Page 2: the dictionary definitions.
Content is read from sitegen/config.py and sitegen/content/knowledge.py so the PDF
cannot drift from the site or state anything the site does not state.
"""

import html
import os
import subprocess
import tempfile
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, REPO)

from sitegen import config
from sitegen.content.knowledge import TERMS

OUT_HTML = os.path.join(tempfile.gettempdir(), "gaiish-reference.html")
OUT_PDF = os.path.join(REPO, "pdfguides", "gaiish-key-concepts-and-definitions.pdf")


def esc(text):
    return html.escape(text, quote=True)


CSS = """
@page { size: A4; margin: 0; }
* { box-sizing: border-box; }
html { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
body { margin: 0; font-family: "DejaVu Sans", Arial, Helvetica, sans-serif;
       color: #0d1b2a; font-size: 7.9pt; line-height: 1.34; }
.page { width: 210mm; height: 297mm; padding: 0 13mm 9mm; overflow: hidden;
        page-break-after: always; display: flex; flex-direction: column; }
.page:last-child { page-break-after: auto; }
.masthead { background: #071a2b; color: #fff; padding: 7mm 13mm 5.5mm;
            margin: 0 -13mm 4mm; border-bottom: 2.5pt solid #22d3ee; }
.wordmark { font-family: "DejaVu Serif", Georgia, serif; font-size: 20pt; letter-spacing: .5pt; }
.tagline { color: #7dd3fc; text-transform: uppercase; letter-spacing: 1.6pt;
           font-size: 6.6pt; margin-top: 1.5mm; }
.definition { margin-top: 2.6mm; font-size: 8.8pt; line-height: 1.4; color: #eaf6ff; max-width: 150mm; }
.definition strong { color: #fff; }
h2 { font-family: "DejaVu Serif", Georgia, serif; font-size: 10.2pt; margin: 3.4mm 0 1.4mm;
     color: #071a2b; border-bottom: .6pt solid #cfe0ec; padding-bottom: 1mm; }
h2:first-of-type { margin-top: 0; }
p { margin: 0 0 2mm; }
.muted { color: #46617a; }
.grid { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 2.5mm; }
.card { border: .6pt solid #cfe0ec; border-top: 2pt solid #0e7490; padding: 2.5mm 3mm;
        background: #f7fbfd; }
.card .n { font-size: 6.2pt; color: #0e7490; letter-spacing: 1pt; }
.card .t { font-family: "DejaVu Serif", Georgia, serif; font-size: 9.6pt; margin: .6mm 0 1mm; }
.card .q { color: #33566f; font-size: 7.6pt; line-height: 1.3; }
.flow { display: flex; flex-wrap: wrap; gap: 1.5mm; align-items: center; margin: 0 0 3mm;
        font-size: 7.6pt; color: #071a2b; }
.flow span.step { background: #071a2b; color: #fff; padding: 1mm 2.4mm; border-radius: 1mm; }
.flow span.arrow { color: #0e7490; }
.two { display: grid; grid-template-columns: 1fr 1fr; gap: 4mm; align-items: start; }
.stack { border: .6pt solid #cfe0ec; padding: 2.5mm 3mm; }
.stack h3 { margin: 0 0 1mm; font-size: 9pt; font-family: "DejaVu Serif", Georgia, serif; }
h3.why { font-family: "DejaVu Serif", Georgia, serif; font-size: 8.8pt; margin: 3mm 0 1.2mm; }
.stack ol { margin: 0; padding-left: 4.5mm; }
.stack li { margin-bottom: .4mm; }
pre { font-family: "DejaVu Sans Mono", "Courier New", monospace; font-size: 6.5pt;
      line-height: 1.3; background: #f3f7fa; border: .6pt solid #cfe0ec;
      padding: 2mm 2.4mm; margin: 0; white-space: pre-wrap; }
.label { font-size: 6.2pt; letter-spacing: 1pt; text-transform: uppercase;
         color: #46617a; margin-bottom: 1mm; }
.label.strong { color: #0e7490; }
.defs { column-count: 2; column-gap: 6mm; }
.def { break-inside: avoid; margin-bottom: 2.4mm; }
.def .term { font-family: "DejaVu Serif", Georgia, serif; font-size: 8.6pt; }
.def .kind { font-size: 5.6pt; letter-spacing: .8pt; text-transform: uppercase;
             border: .5pt solid #0e7490; color: #0e7490; padding: .2mm 1mm; margin-left: 1.2mm;
             vertical-align: 1.2pt; }
.def .kind.general { border-color: #93a9bb; color: #5c7590; }
.def p { margin: .5mm 0 0; font-size: 7.5pt; line-height: 1.32; color: #24425c; }
.foot { margin-top: auto; border-top: .6pt solid #cfe0ec; padding-top: 1.6mm;
        font-size: 6.4pt; color: #5c7590; display: flex; justify-content: space-between; }
"""

TRADITIONAL = "Write a marketing plan for my company."

GAIISH_EXAMPLE = """INTENT:
Create a practical 90-day marketing strategy.

CONTEXT:
[paste product notes and existing campaign results]
Team: one marketer half-time. Audience:
private dental practices with 2-6 chairs.

INSTRUCTION:
Propose channels, messages, weekly activities
and a measurement plan.

CONSTRAINTS:
Budget is $5,000. No paid search or new
engineering. Do not claim results that are
not in the source material.

RESULT:
Executive summary, 90-day timeline, budget
table, message examples and KPIs.

VALIDATION:
Check activities against budget and staffing,
then list every assumption."""


def masthead(subtitle, definition_html):
    return (
        '<div class="masthead"><div class="wordmark">gaiish</div>'
        '<div class="tagline">%s &middot; %s</div>'
        '<div class="definition">%s</div></div>' % (esc(config.SITE_TAGLINE), esc(subtitle), definition_html)
    )


def foot(page_label):
    return (
        '<div class="foot"><span>%s &middot; Specification v%s &middot; Last updated %s</span>'
        "<span>%s</span></div>"
        % (esc(config.SITE_URL), esc(config.SPEC_VERSION), esc(config.LAST_UPDATED), esc(page_label))
    )


def page_one():
    cards = "".join(
        '<div class="card"><div class="n">%02d</div><div class="t">%s</div>'
        '<div class="q">%s</div></div>' % (i, esc(name), esc(question))
        for i, (name, question, _url) in enumerate(config.FRAMEWORK, start=1)
    )
    flow = '<span class="arrow">&rarr;</span>'.join(
        '<span class="step">%s</span>' % esc(name) for name, _q, _u in config.FRAMEWORK
    )
    basic = "".join("<li>%s</li>" % esc(part) for part in config.BASIC_FRAMEWORK)
    pro = "".join("<li>%s</li>" % esc(part) for part in config.PRO_FRAMEWORK)

    return """<section class="page">
%(masthead)s
<h2>The six components</h2>
<div class="grid">%(cards)s</div>
<h2>The Gaiish sequence</h2>
<div class="flow">%(flow)s</div>
<p class="muted">Write the components in the order that makes the request reviewable: what the work is
for, what the model cannot infer, the action, the boundaries, the artefact, and the check. Use only the
components a task needs &mdash; a short request does not require all six.</p>
<h2>Two frameworks</h2>
<div class="two">
  <div class="stack"><h3>Gaiish BASIC</h3>
    <p class="muted">For everyday requests and for learning the shape.</p>
    <ol>%(basic)s</ol></div>
  <div class="stack"><h3>Gaiish PRO</h3>
    <p class="muted">For consequential, reviewed or handed-off work.</p>
    <ol>%(pro)s</ol></div>
</div>
<h2>Traditional prompt vs Gaiish prompt</h2>
<div class="two">
  <div><div class="label">Traditional prompt</div><pre>%(traditional)s</pre>
    <p class="muted" style="margin-top:2mm">The topic is clear; the goal, audience, limits, artefact and
    definition of a usable answer are not. The model has to guess all of them.</p>
    <h3 class="why">Why the structure helps</h3>
    <p>Providing this additional structure can improve instruction adherence and reduce ambiguity: it
    communicates the purpose, the source material and its authority, the action, the boundaries the
    answer must satisfy, the shape of the artefact, and how the result should be checked. It does not
    guarantee a better answer, and it does not make a generated claim true &mdash; people remain
    responsible for verifying facts, calculations, sources and any consequential action.</p>
    <p class="muted">Gaiish is model-independent and still developing. Write once, then communicate
    across generative AI models &mdash; but test the model you actually use, because context limits and
    instruction-following behaviour differ between models.</p></div>
  <div><div class="label strong">Gaiish prompt</div><pre>%(gaiish)s</pre></div>
</div>
%(foot)s
</section>""" % {
        "masthead": masthead(
            "Key concepts",
            "<strong>%s</strong> %s"
            % (esc(config.DEFINITION_SHORT), esc(config.DEFINITION_LONG)),
        ),
        "cards": cards,
        "flow": flow,
        "basic": basic,
        "pro": pro,
        "traditional": esc(TRADITIONAL),
        "gaiish": esc(GAIISH_EXAMPLE),
        "foot": foot("Page 1 of 2 \u00b7 Key concepts"),
    }


def page_two():
    terms = sorted(TERMS, key=lambda item: item["term"].lower())
    entries = []
    for term in terms:
        gaiish = term["kind"] == "gaiish"
        entries.append(
            '<div class="def"><span class="term">%s</span>'
            '<span class="kind%s">%s</span><p>%s</p></div>'
            % (
                esc(term["term"]),
                "" if gaiish else " general",
                "Gaiish" if gaiish else "General",
                esc(term["short"]),
            )
        )
    return """<section class="page">
%(masthead)s
<h2>Definitions</h2>
<div class="defs">%(entries)s</div>
<p class="muted" style="margin-top:3mm">Terms marked <strong>Gaiish</strong> are defined by Gaiish itself;
terms marked <strong>General</strong> are general generative-AI vocabulary included because Gaiish writers
need them. Full entries, related reading and examples for every term are at %(site)s/dictionary.</p>
%(foot)s
</section>""" % {
        "masthead": masthead(
            "Definitions",
            "The Gaiish Dictionary: %d terms. Gaiish terms are the components of the language; general "
            "terms are the generative-AI vocabulary a Gaiish writer needs." % len(terms),
        ),
        "entries": "".join(entries),
        "site": esc(config.SITE_URL),
        "foot": foot("Page 2 of 2 \u00b7 Definitions"),
    }


def main():
    document = (
        "<!DOCTYPE html><html lang=\"en\"><head><meta charset=\"utf-8\">"
        "<title>Gaiish — Key Concepts and Definitions</title><style>%s</style></head>"
        "<body>%s%s</body></html>" % (CSS, page_one(), page_two())
    )
    with open(OUT_HTML, "w", encoding="utf-8") as handle:
        handle.write(document)

    subprocess.run(
        [
            "google-chrome",
            "--headless=new",
            "--disable-gpu",
            "--no-sandbox",
            "--no-pdf-header-footer",
            "--print-to-pdf=" + OUT_PDF,
            "file://" + OUT_HTML,
        ],
        check=True,
        capture_output=True,
    )
    print("wrote", OUT_PDF, os.path.getsize(OUT_PDF), "bytes")


if __name__ == "__main__":
    main()
