"""
VLib CLI and Runner Integration Tests
Validates command-line interface flags, argument parsing, headless execution, and system diagnostics.
"""

import sys
import unittest
import subprocess
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

import run_client


class TestVLibCommandLineInterface(unittest.TestCase):
    def test_cli_version_flag_execution(self):
        cmd = [sys.executable, str(PROJECT_ROOT / "run_client.py"), "--version"]
