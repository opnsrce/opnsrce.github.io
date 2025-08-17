# Repository guidelines

You are an LLM agent contributing to a Hugo static site that uses the
PaperMod theme and GitHub Pages. Follow these instructions to make precise,
safe, and minimal changes.

## Quick checklist

- Read commit rules and writing standards in `CONTRIBUTIONS.md`.
- For posts, use `content/blog/<slug>/index.md` with images adjacent.
- Validate locally: `hugo server -D`; lint:
  `npx markdownlint-cli AGENTS.md -c .markdownlint.json`.
- Do not edit `public/`, theme code, or CI unless requested.

## When to edit what

- `content/blog/<slug>/index.md`: Write or update posts; keep images alongside.
- `hugo.json`: Tweak menus, params, or theme config; justify changes in the PR.
- `.github/workflows/`: Edit only for deploy/build changes; coordinate in PRs.
- `themes/PaperMod/`: Do not modify; prefer overrides via project `layouts/`.
- `public/`: Never edit; it is generated output.

## Project structure and module organization

- `content/`: Author posts at `content/blog/<slug>/index.md` with images in
  the same folder (e.g., `cover.jpg`).
- `themes/PaperMod/`: Theme code. Do not modify unless asked.
- `archetypes/`: Content templates.
- `public/`: Hugo build output. Never edit.
- `.github/workflows/`: CI and Pages deploy. Avoid changes unless requested.

## Build, test, and development commands

- `hugo server -D --config hugo.json`: Serve locally with drafts; hot reload.
- `hugo --gc --minify --config hugo.json`: Production build to `public/`.
- `npm ci`: Install tools (husky, commitlint, prettier).
- `npm run lint`: Apply Prettier to supported files.

CI runs on a daily schedule (00:05 UTC) and manual dispatch.

## Coding style and naming conventions

- Prettier: Use `.prettierrc` as the single source of truth. Do not copy
  rules into docs. Run `npm run lint` before proposing changes.
- Markdown: Prettier ignores `*.md` (see `.prettierignore`). Follow
  `.markdownlint.json` for headings, line length, and list style.
- Content layout: One folder per post (`content/blog/my-post/index.md`) with
  images adjacent. Include `title`, `date` or `publishDate`, `summary`,
  `tags`, and `cover.image`.
- For tags and filenames, follow
  [content and file naming conventions][03].

Example front matter (minimal):

```yaml
---
title: "My post title"
date: 2025-01-15
tags: [hugo, ci]
cover:
  image: cover.jpg
summary: "One or two sentences about the post."
---
```

## Scheduling posts

- Use `publishDate` to control publish timing; include timezone.
- CI runs daily at `00:05` UTC; content publishes when `date`/`publishDate` is
  in the past as of that build (UTC).
- Date-only values publish at `00:00:00` UTC for that date.

Example scheduled post:

```yaml
---
title: "My scheduled post"
publishDate: 2025-09-01T15:00:00Z
draft: false
tags: [hugo]
---
```

## Testing guidelines

- No unit tests; builds must succeed locally and in CI.
- Validate content renders: `hugo server -D` and click through pages.
- Ensure dates are correct. Drafts (`draft: true`) won't publish; scheduled
  posts build when `date/publishDate <= now` (UTC).

## Commit and pull request guidelines

- Follow commit rules in [CONTRIBUTIONS.md: commit standards][01]
  (Conventional Commits). Commitlint enforces messages.
  Examples:
  - `feat(blog): add daily-notes article`
  - `fix(blog): correct broken link` with footer `Closes #123`
- For PRs, include a clear description, link issues with tokens
  (e.g., `Closes #123`), and add screenshots for visual changes.
- Husky runs commit checks and a production build on push.

## Security and configuration tips

- No secrets are needed; the site is static. Avoid third-party scripts unless
  necessary and document the rationale in the PR.
- Do not commit generated files (`public/`) or theme vendored changes.
- Honor the nav and params in `hugo.json`; update intentionally with context.

## Writing and formatting

- Follow the writing and formatting standards in
  [CONTRIBUTIONS.md: writing and formatting standards][02].

[01]: CONTRIBUTIONS.md#commit-standards
[02]: CONTRIBUTIONS.md#writing-and-formatting-standards
[03]: CONTRIBUTIONS.md#content-and-file-naming-conventions
