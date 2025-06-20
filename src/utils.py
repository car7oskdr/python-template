"""
Utility functions for the application.
"""

import json
import os
from typing import Any, Dict, List


def read_config(config_path: str) -> Dict[str, Any]:
    """Read configuration from a JSON file.

    Args:
        config_path: Path to the configuration file

    Returns:
        Configuration dictionary

    Raises:
        FileNotFoundError: If config file doesn't exist
        json.JSONDecodeError: If config file is invalid JSON
    """
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Configuration file not found: {config_path}")

    with open(config_path, "r", encoding="utf-8") as f:
        return json.load(f)  # type: ignore


def save_config(config: Dict[str, Any], config_path: str) -> None:
    """Save configuration to a JSON file.

    Args:
        config: Configuration dictionary to save
        config_path: Path where to save the configuration
    """
    with open(config_path, "w", encoding="utf-8") as f:
        json.dump(config, f, indent=2, ensure_ascii=False)


def validate_input(data: Any, expected_type: type) -> bool:
    """Validate input data type.

    Args:
        data: Data to validate
        expected_type: Expected type

    Returns:
        True if data is of expected type, False otherwise
    """
    return isinstance(data, expected_type)


def format_list(items: List[str], separator: str = ", ") -> str:
    """Format a list of items into a string.

    Args:
        items: List of items to format
        separator: Separator to use between items

    Returns:
        Formatted string
    """
    return separator.join(items)
