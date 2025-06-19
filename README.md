# Python Application Template

A basic Python application template with a clean, organized structure following best practices, using **uv** for fast dependency management.

## Features

- Clean project structure
- Modular design with separate source and test directories
- Comprehensive test suite
- Configuration management utilities
- Logging setup
- Type hints throughout
- Development tools configuration
- **Fast dependency management with uv**
- Modern Python packaging with pyproject.toml

## Project Structure

```
python-app/
├── main.py              # Application entry point
├── pyproject.toml       # Project configuration and dependencies
├── uv.lock              # Lock file for reproducible builds
├── src/                 # Source code
│   ├── __init__.py
│   ├── app.py          # Main application class
│   └── utils.py        # Utility functions
├── tests/              # Test files
│   ├── __init__.py
│   ├── test_app.py     # Tests for main app
│   └── test_utils.py   # Tests for utilities
├── docs/               # Documentation (create as needed)
├── Makefile            # Development commands
├── README.md          # This file
└── .gitignore         # Git ignore rules
```

## Prerequisites

Install **uv** (fast Python package manager):
```bash
# On macOS and Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# On Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# Or with pip
pip install uv
```

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd python-app
```

2. Install dependencies with uv:
```bash
# Install all dependencies (including dev dependencies)
uv sync

# Or install only production dependencies
uv sync --no-dev
```

3. Activate the virtual environment (optional, uv manages this automatically):
```bash
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

## Usage

### Running the Application

```bash
# Using uv run (recommended)
uv run python main.py

# Or using the Makefile
make run

# Or using the installed command
uv run python-app
```

### Running Tests

```bash
# Run all tests
uv run pytest

# Run with coverage
uv run pytest --cov=src

# Run specific test file
uv run pytest tests/test_app.py

# Or using the Makefile
make test
make test-cov
```

### Development Tools

```bash
# Code formatting
uv run black src/ tests/

# Import sorting
uv run isort src/ tests/

# Linting
uv run flake8 src/ tests/

# Type checking
uv run mypy src/

# Or using the Makefile
make format
make lint
```

### Managing Dependencies

```bash
# Add a new dependency
uv add package-name

# Add a development dependency
uv add --dev package-name

# Remove a dependency
uv remove package-name

# Show dependency tree
uv tree

# Sync dependencies from pyproject.toml
uv sync
```

## Configuration

The application includes utility functions for configuration management:

```python
from src.utils import read_config, save_config

# Read configuration
config = read_config('config.json')

# Save configuration
save_config({'key': 'value'}, 'config.json')
```

## Development Workflow

### Using Makefile Commands

```bash
# Install development dependencies
make install-dev

# Run full development cycle (format + lint + test)
make dev

# Check code quality
make check

# Clean build artifacts
make clean
```

### Adding New Features

1. Create new modules in the `src/` directory
2. Add corresponding tests in the `tests/` directory
3. Add dependencies to `pyproject.toml` if needed:
   ```bash
   uv add package-name
   ```
4. Update documentation as needed

## Why uv?

- **Speed**: Up to 10-100x faster than pip
- **Reliability**: Deterministic dependency resolution
- **Modern**: Uses the latest Python packaging standards
- **Simple**: Single tool for dependency management, virtual environments, and running commands
- **Compatible**: Works with existing Python projects and tools

## Testing

The project includes a comprehensive test suite using `pytest`. Tests are located in the `tests/` directory and follow the naming convention `test_*.py`.

## Code Style

This project follows PEP 8 style guidelines and uses:
- Black for code formatting
- isort for import sorting
- Flake8 for linting
- MyPy for type checking

All tools are configured in `pyproject.toml` for consistency.

## Troubleshooting

### Common Issues

1. **uv not found**: Install uv using the instructions above
2. **Import errors**: Make sure you're running from the project root directory
3. **Test failures**: Ensure all dependencies are installed with `uv sync`
4. **Type checking errors**: Run `uv run mypy src/` to see detailed type issues

### Migration from pip

If you're migrating from a pip-based project:
1. Replace `requirements.txt` with `pyproject.toml`
2. Use `uv add` instead of `pip install`
3. Use `uv run` instead of `python -m` for running tools
4. Update your CI/CD pipelines to use uv

## Support

For questions or issues, please open an issue on the project repository. 