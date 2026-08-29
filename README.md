# gaiish.com-site

The gaiish.com site. gaiish is a language humans use to optimise communication with generative AI models; the front page presents that idea (clarity, context, intent, precision, result), then covers the underlying generative AI technologies and a reference list of language models, with a detail page per technology. Static site hosted on Vercel (project `gaiish-com-site`, domains gaiish.com and www.gaiish.com).

## Files

- `index.html` — front page
- `principles/*.html` — the five gaiish principles (clarity, context, intent, precision, result) with prompt examples
- `topics/*.html` — detail pages (transformers, diffusion, multimodal, embeddings & RAG, fine-tuning, agents)
- `assets/hero.jpg` — hero image
- `assets/brand/` — brand reference image and alternate renders used as templates for new imagery
- `styles.css` — styling
- `vercel.json` — Vercel config (clean URLs)

## Local preview

```bash
python3 -m http.server 8000
# open http://localhost:8000
```

## Deploy

Connect this repository to Vercel (Add New → Project → import `gaiish.com-site`), or from the CLI:

```bash
npx vercel        # preview deployment
npx vercel --prod # production deployment
```


