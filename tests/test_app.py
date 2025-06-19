"""
Unit tests for the main application module.
"""

import unittest
from unittest.mock import patch
from src.app import App


class TestApp(unittest.TestCase):
    """Test cases for the App class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.app = App("Test App")
    
    def test_app_initialization(self):
        """Test app initialization."""
        self.assertEqual(self.app.name, "Test App")
        self.assertIsNotNone(self.app.logger)
    
    def test_get_name(self):
        """Test get_name method."""
        self.assertEqual(self.app.get_name(), "Test App")
    
    @patch('builtins.print')
    def test_run(self, mock_print):
        """Test run method."""
        self.app.run()
        mock_print.assert_called_once_with("Welcome to Test App!")
    
    def test_default_app_name(self):
        """Test default app name."""
        default_app = App()
        self.assertEqual(default_app.name, "Python App")


if __name__ == '__main__':
    unittest.main() 