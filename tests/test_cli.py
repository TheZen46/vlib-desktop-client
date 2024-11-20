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
        res = subprocess.run(cmd, capture_output=True, text=True)
        self.assertEqual(res.returncode, 0)
        self.assertIn("VLib Client", res.stdout)
        self.assertIn("1.0.0", res.stdout)

    def test_cli_diagnostics_flag_execution(self):
        cmd = [sys.executable, str(PROJECT_ROOT / "run_client.py"), "--diag"]
        res = subprocess.run(cmd, capture_output=True, text=True)
        self.assertEqual(res.returncode, 0)
        self.assertIn("System Diagnostics", res.stdout)
        self.assertIn("Tkinter", res.stdout)
