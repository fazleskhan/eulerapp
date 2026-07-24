# eulerapp

This repository is a [Dev Container](https://containers.dev/) environment set up to work through
Anthropic's **Claude Partner Network Learning Path** on [Skilljar](https://anthropic.skilljar.com/).
Opening this repo in VS Code (or GitHub Codespaces) with the Dev Containers extension builds a
ready-to-use environment with all the tools and dependencies needed to complete the course
exercises.

## What the devcontainer sets up

Defined in [`.devcontainer/devcontainer.json`](.devcontainer/devcontainer.json), the container:

- Uses the `mcr.microsoft.com/devcontainers/python:3-3.13-trixie` base image (Python 3.13)
- Adds Node.js via the `devcontainers/features/node` feature
- Forwards ports `6274`/`6277` for the MCP Inspector UI and proxy
- Runs [`scripts/postCreateCommand.sh`](scripts/postCreateCommand.sh) on creation, which:
  - Installs the [MCP Inspector](https://github.com/modelcontextprotocol/inspector) globally via npm
  - Installs Python dependencies from `requirements.txt`
  - Installs the [Claude Code](https://claude.com/claude-code) CLI
  - Prevents local changes to `.env` from being committed (`git update-index --skip-worktree`)
- Configures recommended VS Code extensions (Jupyter, PDF viewer, Python envs)

## Repository layout

| Path | Description |
| --- | --- |
| [`cli_project/`](cli_project) | MCP Chat — a CLI chat app built on the Anthropic API and MCP |
| [`app_starter/`](app_starter) | Starter project for building MCP document tools |
| `jupyter/` | Notebooks used throughout the learning path |
| `scripts/` | Setup scripts run by the devcontainer |
| `saved/` | Saved exercise output/artifacts |

## Getting started

1. Open this repository in VS Code and reopen in the container when prompted (or launch via
   GitHub Codespaces).
2. Wait for `postCreateCommand.sh` to finish provisioning the environment.
3. Set your `ANTHROPIC_API_KEY` in the `.env` file at the repo root.
4. See each subproject's README (e.g. [`cli_project/README.md`](cli_project/README.md)) for
   exercise-specific setup and usage instructions.

## License

MIT — see [LICENSE](LICENSE).
