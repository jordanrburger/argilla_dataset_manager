"""
Argilla Dataset Manager
======================

A Python package for managing and uploading datasets to Argilla.
"""

from .datasets.settings_manager import DatasetTemplate, SettingsManager
from .utils.argilla_client import get_argilla_client
from .utils.dataset_manager import DatasetManager

__version__ = "0.1.7"
__all__ = ["DatasetManager", "DatasetTemplate", "SettingsManager", "get_argilla_client"]
