"""
Unit tests for the utilities module.
"""

import os
import tempfile
import unittest

from src.utils import format_list, read_config, save_config, validate_input


class TestUtils(unittest.TestCase):
    """Test cases for utility functions."""

    def setUp(self):
        """Set up test fixtures."""
        self.test_config = {
            "app_name": "Test App",
            "version": "1.0.0",
            "debug": True,
        }

    def test_save_and_read_config(self):
        """Test saving and reading configuration."""
        with tempfile.NamedTemporaryFile(
            mode="w",
            suffix=".json",
            delete=False,
        ) as f:
            config_path = f.name

        try:
            # Test saving config
            save_config(self.test_config, config_path)
            self.assertTrue(os.path.exists(config_path))

            # Test reading config
            loaded_config = read_config(config_path)
            self.assertEqual(loaded_config, self.test_config)
        finally:
            os.unlink(config_path)

    def test_read_config_file_not_found(self):
        """Test reading non-existent config file."""
        with self.assertRaises(FileNotFoundError):
            read_config("non_existent_file.json")

    def test_validate_input(self):
        """Test input validation."""
        self.assertTrue(validate_input("test", str))
        self.assertTrue(validate_input(123, int))
        self.assertTrue(validate_input([1, 2, 3], list))
        self.assertFalse(validate_input("test", int))
        self.assertFalse(validate_input(123, str))

    def test_format_list(self):
        """Test list formatting."""
        items = ["apple", "banana", "orange"]
        self.assertEqual(format_list(items), "apple, banana, orange")
        self.assertEqual(format_list(items, " | "), "apple | banana | orange")
        self.assertEqual(format_list([]), "")


if __name__ == "__main__":
    unittest.main()
