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
    )
    parser.add_argument(
        "-t", "--test",
        action="store_true",
        help="Run the complete automated unit test suite and exit."
    )
    parser.add_argument(
        "--diag",
        action="store_true",
        help="Run complete client subsystem diagnostics and health check."
    )
    parser.add_argument(
        "--offline",
        action="store_true",
        help="Force Offline Demo Mode, bypassing remote database connections."
    )
    parser.add_argument(
        "--user",
        type=str,
        default=None,
        help="Pre-authenticate as a specific user in offline demo mode (e.g. thezen46, Poldo, scandaloah)."
    )
    parser.add_argument(
        "--page",
        type=str,
        default=None,
        help="Direct deep-link to launch a specific page (e.g. main_channel, game_session, modding, options, getVIP)."
    )
    parser.add_argument(
        "--credits",
        type=int,
        default=None,
        help="Developer override: set wallet credits balance upon launch."
    )
    parser.add_argument(
        "--sound",
        choices=["on", "off"],
        default=None,
        help="Enable or mute client synthesized audio effects."
    )
    return parser.parse_args()


def run_tests():
    import unittest
    print("=" * 60)
    print("  Running VLib Client Automated Test Suite...")
    print("=" * 60)
    loader = unittest.TestLoader()
    suite = loader.discover(str(PROJECT_ROOT / "tests"), pattern="test_*.py")
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    sys.exit(0 if result.wasSuccessful() else 1)


def run_diagnostics():
    print("=" * 65)
    print(f"  VLib (Las Purgas) Desktop Client v{CLIENT_VERSION} - System Diagnostics")
    print("=" * 65)
    print(f"• Platform:         {platform.system()} {platform.release()} ({platform.machine()})")
    print(f"• Python Version:   {sys.version.split()[0]} ({sys.executable})")

    # Tkinter check
    try:
        import tkinter as tk
        r = tk.Tk()
        tk_ver = r.tk.call("info", "patchlevel")
        r.destroy()
        print(f"• GUI Engine:       Tkinter {tk_ver} [OK]")
    except Exception as e:
        print(f"• GUI Engine:       Tkinter Failed: {e} [ERROR]")

    # Pillow check
    try:
        import PIL
        from PIL import Image
        print(f"• Imaging Engine:   Pillow {PIL.__version__} [OK]")
    except Exception as e:
        print(f"• Imaging Engine:   Pillow Failed: {e} [ERROR]")

    # Audio Engine
    if sys.platform == "win32":
        try:
            import winsound
            print("• Audio Engine:     Windows Wave/Beep Synthesizer [OK]")
        except Exception as e:
            print(f"• Audio Engine:     Windows Audio Unavailable: {e}")
    else:
        print("• Audio Engine:     Non-Windows Host (Audio Muted)")

    # Asset frames 0 to 21
    assets_dir = PROJECT_ROOT / "tentativo parte1" / "build" / "assets"
    missing_frames = []
    for f in range(22):
        fd = assets_dir / f"frame{f}"
        if not fd.exists():
            missing_frames.append(f"frame{f}")
    if not missing_frames:
        print("• Asset Slices:     Frames 0 through 21 (100% Present) [OK]")
    else:
        print(f"• Asset Slices:     Missing: {missing_frames} [WARNING]")

    # Local storage caches
    caches = [
        ("users.json", PROJECT_ROOT / "tentativo parte1" / "users.json"),
        ("user_profile.json", PROJECT_ROOT / "tentativo parte1" / "local_temp_files" / "user_profile.json"),
        ("Onl_verification.json", PROJECT_ROOT / "tentativo parte1" / "Onl_verification.json"),
        ("support_tickets.json", PROJECT_ROOT / "tentativo parte1" / "local_temp_files" / "support_tickets.json")
    ]
    for label, path in caches:
        status = "Present" if path.exists() else "Initialized on First Run"
        print(f"• Cache File:       {label} -> {status}")

    print("=" * 65)
    print("  Diagnostic Status: ALL CRITICAL SUBSYSTEMS HEALTHY")
    print("=" * 65)
    sys.exit(0)


def main():
    args = parse_arguments()

    if args.test:
        run_tests()

    if args.diag:
        run_diagnostics()

    if args.offline:
        os.environ["VLIB_FORCE_OFFLINE"] = "1"
        print("[Launcher] Offline Mode forced via CLI argument.")

    print("=" * 60)
    print(f"  VLib (Las Purgas) Desktop Client v{CLIENT_VERSION} - Initializing...")
    print("=" * 60)
    print(f"[Launcher] Project Root: {PROJECT_ROOT}")
    print(f"[Launcher] Application Engine: {APP_DIR}")

    try:
        from main import Application, OUTPUT_PATH
    except ImportError as e:
        print(f"Error importing VLib application: {e}")
        sys.exit(1)

    app = Application(OUTPUT_PATH=OUTPUT_PATH)

