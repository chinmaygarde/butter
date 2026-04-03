default:
    @just --list

# Install all dependencies
install:
    uv sync

# Check formatting and linting
lint:
    uv run ruff format --check src/
    uv run ruff check src/

# Auto-format source files
fmt:
    uv run ruff format src/

# Run the test suite
test:
    uv run pytest

# Run the butter CLI (use: just run -- --help)
run *args:
    uv run butter {{ args }}

# Install the butter CLI as a uv tool
install-tool:
    uv tool install --reinstall .
