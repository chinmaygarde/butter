# Automatic Agent Triggers

## docs-auditor

After completing a task that involves significant source code changes — new features, API changes, behavioral changes, or substantial refactoring — automatically invoke the `docs-auditor` agent to audit existing documentation and bring it in line with the current code. Skip this for minor bug fixes, trivial edits, or tasks that only touch documentation files.

## ci-build-sync

After editing any build configuration file, automatically invoke the `ci-build-sync` agent to review the changes and update CI/CD pipeline configuration accordingly.

Build configuration files include: `Makefile`, `CMakeLists.txt`, `CMakePresets.json`, `package.json`, `package-lock.json`, `yarn.lock`, `pnpm-lock.yaml`, `BUILD`, `BUILD.bazel`, `WORKSPACE`, `build.gradle`, `build.gradle.kts`, `settings.gradle`, `pom.xml`, any file under `.github/workflows/`, `.gitlab-ci.yml`, `.circleci/config.yml`, `Jenkinsfile`, `Dockerfile`, `docker-compose.yml`, `docker-compose.yaml`, `.travis.yml`, `azure-pipelines.yml`.
