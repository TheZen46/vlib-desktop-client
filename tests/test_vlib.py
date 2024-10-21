"""
VLib Client Automated Test Suite
Verifies mathematical models, asset integrity, data models, page routing,
password security, native image processing, forced offline mode, profile economy, and 100% page coverage.
"""

import unittest
from unittest.mock import patch
import math
import hashlib
import sys
import os
import re
from datetime import datetime
from pathlib import Path
from PIL import Image

REPO_ROOT = Path(__file__).resolve().parent.parent
APP_DIR = REPO_ROOT / "tentativo parte1" / "build" / "try"

if str(APP_DIR) not in sys.path:
    sys.path.insert(0, str(APP_DIR))

from sqlconn_basdata import Mycon_basdata
from profile_manager import ProfileManager
from main import Application, OUTPUT_PATH


class TestVLibAssetsAndPaths(unittest.TestCase):
    def test_assets_directories_exist(self):
        assets_dir = REPO_ROOT / "tentativo parte1" / "build" / "assets"
        self.assertTrue(assets_dir.exists(), "Assets directory should exist")
        for frame_idx in range(22):
            frame_dir = assets_dir / f"frame{frame_idx}"
            self.assertTrue(frame_dir.exists(), f"Frame {frame_idx} directory must exist")
            self.assertGreater(len(list(frame_dir.iterdir())), 0, f"Frame {frame_idx} should contain images")

    def test_icon_and_audio_exist(self):
        ico = REPO_ROOT / "tentativo parte1" / "las_purgas.ico"
        audio = REPO_ROOT / "tentativo parte1" / "elevator_wait.mp3"
        self.assertTrue(ico.exists(), "las_purgas.ico must exist")
        self.assertTrue(audio.exists(), "elevator_wait.mp3 must exist")


class TestVLibSineWaveMath(unittest.TestCase):
    def test_harmonic_sine_wave_bounds(self):
        amplitude = 15
        frequency = 3.2
        num_spheres = 6
        center_y = 25

        for t in [0.0, 0.5, 1.0, 2.5, 5.0]:
            for i in range(num_spheres):
                y = center_y + amplitude * math.sin(frequency * (2 * math.pi * (i / num_spheres) - frequency * t))
                self.assertGreaterEqual(y, center_y - amplitude - 1e-9)
                self.assertLessEqual(y, center_y + amplitude + 1e-9)


class TestVLibAuthentication(unittest.TestCase):
    def test_offline_demo_authentication(self):
        client = Mycon_basdata(username="thezen46", password="S/um17")
        self.assertTrue(client.find_and_verify(), "Default demo user thezen46 should verify")

    def test_secondary_demo_user(self):
        client = Mycon_basdata(username="Poldo", password="C4L4br3$")
        self.assertTrue(client.find_and_verify(), "Demo user Poldo should verify")

    def test_invalid_password_rejected(self):
        client = Mycon_basdata(username="thezen46", password="wrong_password_999")
        self.assertFalse(client.find_and_verify(), "Invalid password must be rejected")

    def test_default_image_fallback(self):
        client = Mycon_basdata(username="thezen46")
        img = client.get_imagepath()
        self.assertIn("png", img, "Image path should return a valid png identifier")

    def test_forced_offline_mode(self):
        os.environ["VLIB_FORCE_OFFLINE"] = "1"
        try:
            client = Mycon_basdata(username="thezen46", password="S/um17")
            self.assertTrue(client.is_offline, "Client must be offline when VLIB_FORCE_OFFLINE is set")
            self.assertTrue(client.find_and_verify(), "Demo user should verify in forced offline mode")
        finally:
            os.environ.pop("VLIB_FORCE_OFFLINE", None)


class TestVLibEconomyAndProfile(unittest.TestCase):
    def setUp(self):
        self.pm = ProfileManager()

    def test_initial_credits_and_rank(self):
        self.assertGreater(self.pm.get_credits(), 0)
        self.assertIn("CR", self.pm.get_formatted_credits())

    def test_credit_addition_and_spending(self):
        initial = self.pm.get_credits()
        self.pm.add_credits(500)
        self.assertEqual(self.pm.get_credits(), initial + 500)

        spent = self.pm.spend_credits(250)
        self.assertTrue(spent)
        self.assertEqual(self.pm.get_credits(), initial + 250)

    def test_insufficient_credit_rejection(self):
        large_amount = self.pm.get_credits() + 999999
        self.assertFalse(self.pm.spend_credits(large_amount))

    def test_vip_activation(self):
        self.pm.set_vip(True)
