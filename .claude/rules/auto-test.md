# Automatic Test Runs

After completing any task that involves source code changes or build configuration changes, run the full test suite before considering the task done:

```
uv run pytest
```

If tests fail, fix the failures before finishing. Do not skip or ignore failing tests.
