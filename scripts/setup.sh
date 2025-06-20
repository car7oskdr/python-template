#!/bin/bash

# Setup script for Python application with uv

set -e

echo "🚀 Setting up Python application with uv..."

# Check if uv is installed
if ! command -v uv &> /dev/null; then
    echo "❌ uv is not installed. Please install it first:"
    echo "   curl -LsSf https://astral.sh/uv/install.sh | sh"
    exit 1
fi

echo "✅ uv is installed"

# Install dependencies
echo "📦 Installing dependencies..."
uv sync

# Run initial tests
echo "🧪 Running initial tests..."
uv run pytest tests/ -v

echo "✅ Setup complete!"
echo ""
echo "🎉 Your Python application is ready!"
echo ""
echo "Next steps:"
echo "  • Run the application: make run"
echo "  • Run tests: make test"
echo "  • Format code: make format"
echo "  • Check code quality: make check"
echo ""
echo "Happy coding! 🐍" 