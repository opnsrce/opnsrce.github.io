# LeviHackwith.com

Personal blog and knowledge site built with [Hugo][1] and the [PaperMod][2] (aka
PaperDoc) theme. Hosted on GitHub Pages. No analytics, no comments, no
unnecessary extras.

This is just me yelling into HTML about whatever I’m thinking and leaving my
notes lying around.

## Quick Start (Devcontainer)

This repo is configured to run in a VS Code devcontainer with Docker.

```bash
# Clone repo
git clone git@github.com:opnsrce/opnsrce.github.io.git levihackwithcom
cd levihackwithcom

# Open in VS Code and let devcontainer spin up
# Hugo will already be installed inside the container.

# Start local server
hugo server -D

# Build static site (minified)
hugo --gc --minify
```

### Manual Docker Commands

If you're not using VS Code's devcontainer integration, you can build and run
the Docker image directly:

```bash
# Build the Docker image
docker build -t levihackwithcom .

# Run a container interactively, mounting the current dir
docker run --rm -it -v $(pwd):/workspaces/levihackwithcom -p 1313:1313 levihackwithcom /bin/bash

# Inside the container:
hugo server -D --bind 0.0.0.0
```

View the site locally at http://localhost:1313

## Content Structure

Content lives in `/content/` and is split into:

- `/blog/` → casual posts + updates
- `/docs/` → technical notes & references
- `/links/` → curated link dumps
- `/projects/` → experiments & builds
- `/about/` → short bio page

Each section includes an `_index.md` file used by Hugo to define list pages.

Markdown files follow 80-char wrap (120 for code) enforced via linting.

## Deployment

[![Deploy Hugo site][8]][9]

This site uses a two-branch setup for deployment:

- **`master`** → Hugo source content, theme, and configuration.
- **`gh-pages`** → auto-generated static site, deployed via GitHub Actions.

GitHub Pages serves the `gh-pages` branch at [levihackwith.com][4]. This keeps
the build artifacts separate from the source.

### Manual Deployment (legacy)

Previously, deployment was manual via:

```bash
hugo --gc --minify
git subtree push --prefix public origin gh-pages
```

### Current Deployment

Now automated via GitHub Actions:

- Push to `master` triggers a build and deploy to `gh-pages`.
- Custom domain: [levihackwith.com][4]

## Contributing

 This repo is solo-maintained but enforces commit & lint standards:

- Commits follow [Conventional Commits][3]
  (`CONTRIBUTIONS.md` has details).
- Code linting is enforced with [Prettier][6].
- Markdown linting is enforced with [markdownlint][7].
- Husky hooks enforce commit linting and run a Hugo build on push.

## License

This project is licensed under the [MIT License][5].

[1]: https://gohugo.io/
[2]: https://github.com/adityatelange/hugo-PaperDoc
[3]: https://www.conventionalcommits.org/
[4]: https://levihackwith.com/
[5]: LICENSE
[6]: https://prettier.io/
[7]: https://github.com/DavidAnson/markdownlint
[8]: https://github.com/opnsrce/opnsrce-site/actions/workflows/deploy.yml/badge.svg
[9]: https://github.com/opnsrce/opnsrce-site/actions/workflows/deploy.yml
