.PHONY: help install install-dev test lint format clean run sync

# Default target
help:
	@echo "Available commands:"
	@echo "  install     - Install production dependencies with uv"
	@echo "  install-dev - Install development dependencies with uv"
	@echo "  sync        - Sync dependencies from pyproject.toml"
	@echo "  test        - Run tests"
	@echo "  lint        - Run linting"
	@echo "  format      - Format code"
	@echo "  clean       - Clean build artifacts"
	@echo "  run         - Run the application"

# Install production dependencies
install:
	uv sync --no-dev

# Install development dependencies
install-dev:
	uv sync

# Sync dependencies from pyproject.toml
sync:
	uv sync

# Run tests
test:
	uv run pytest tests/ -v

# Run tests with coverage
test-cov:
	uv run pytest tests/ --cov=src --cov-report=html --cov-report=term

# Run linting
lint:
	uv run flake8 src/ tests/
	uv run mypy src/

# Format code
format:
	uv run black src/ tests/
	uv run isort src/ tests/

# Clean build artifacts
clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	rm -rf __pycache__/
	rm -rf src/__pycache__/
	rm -rf tests/__pycache__/
	rm -rf .pytest_cache/
	rm -rf .mypy_cache/
	rm -rf htmlcov/
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete

# Run the application
run:
	uv run python main.py

# Development setup
dev-setup: install-dev
	uv run pre-commit install

# Check code quality
check: lint test

# Full development cycle
dev: format lint test

# Add a new dependency
add:
	@read -p "Enter package name: " package; \
	uv add $$package

# Add a development dependency
add-dev:
	@read -p "Enter package name: " package; \
	uv add --dev $$package

# Remove a dependency
remove:
	@read -p "Enter package name: " package; \
	uv remove $$package

# Show dependency tree
tree:
	uv tree 