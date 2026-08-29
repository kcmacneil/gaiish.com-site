# Gaiish content and tools

The site is a generated static site. Python modules under `sitegen/content/` contain page
data and small page factories; `sitegen/render.py` turns each page dictionary into HTML.
Generated HTML, `sitemap.xml`, `robots.txt` and `vercel.json` are committed at the repository
root. `sitegen/config.py` is the contract for identity, canonical definitions, navigation,
frameworks, redirects, `SPEC_VERSION` and `LAST_UPDATED`.

## Adding knowledge content

### Dictionary term

Add a dictionary to `TERMS` in `sitegen/content/knowledge.py` with:

* a stable lowercase `slug`;
* `term`, concise `short` definition, and substantive `body` paragraphs;
* `kind: "gaiish"` for an official Gaiish component or `kind: "general"` for general AI
  terminology;
* `links` pointing to relevant method sections, framework pages or topic articles.

The module sorts the dictionary alphabetically, creates the A–Z index and generates both
`/dictionary` and `/dictionary/<slug>`. Its `DefinedTermSet` and `DefinedTerm` JSON-LD are
generated from the same visible definition data.

### Prompt example

Add a dictionary to `EXAMPLES` with `title`, `traditional`, `gaiish`, `why`, and `links`.
Use a real domain task. The explanation must name the components added and explain why the
structure is useful; do not add shallow keyword variations.

### Prompt-library category

Add a dictionary to `LIBRARY` with an exact category name and an `entries` list. Each entry is
`(title, prompt, why, links)`. Keep prompts complete enough to adapt, use relevant links to
the dictionary or method, and never include private or fabricated source material.

## Specification versions

For a new version, create a sibling page route such as
`/gaiish-language/specification-1-1` (do not overwrite the current version). Use
`config.SPEC_VERSION` for the current specification's visible version string, add the new
version to navigation when it is current, and add a dated entry to `sitegen/content/authority.py`
or the changelog page. Re-run the build so the sibling route and sitemap entry are generated.

## Browser tools

The prompt builder fields are Goal / Intent, Context, Audience, Role, Knowledge, Instructions,
Constraints, Output, Tone and Validation. `tools/prompt-builder.js` formats non-empty fields,
supports clipboard copy with a fallback, and saves/restores the fields with `localStorage`.

The analyzer loads the authored `tools/analyzer-score.js` unchanged. Its component weights are
Intent 20, Context 20, Instruction 20, Constraints 15, Output 15 and Validation 10. The score
is a heuristic based on how explicitly the prompt expresses the framework; it is not a
validated measurement and cannot establish truth, quality or model behaviour. The UI uses
`window.GaiishScore.analyze` and `window.GaiishScore.toGaiish`.

## SEO and structured data

Every generated page has a unique title, description and canonical URL from its page dictionary.
Knowledge pages emit `DefinedTermSet` / `DefinedTerm`; the two tool pages emit accurate
browser-based, free `WebApplication` objects. Do not add claims that are not visible in the
page content. `build.py` includes generated routes and hand-written legacy routes in
`sitemap.xml`.

## Build and deployment

1. Edit the relevant content module or browser script.
2. Run `python3 build.py`.
3. Review the generated HTML and sitemap, then commit generated output with the source change.
4. Push the commit to `main`.
5. Vercel serves the committed static files and deploys automatically.

There is no Vercel build step. Locally, preview with `python3 -m http.server 8000`.

## Google Search Console

Verify the `gaiish.com` domain in Google Search Console, then submit
`https://gaiish.com/sitemap.xml`. Inspect the home page, `/what-is-gaiish`,
`/gaiish-method`, `/gaiish-language/specification`, `/dictionary`, `/examples`,
`/prompt-library`, and both tool URLs. Monitor indexing coverage and queries containing
“Gaiish”, “AI prompting”, “prompt engineering” and “human-AI communication”. Find pages
with high impressions but low click-through rate, then improve their visible title,
description and opening copy without making unsupported claims.

## Analytics and privacy

`site.js` exposes a small `window.gaiishTrack(event, detail)` shim. If a future analytics
integration provides `window.dataLayer`, the shim pushes safe event metadata; otherwise it is
a no-op. Builder and analyzer events identify actions such as viewed, generated, copied,
saved, analyzed or converted. **Never pass prompt text, field values or source material to
analytics.** There are no third-party analytics, cookies or server submissions in these tools.

## Preserved content and redirects

The original `/generative-ai`, `/topics/*`, `/principles/*`, `/outcomes/*` and interactive
brand map content remain available. The map is now at `/gaiish-map` so the generated home page
can be the authoritative Gaiish introduction.

The redirect map is defined in `sitegen/config.py` and generated into `vercel.json`:

| Legacy route | Destination |
| --- | --- |
| `/prompt-builder` | `/tools/prompt-builder` |
| `/prompt-analyzer` | `/tools/prompt-analyzer` |
| `/specification` | `/gaiish-language/specification` |
| `/method` | `/gaiish-method` |
| `/basic` | `/gaiish-basic` |
| `/pro` | `/gaiish-pro` |
| `/learn` | `/learn-gaiish` |
| `/glossary` | `/dictionary` |
