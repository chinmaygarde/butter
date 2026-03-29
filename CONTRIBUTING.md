# Contributing to butter

## Dev Setup

1. Clone the repo and enter the directory:
   ```bash
   git clone https://github.com/chinmaygarde/butter.git
   cd butter
   ```

2. Install dependencies (requires [uv](https://docs.astral.sh/uv/) and [just](https://just.systems/)):
   ```bash
   just install
   ```

3. Activate the virtual environment:
   ```bash
   source .venv/bin/activate
   ```

## Common Tasks

All developer workflows are managed through the `Justfile`:

```bash
just          # list available recipes
just install  # install all dependencies (uv sync)
just lint     # check formatting and linting (ruff)
just fmt      # auto-format source files (ruff format)
just test     # run the test suite (pytest)
just run      # run butter CLI (just run -- --help)
```

## Coding Conventions

- **Type hints** on all public functions and methods.
- **Ruff** for formatting and linting. CI enforces `ruff format --check` and `ruff check`.
- Keep CLI logic thin — business logic lives in modules, not in Click callbacks.
- Use `rich` for all user-facing output; avoid bare `print()`.

## Pull Request Process

1. Branch off `main`: `git checkout -b feat/my-feature`
2. Make your changes and add tests.
3. Ensure CI passes locally: `just lint && just test`
4. Open a PR against `main` with a clear description of what and why.
5. A maintainer will review and merge.

## Running Tests

```bash
just test
# or directly:
uv run pytest
```

Tests live in `tests/`. Add a test file per module (`tests/test_cli.py`, etc.).
