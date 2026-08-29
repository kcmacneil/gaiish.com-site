# gaiish.com-site

The gaiish.com site: a front page about generative AI technologies with a reference list of language models, plus detail pages for each technology. Static site hosted on Vercel (project `gaiish-com-site`, domains gaiish.com and www.gaiish.com).

## Files

- `index.html` — front page
- `topics/*.html` — detail pages (transformers, diffusion, multimodal, embeddings & RAG, fine-tuning, agents)
- `assets/hero.jpg` — hero image
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


