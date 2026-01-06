# Contributing to ConvertAPI Python Client

Thank you for your interest in contributing to the ConvertAPI Python Client! This document provides guidelines and instructions for contributing.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Environment Setup](#development-environment-setup)
- [Coding Standards](#coding-standards)
- [Testing Requirements](#testing-requirements)
- [Pull Request Process](#pull-request-process)
- [Reporting Bugs](#reporting-bugs)
- [Suggesting Enhancements](#suggesting-enhancements)

## Code of Conduct

This project and everyone participating in it is governed by our [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code.

## Getting Started

1. Fork the repository on GitHub
2. Clone your fork locally:
   ```bash
   git clone https://github.com/YOUR_USERNAME/convertapi-library-python.git
   cd convertapi-library-python
   ```
3. Add the upstream repository:
   ```bash
   git remote add upstream https://github.com/Nietzsche-Ubermensch/convertapi-library-python.git
   ```

## Development Environment Setup

1. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install the package in development mode with all dependencies:**
   ```bash
   pip install -e ".[dev,test]"
   ```

3. **Set up your ConvertAPI credentials:**
   ```bash
   export CONVERT_API_SECRET=your_api_token_here
   ```

## Coding Standards

We follow [PEP 8](https://pep8.org/) style guidelines with some modifications:

### Style Guidelines

- **Line Length**: Maximum 120 characters (enforced by ruff)
- **Indentation**: 4 spaces (no tabs)
- **Imports**: Group imports in the following order:
  1. Standard library imports
  2. Third-party imports
  3. Local application imports
- **Type Hints**: Required for all public functions and methods
- **Docstrings**: Required for all public modules, classes, and functions
  - Use Google-style docstrings
  - Include parameter types and return types
  - Provide usage examples for complex functions

### Code Quality Tools

Run these tools before submitting a pull request:

```bash
# Format and lint code
ruff check convertapi --fix
ruff format convertapi

# Type checking
mypy convertapi

# Run tests with coverage
pytest --cov=convertapi --cov-report=term-missing
```

### Example Function with Type Hints and Docstring

```python
from typing import Dict, Optional

def convert(to_format: str, params: Dict[str, any], 
            from_format: Optional[str] = None, 
            timeout: Optional[int] = None) -> 'Result':
    """Convert a file to the specified format.
    
    Args:
        to_format: Target file format (e.g., 'pdf', 'jpg').
        params: Conversion parameters including 'File' path or URL.
        from_format: Source format (auto-detected if not provided).
        timeout: Request timeout in seconds.
        
    Returns:
        Result object containing converted files.
        
    Raises:
        ApiError: If the conversion fails or credentials are invalid.
        
    Example:
        >>> import convertapi
        >>> convertapi.api_credentials = 'your-token'
        >>> result = convertapi.convert('pdf', {'File': 'document.docx'})
        >>> result.file.save('output.pdf')
    """
    task = Task(from_format, to_format, params, timeout=timeout)
    return task.run()
```

## Testing Requirements

### Writing Tests

- Write tests for all new features and bug fixes
- Place tests in the `tests/` directory
- Use descriptive test names: `test_<functionality>_<scenario>`
- Maintain or improve code coverage (aim for >80%)

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage report
pytest --cov=convertapi --cov-report=html

# Run specific test file
pytest tests/test_convertapi.py

# Run specific test
pytest tests/test_convertapi.py::TestConvertapi::test_convert_file
```

### Test Structure

```python
import pytest
from convertapi import ApiError

def test_feature_success():
    """Test successful feature execution."""
    # Arrange
    ...
    # Act
    result = ...
    # Assert
    assert result is not None

def test_feature_handles_error():
    """Test that feature properly handles errors."""
    with pytest.raises(ApiError):
        # code that should raise ApiError
        ...
```

## Pull Request Process

1. **Create a feature branch:**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes:**
   - Write clear, descriptive commit messages
   - Follow the coding standards
   - Add tests for new functionality
   - Update documentation as needed

3. **Ensure all checks pass:**
   ```bash
   # Run linter
   ruff check convertapi
   
   # Run type checker
   mypy convertapi
   
   # Run tests
   pytest --cov=convertapi
   ```

4. **Update documentation:**
   - Update README.md if adding new features
   - Update CHANGELOG.md following [Keep a Changelog](https://keepachangelog.com/) format
   - Add docstrings to new functions/classes

5. **Push your changes:**
   ```bash
   git push origin feature/your-feature-name
   ```

6. **Create a Pull Request:**
   - Use a clear, descriptive title
   - Fill out the PR template completely
   - Reference any related issues
   - Request review from maintainers

7. **Address review feedback:**
   - Make requested changes promptly
   - Keep the discussion professional and constructive
   - Update your PR with new commits or amendments

## Reporting Bugs

Use the [Bug Report template](.github/ISSUE_TEMPLATE/bug_report.md) when reporting bugs. Include:

- Clear description of the bug
- Steps to reproduce
- Expected vs actual behavior
- Environment details (Python version, OS, etc.)
- Relevant code snippets or error messages

## Suggesting Enhancements

Use the [Feature Request template](.github/ISSUE_TEMPLATE/feature_request.md) when suggesting enhancements. Include:

- Clear description of the feature
- Use cases and benefits
- Possible implementation approach
- Examples of similar features in other libraries

## Questions?

If you have questions about contributing, feel free to:
- Open a [Discussion](https://github.com/Nietzsche-Ubermensch/convertapi-library-python/discussions)
- Ask in your pull request or issue

Thank you for contributing to ConvertAPI Python Client! 🎉
