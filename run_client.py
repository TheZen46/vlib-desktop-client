#!/usr/bin/env python3
"""
VLib (Las Purgas) Desktop Client Launcher
Unified entry point to run the VLib application, execute test suites, perform system diagnostics,
deep-link to specific views, or force offline mode.
"""

import sys
import os
import argparse
import platform
from pathlib import Path

# Add core application package directory to sys.path
PROJECT_ROOT = Path(__file__).resolve().parent
APP_DIR = PROJECT_ROOT / "tentativo parte1" / "build" / "try"

if str(APP_DIR) not in sys.path:
    sys.path.insert(0, str(APP_DIR))

# Ensure required runtime directories exist
local_cache = PROJECT_ROOT / "tentativo parte1" / "local_temp_files"
local_cache.mkdir(parents=True, exist_ok=True)

CLIENT_VERSION = "1.0.0"


def parse_arguments():
    parser = argparse.ArgumentParser(
        prog="vlib",
        description="VLib (Las Purgas) Desktop Community Client & Modding Launcher"
    )
    parser.add_argument(
        "-v", "--version",
        action="version",
        version=f"VLib Client v{CLIENT_VERSION} (Las Purgas)"
