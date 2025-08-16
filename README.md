# LeviHackwith.com

Personal blog and knowledge site built with [Hugo][01] and the [PaperMod][02]
(aka PaperDoc) theme. Hosted on GitHub Pages. No analytics, no comments, no
unnecessary extras.

This is just me yelling into HTML about whatever I’m thinking and leaving my
notes lying around.

## Quick start (devcontainer)

This repo is configured to run in a VS Code devcontainer with Docker.

```bash
# Clone repo (directory name is optional)
git clone git@github.com:opnsrce/opnsrce.github.io.git levihackwithcom
cd levihackwithcom

# Open in VS Code and let devcontainer spin up
# Hugo will already be installed inside the container.

# Start local server
hugo server -D

# Build static site (minified)
hugo --gc --minify
```

### VS Code: open folder in devcontainer

If you have Docker and the [Dev Containers extension][10] installed,
VS Code will prompt you to reopen the project in a container. Confirm the prompt
and VS Code will launch the prebuilt Docker devcontainer with Hugo and other
dependencies already installed.

If VS Code doesn't prompt you, you can pull up the command pallete
(`Cmd/Ctrl+Shift+P`) and run `Dev Containers: Open Folder in Container`
manually.

View the site via [localhost][11].

## Content structure

Content lives in `/content/` and is split into:

- `/blog/` → casual posts + updates
- `/docs/` → technical notes & references
- `/links/` → curated link dumps
- `/projects/` → experiments & builds
- `/about/` → short bio page

Each section includes an `_index.md` file used by Hugo to define list pages.

Markdown files follow 80-char wrap (120 for code) enforced via linting.

## Deployment

[![Deploy Hugo site][08]][09]

This site is deployed via GitHub Actions:

- Push to `master` triggers an automated build and deploy via GitHub Actions.

## Contributing

This repo is solo-maintained but enforces commit & lint standards:

- Commits follow [Conventional Commits][03]
  (`CONTRIBUTIONS.md` has details).
- Code linting is enforced with [Prettier][06].
- Markdown linting is enforced with [markdownlint][07].
- Husky hooks enforce commit linting and run a Hugo build on push.

## License

This project is licensed under the [MIT License][05].

[01]: https://gohugo.io/
[02]: https://github.com/adityatelange/hugo-PaperDoc
[03]: https://www.conventionalcommits.org/
[05]: LICENSE
[06]: https://prettier.io/
[07]: https://github.com/DavidAnson/markdownlint
[08]: https://github.com/opnsrce/opnsrce.github.io/actions/workflows/deploy.yml/badge.svg
[09]: https://github.com/opnsrce/opnsrce.github.io/actions/workflows/deploy.yml
[10]: https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers
[11]: http://localhost:1313
