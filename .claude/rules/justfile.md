# Use Justfile Tasks

Always invoke project tasks via `just` wherever a recipe exists. Do not run the underlying commands directly.

Current recipes:

| Recipe | Command | Use for |
|--------|---------|---------|
| `just install` | `uv sync` | Installing dependencies |
| `just lint` | ruff format + check | Checking formatting and linting |
| `just fmt` | ruff format | Auto-formatting source files |
| `just test` | `uv run pytest` | Running the test suite |
| `just run -- <args>` | `uv run butter <args>` | Running the CLI |

Fall back to direct commands only when no recipe covers the operation.
