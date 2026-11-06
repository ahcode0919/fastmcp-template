# CLAUDE.md

Python project template using `uv` for environment/dependency management and `just` as the command runner.

## Commands

See the [Project Commands](README.md#project-commands) section of `README.md`.

Run `just lint` and `just test` before considering a change done.

## Layout

- `src/example/` - the package (src layout, built with `uv_build`, installed editable by `uv sync`)
- `src/example/calculator.py` - the FastMCP server (`mcp`) and `main()` entry point, exposed as the
  `example` script
- `src/example/__main__.py` - runs `main()` for `python -m example`
- `tests/` - pytest tests; import the package as `from example.<module> import ...`
- `prek.toml` - git hook config (`prek install` to enable)
- `.github/workflows/` - `python.yml` (lint + tests), `security.yml` (zizmor, gitleaks),
  `release-drafter.yml` (draft release, PR labels), `release.yml` (manual release)
- `.github/release-drafter.yml` - release label → version bump / release notes section mapping
- `.github/dependabot.yml` - weekly updates for actions, uv, dev container image and features
- `.devcontainer/` - dev container; base image, `just`, and `uv` pinned by tag + digest
- `scripts/` - repo maintenance scripts

## Conventions

@pyproject.toml

## CI, security, and releases

- Pin GitHub Actions to a full commit SHA with a version comment (`uses: owner/action@<sha> # vX.Y.Z`);
  run `just zizmor` after editing workflows
- Give each workflow/job least-privilege `permissions`; set `persist-credentials: false` on checkout
  unless the job pushes
- Pin Docker images as `image:tag@sha256:<digest>`
- uv is pinned to 0.13.x in four places that must stay in sync: `[tool.uv] required-version` and the
  `uv_build` requirement in `pyproject.toml`, `setup-uv` `version` in the workflows, and the uv image in
  `.devcontainer/Dockerfile`
- Every PR needs a release label (GitHub PR label, not a title/commit prefix): `breaking`, `feature`,
  `enhancement`, `bug`, `fix`, `chore`, `ci`, `dependencies`, `documentation`, `refactor`, or `skip-changelog`
