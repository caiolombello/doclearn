# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## v1.4.1 (2024-08-25)

### chore

- **changelog**: Update CHANGELOG.md for version 1.4.0 release notes and improvements.

### fix

- **ci**: CI/CD workflow support tagging and extract tag name for Docker image.

## v1.4.0 (2024-08-25)

### chore

- **ci**: Add GitHub Actions CI/CD workflow for DocLearn application

### docs

- **README**: Update API endpoints section with translations and additional search endpoints.
- **changelog**: Update CHANGELOG.md to include version 1.3.0 release notes.
- **changelog**: Update CHANGELOG.md to reflect recent changes and improvements in the project.

### feat

- **google_search**: Add configuration option to enable or disable Google search functionality.

## v1.3.0 (2024-08-25)

### chore

- **commitizen**: Update commitizen configuration to use cz_gitmoji instead of cz_conventional_commits.

### docs

- **changelog**: Update CHANGELOG.md to reflect recent changes and improvements in the project.

### feat

- **google_client**: Add Google search functionality using the Custom Search API.

## [1.2.0] - 2024-08-25

### Added

- feat(api): Implemented new routes for repository and content search
- docs: Updated documentation to reflect new API functionalities

### Changed

- refactor: Improved code structure for better clarity and maintainability

## [1.1.0] - 2024-08-24

### Added

- ✨ feat(core/github_client): Implemented token rotation for GitHub API requests to handle rate limits

### Fixed

- ⬇️ fix(dependencies): Downgraded `cz_conventional_commits` from version 1.2.0 to 1.1.0
- 🔖 fix(version): Downgraded version from 1.2.0 to 1.1.0 in `pyproject.toml`

## [1.0.0] - 2024-08-22

### Added

- 🎉 feat(initial-setup): Initialized project with basic structure, including API routes, core logic, and documentation
- ✨ feat(api): Added initial API routes for managing Markdown files and repository information
- ✨ feat(docker): Added Dockerfile and updated dependencies for uvicorn
- ✨ feat(docs): Added Docker usage instructions and GPT integration link to README

[1.3.0]: https://github.com/caiolombello/doclearn/compare/v1.2.0...v1.3.0
[1.2.0]: https://github.com/caiolombello/doclearn/compare/v1.1.0...v1.2.0
[1.1.0]: https://github.com/caiolombello/doclearn/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.com/caiolombello/doclearn/releases/tag/v1.0.0