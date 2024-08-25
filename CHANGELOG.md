# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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

[1.2.0]: https://github.com/caiolombello/doclearn/compare/v1.1.0...v1.2.0
[1.1.0]: https://github.com/caiolombello/doclearn/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.com/caiolombello/doclearn/releases/tag/v1.0.0