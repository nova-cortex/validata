# Contributing to Validata: AI-Powered Fake News Detector

Thank you for your interest in contributing to Validata! We welcome contributions from everyone and appreciate your help in making this tool more robust and effective in combating misinformation.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [How to Contribute](#how-to-contribute)
- [Development Setup](#development-setup)
- [Coding Standards](#coding-standards)
- [Commit Guidelines](#commit-guidelines)
- [Pull Request Process](#pull-request-process)
- [Issue Guidelines](#issue-guidelines)
- [Community](#community)

## Code of Conduct

This project and everyone participating in it is governed by our [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code. Please report unacceptable behavior to [ujjwalkrai@gmail.com](mailto:ujjwalkrai@gmail.com).

## Getting Started

### Prerequisites

Before you begin, ensure you have the following:
- Python 3.8+ installed
- `pip` (Python package installer)
- A GitHub account
- Git installed on your local machine
- Basic knowledge of Python, FastAPI, Streamlit, and Markdown
- API Keys:
    - **Google Gemini API Key**: For AI services.
    - **NewsAPI Key**: For news searching.

### First Time Setup

1. Fork the Validata repository on GitHub.
2. Clone your fork locally:
   ```bash
   git clone https://github.com/your-username/validata.git
   cd validata
   ```
3. Add the upstream repository:
   ```bash
   git remote add upstream https://github.com/nova-cortex/validata.git
   ```
4. Set up environment variables:
   Create a `.env` file in the root directory and add your API keys:
   ```
   GEMINI_API_KEY="YOUR_GEMINI_API_KEY"
   NEWSAPI_KEY="YOUR_NEWSAPI_KEY"
   BACKEND_URL="http://localhost:8000" # Default, change if your backend runs on a different host/port
   ```
5. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
7. Review the project structure:
```
fake-news-detector/
├── .env
├── LICENSE
├── pyproject.toml              # Project metadata and dependencies (PEP 621)
├── README.md
├── requirements.txt
├── assets/
│   ├── validata-banner.png
│   ├── validata-logo.png
│   └── screenshots/
│       └── screenshot.png
├── backend/
│   ├── app.py
│   ├── api/
│   │   ├── __init__.py
│   │   ├── search.py
│   │   └── verification.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── article_extractor.py
│   │   ├── credibility_scorer.py
│   │   ├── fact_checker.py
│   │   └── news_searcher.py
│   └── utils/
│       ├── __init__.py
│       └── helpers.py
├── docs/
│   ├── CHANGELOG.md
│   ├── CODE_OF_CONDUCT.md
│   ├── CONTRIBUTING.md
│   ├── README.md
│   ├── SECURITY.md
│   ├── STATUS.md
│   └── USAGE.md
└── frontend/
    ├── api_client.py
    ├── app.py
    ├── charts.py
    ├── display.py
    ├── error_components.py
    └── styles.py
```

## How to Contribute

### Types of Contributions

We welcome several types of contributions:

- **Feature Development**: Implement new AI models, data sources, or analysis capabilities.
- **Bug Fixes**: Identify and resolve issues in the backend logic or frontend display.
- **Performance Improvements**: Optimize code for faster processing and better resource utilization.
- **Documentation**: Enhance existing documentation or create new guides.
- **UI/UX Enhancements**: Improve the Streamlit interface for better user experience.
- **Testing**: Write unit, integration, or end-to-end tests.
- **Security Enhancements**: Improve the security posture of the application.

### Before You Start

1. Check existing [issues](https://github.com/nova-cortex/validata/issues) and [pull requests](https://github.com/nova-cortex/validata/pulls) to avoid duplicates.
2. For major changes or new features, please open an issue first to discuss your proposed changes.
3. Make sure your contribution aligns with Validata's goal of providing an effective AI-powered fake news detection tool.

## Development Setup

### Local Development

1. Create a new branch for your feature or improvement:
   ```bash
   git checkout -b feature/your-feature-name
   # or
   git checkout -b fix/issue-description
   # or
   git checkout -b docs/documentation-update
   ```

2. Make your changes following our [coding standards](#coding-standards).

3. Test your changes:
   - Run unit tests for backend services.
   - Manually test frontend functionality.
   - Verify API responses and data integrity.

4. Preview your changes:
   - Start the backend server (`cd backend && python app.py`).
   - Start the frontend application (`cd frontend && streamlit run app.py`).
   - Interact with the application in your browser to ensure changes work as expected.

## Coding Standards

### General Guidelines

- Follow PEP 8 for Python code.
- Write clear, readable, and well-commented code.
- Use meaningful variable and function names.
- Ensure code is modular and reusable.
- Handle errors gracefully and provide informative messages.

### Documentation Standards

#### Markdown Guidelines
- Use consistent heading hierarchy (`# ## ### ####`).
- Include table of contents for longer documents.
- Use code blocks with appropriate language highlighting.
- Include proper links and references.
- Follow standard Markdown formatting practices.

#### Code Documentation
- Document functions, classes, and complex logic using docstrings.
- Explain the purpose, parameters, and return values of functions.

### File Organization

- Keep related files in appropriate directories (e.g., `services`, `api`, `utils`).
- Use clear, descriptive file names.
- Maintain consistent directory structure.

## Commit Guidelines

We follow the [Conventional Commits](https://www.conventionalcommits.org/) specification for commit messages.

### Commit Message Format

```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

### Types

- `feat`: A new feature or enhancement.
- `fix`: A bug fix.
- `docs`: Documentation only changes.
- `style`: Changes that do not affect the meaning of the code (white-space, formatting, missing semicolons, etc.).
- `refactor`: A code change that neither fixes a bug nor adds a feature.
- `perf`: A code change that improves performance.
- `test`: Adding missing tests or correcting existing tests.
- `chore`: Maintenance tasks, build process changes, etc.

### Examples

```
feat(backend): add new credibility scoring algorithm

fix(frontend): resolve URL validation issue in input field

docs: update installation instructions in README

style(frontend): improve button styling in Streamlit app

refactor(services): extract common utility functions to helpers.py
```

## Pull Request Process

### Before Submitting

1. Ensure your branch is up to date with the `main` branch:
   ```bash
   git fetch upstream
   git rebase upstream/main
   ```
2. Run all tests and ensure they pass.
3. Review your changes thoroughly.
4. Update documentation if necessary.
5. Ensure all links and references work correctly.

### Submitting Your Pull Request

1. Push your branch to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```
2. Create a pull request from your fork to the `main` branch of the `nova-cortex/validata` repository.
3. Fill out the pull request template completely.
4. Link any related issues using keywords (e.g., "Closes #123").

### Pull Request Template

When creating a pull request, please include:

- **Description**: Clear description of what changes you made.
- **Motivation**: Why are these changes needed?
- **Type of Change**: Bug fix, new feature, documentation, etc.
- **Testing**: How did you test your changes?
- **Screenshots**: If applicable, add screenshots of visual changes.
- **Breaking Changes**: List any breaking changes.
- **Checklist**: Complete the provided checklist.

### Review Process

1. All pull requests require at least one review from a maintainer.
2. Address any feedback or requested changes promptly.
3. Once approved, a maintainer will merge your pull request.
4. Your contribution will be included in the next release.

## Issue Guidelines

### Before Creating an Issue

1. Search existing issues to avoid duplicates.
2. Check if the issue might be related to your specific use case.
3. Gather relevant information (screenshots, error logs, steps to reproduce).

### Bug Reports

When reporting a bug, please include:

- **Bug Description**: Clear and concise description.
- **Steps to Reproduce**: How to reproduce the issue.
- **Expected Behavior**: What you expected to happen.
- **Actual Behavior**: What actually happened.
- **Component Affected**: Which part of the application (backend, frontend, specific service) has the issue.
- **Additional Context**: Screenshots, error messages, browser console logs, etc.

### Feature Requests

When requesting a feature, please include:

- **Feature Description**: Clear description of the proposed feature.
- **Use Case**: Why is this feature needed? What problem does it solve?
- **Proposed Solution**: Your ideas for implementation.
- **Examples**: Examples from other projects or mockups if applicable.
- **Additional Context**: Any other relevant information.

## Community

### Getting Help

If you need help or have questions, don't hesitate to:
- Open an issue with the "question" label.
- Email us at [ujjwalkrai@gmail.com](mailto:ujjwalkrai@gmail.com).
- Check existing documentation for examples.

### Recognition

We appreciate all contributions and maintain a contributors list to recognize everyone who has helped improve this project. All contributors will be acknowledged in our documentation.

### License

By contributing to this project, you agree that your contributions will be licensed under the MIT License, the same license as the project. See [LICENSE](../LICENSE) for details.

---

## Quick Reference

### Common Commands

```bash
# Setup
git clone https://github.com/nova-cortex/validata.git
cd validata
git remote add upstream https://github.com/nova-cortex/validata.git

# Install dependencies (from root)
pip install -r requirements.txt

# Development
git checkout -b feature/new-feature
# Make your changes
git add .
git commit -m "feat: add new feature X"
git push origin feature/new-feature

# Running the application
# In backend directory:
# python app.py
# In frontend directory:
# streamlit run app.py
```

### 📞 Support

- **📧 Email**: [ujjwalkrai@gmail.com](mailto:ujjwalkrai@gmail.com)
- **🐛 Issues**: [Validata Issues](https://github.com/nova-cortex/validata/issues)
- **🔓 Security**: [Validata Security](https://github.com/nova-cortex/validata/security)
- **⛏ Pull Requests**: [Validata Pull Requests](https://github.com/nova-cortex/validata/pulls)
- **📖 Documentation**: [Validata Documentation](https://github.com/nova-cortex/validata/tree/main/docs)

### Need Help?

If you're new to contributing or need assistance:
- Review our existing code and documentation for examples.
- Check the project structure and follow existing patterns.
- Don't hesitate to ask questions in issues or via email.
- Start with small improvements to get familiar with the project.

Thank you for contributing to Validata! Together, we're building a powerful tool to help users navigate the complex news landscape. 🎉
