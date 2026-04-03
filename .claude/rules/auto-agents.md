# Automatic Agent Triggers

When multiple auditor agents are triggered at the end of a task, launch them all in parallel (single message, multiple Agent tool calls).

## both (docs-auditor + ci-build-sync)

After any task involving significant source code changes **or** build configuration changes, launch both `docs-auditor` and `ci-build-sync` in parallel. This covers the union of their individual triggers — when in doubt, launch both.

## docs-auditor

After completing a task that involves significant source code changes — new features, API changes, behavioral changes, or substantial refactoring — automatically invoke the `docs-auditor` agent to audit existing documentation and bring it in line with the current code. Skip this for minor bug fixes, trivial edits, or tasks that only touch documentation files.

## ci-build-sync

After editing any build configuration file, automatically invoke the `ci-build-sync` agent to review the changes and update CI/CD pipeline configuration accordingly.

Build configuration files include: `Makefile`, `CMakeLists.txt`, `CMakePresets.json`, `package.json`, `package-lock.json`, `yarn.lock`, `pnpm-lock.yaml`, `BUILD`, `BUILD.bazel`, `WORKSPACE`, `build.gradle`, `build.gradle.kts`, `settings.gradle`, `pom.xml`, any file under `.github/workflows/`, `.gitlab-ci.yml`, `.circleci/config.yml`, `Jenkinsfile`, `Dockerfile`, `docker-compose.yml`, `docker-compose.yaml`, `.travis.yml`, `azure-pipelines.yml`.
