# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```bash
just install      # install dependencies (uv sync)
just lint         # ruff format --check + ruff check (what CI runs)
just fmt          # auto-format with ruff
just test         # run full test suite with pytest
just run -- ARGS  # run the butter CLI (e.g. just run -- --help)
```

Run a single test file: `uv run pytest tests/test_cli.py`
Run a single test by name: `uv run pytest -k test_help`

## Architecture

This is a Python CLI tool built with [Click](https://click.palletsprojects.com/) and [Rich](https://rich.readthedocs.io/). The entry point is `butter_tree.cli:main`.

**Key layout:**
- `src/butter_tree/cli.py` — top-level `cli` Click group; registers sub-commands and defines `add`, `list`, `remove` stubs
- `src/butter_tree/doctor.py` — `doctor` command group with the `filesystem` subcommand; uses `ctypes`/`statfs` to detect BTRFS without shelling out
- `tests/test_cli.py` — uses Click's `CliRunner` for all tests; no subprocess invocation

**Design conventions:**
- CLI callbacks stay thin — business logic lives in modules, not Click handlers
- All user-facing output goes through `rich.console.Console`; no bare `print()`
- Type hints required on all public functions
- `add`, `list`, and `remove` commands are stubs; only `doctor filesystem` is implemented

The tool targets Linux + BTRFS at runtime, but the test suite runs on macOS/Linux (CI matrix covers both).
