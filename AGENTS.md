# ThinkLab website: notes for AI assistants and new sessions

Read this before changing anything in this folder.

## 1. Sync first (this site is edited from two computers)

- Run `git pull` **before** editing anything.
- Run `git fetch && git status` **before** pushing. If GitHub is ahead, bring those commits in first and never overwrite them.
- On 2026-10-22, one computer was 7 commits behind GitHub, and a push nearly clobbered that morning's work (blog setup, famine-photo blurring).

## 2. How the site works

- Plain static HTML, published by GitHub Pages from the `main` branch of `takyurp09/thinklabep` to **thinklabep.org** (see `CNAME`).
- Pushing to `main` puts changes live in about a minute. If the deploy sits "queued" for more than a few minutes, start a fresh build:
  `gh api -X POST repos/takyurp09/thinklabep/pages/builds`
- **Everything committed is public** on thinklabep.org.
- Local preview: `python3 -m http.server 8765`, then open http://localhost:8765

### index.html
- One page split into tabs. Each `<section>` has a `data-tab` attribute, and the script at the bottom shows one tab at a time.
- A new section must have `data-tab`. An extra section inside a tab (like `#latest` or `#subscribe`) must come directly after another section of the same tab, or the scroll-to-section link won't work.

### assets/style.css
- After changing the CSS, bump the cache version `style.css?v=N` in `index.html` **and** in every `blog/*.html`. It is currently `v=4`.
- The rule `section[data-tab]:not(#home)` sets a min-height. Overriding it needs higher specificity (see the `#blog` / `#subscribe` rule near the end of the file).

### blog/
- Each post is a standalone HTML page. Bangla posts use `class="bn"` on `<body>` and on their homepage card.
- For each new post: add a card to `.blog-grid` in `index.html` with `data-lang="bn"` or `data-lang="en"`. Update the "Latest from ThinkLab" strip, and add next/previous links if the post is part of a series (e.g. নোবেলের অর্থনীতি).
- `blog/facebook-captions.md` is a private draft and is in `.gitignore`.

### Videos and tutorials
- Videos live on YouTube (@ThinkLabEP) and are embedded by video ID. **Never commit video files** (GitHub's limit is 100 MB, and the intro video alone is about 545 MB).
- The Tutorials section lists lectures by hand. When a new lecture is uploaded, add it to its series list in `index.html`.

## 3. Do not publish

- Personal images in `assets/images/` that the site doesn't use (Al_Aqsa, kabba_*, MAsjid Nawabi, and others). Leave them uncommitted.
- `blog/img/sen-1943-b.jpg`: unused, and possibly an unblurred famine photo. The famine photos are blurred on purpose; keep them that way.
- Video, `.pptx` and `.pdf` files (already in `.gitignore`).

## 4. Current status (October 2026)

- ThinkLab is **not recruiting**. The old "Join Us" section is now "Collaborate", so don't add hiring or "paid position" language.
- The email signup opens the visitor's email app (mailto). It could move to a real service such as Buttondown.
- Still to do: founder links (Google Scholar, LinkedIn, CV) on the Team card, a public link for the climate-shocks working paper, and fixing the YouTube title typo "Introuducing ThinkLab".
