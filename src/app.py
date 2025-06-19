"""
Main application module.
"""

import logging
from typing import Optional


class App:
    """Main application class."""
    
    def __init__(self, name: str = "Python App"):
        """Initialize the application.
        
        Args:
            name: Application name
        """
        self.name = name
        self.logger = self._setup_logging()
        
    def _setup_logging(self) -> logging.Logger:
        """Setup logging configuration.
        
        Returns:
            Configured logger instance
        """
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        return logging.getLogger(self.name)
    
    def run(self) -> None:
        """Run the application."""
        self.logger.info(f"Starting {self.name}")
        print(f"Welcome to {self.name}!")
        self.logger.info(f"{self.name} finished successfully")
    
    def get_name(self) -> str:
        """Get the application name.
        
        Returns:
            Application name
        """
        return self.name 