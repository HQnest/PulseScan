"""
PulseScan - A modular toolkit for system visibility, network diagnostics, and workflow automation.

This package provides safe, ethical tools for system analysis and monitoring.
"""

__version__ = "0.1.0"

from . import diagnostics
from . import visibility
from . import automation
from . import web

__all__ = ["diagnostics", "visibility", "automation", "web"]