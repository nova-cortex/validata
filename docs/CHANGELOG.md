# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- New features that have been added but not yet released

### Changed
- Changes in existing functionality

### Deprecated
- Soon-to-be removed features

### Removed
- Features that have been removed

### Fixed
- Bug fixes

### Security
- Security improvements and vulnerability fixes

## [1.0.0] - 2025-10-29

### Added
- Initial release of Validata: AI-Powered Fake News Detector.
- Implemented FastAPI backend for AI services (article extraction, credibility scoring, fact-checking, news searching).
- Developed Streamlit frontend for interactive user interface.
- Integrated Google Gemini API for advanced AI analysis.
- Integrated NewsAPI for multi-source news article access.
- Comprehensive documentation: `README.md`, `CONTRIBUTING.md`, `USAGE.md`, `CHANGELOG.md`, `CODE_OF_CONDUCT.md`, `SECURITY.md`, `STATUS.md`.
- Custom CSS styling for a modern and professional UI/UX.
- Error handling and informative error messages for various scenarios (connection, timeout, invalid URL, API rate limits, extraction failures).

### Changed
- Renamed project from "Repo Blueprint" to "Validata: AI-Powered Fake News Detector".
- Updated all documentation files (`README.md`, `CONTRIBUTING.md`, `USAGE.md`) to reflect the new project name, features, and structure.
- Replaced placeholder images and banner with Validata-specific assets.
- Modified folder structure description to accurately represent the Validata codebase.

### Fixed
- Ensured all internal links in documentation are updated and functional.
- Corrected installation and usage instructions to match Validata's Python-based backend and frontend.

---

## Guidelines for Contributors

When adding entries to this changelog:

1. **Group changes** by type using the categories above
2. **Write for humans** - use clear, descriptive language
3. **Include issue/PR numbers** when relevant: `Fixed login bug (#123)`
4. **Date format** should be YYYY-MM-DD
5. **Version format** should follow [Semantic Versioning](https://semver.org/)
6. **Keep entries concise** but informative

### Version Number Guidelines
- **Major** (X.y.z) - Breaking changes
- **Minor** (x.Y.z) - New features, backwards compatible
- **Patch** (x.y.Z) - Bug fixes, backwards compatible

### Example Entry Format
```markdown
## [1.2.3] - 2024-01-15

### Added
- New feature description (#PR-number)

### Fixed
- Bug fix description (fixes #issue-number)
```
