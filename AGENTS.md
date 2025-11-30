# Repository Guidelines

## Project Structure & Module Organization
- `pipeline.py`: CLI entry and end-to-end generation pipeline.
- `template_generator.py`, `section_library.py`, `design_system.py`: Core generation, reusable sections, and design skins.
- `template_validator.py`: Heuristics and auto-fixes for output quality.
- `mjml_converter.py`: MJML conversion and optional HTML compilation.
- `external_sources.py`: Fetches public templates and extracts patterns.
- `preview_server.py`: Local browser preview server (`--preview`).
- `package.json`: Node dependency `mjml`; run `npm install` once.
- Outputs: JSON batches (e.g., `output_batch.json`) and optional compiled HTML.

## Build, Test, and Development Commands
- Install MJML (local): `npm install` in repo root.
- Generate batch: `python3 pipeline.py --output output_batch.json`.
- Single template: `python3 pipeline.py -t welcome_basic -s apple_light`.
- Convert to MJML: `python3 pipeline.py -f mjml --output batch_mjml.json`.
- Compile MJML→HTML: `python3 pipeline.py --compile --output compiled.json` (requires MJML CLI; optionally `npm i -g mjml`).
- Preview server: `python3 pipeline.py --preview --port 8080`.

## Coding Style & Naming Conventions
- Python: PEP 8, 4-space indent, `snake_case` for functions/vars, `CapWords` for classes, `UPPER_SNAKE_CASE` for constants.
- Keep modules cohesive; prefer pure functions; add type hints and docstrings.
- JSON fields and template tokens are lower_snake; keep section ids stable.

## Testing Guidelines
- Prefer `pytest`; name tests `test_*.py` near related modules or under `tests/`.
- Cover: section extraction, normalization, MJML conversion, and validator fixes.
- Run locally: `pytest -q` (add as dev dependency if introducing tests).

## Commit & Pull Request Guidelines
- Commits: imperative mood, concise scope, e.g., "Add MJML converters for remaining section types".
- Reference PR/issue when relevant, e.g., `(#12)`.
- PRs must include: purpose, notable changes, how to run (`python3 …`), and before/after notes or screenshots (if HTML output affected).
- Ensure no large generated files are committed; add samples under a short, representative path.

## Security & Agent Notes
- Only use public, legally safe sources; replace brand assets with placeholders (see `OBJECTIVE.md`).
- Do not commit secrets or API keys. Network usage should respect source licenses.
- Keep layouts 640px max width and use provided tokens/placeholders to ensure portability.
