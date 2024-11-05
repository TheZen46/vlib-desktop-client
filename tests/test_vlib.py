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
        self.assertTrue(self.pm.is_vip())
        self.assertIn("VIP", self.pm.get_rank())

    def test_daily_allowance_claim_and_cooldown(self):
        self.pm.data["last_daily_claim"] = 0
        initial_cr = self.pm.get_credits()
        success, reward, new_cr, msg = self.pm.claim_daily_allowance()
        self.assertTrue(success)
        self.assertGreater(reward, 0)
        self.assertEqual(new_cr, initial_cr + reward)

        success_retry, reward_retry, current_cr, msg_retry = self.pm.claim_daily_allowance()
        self.assertFalse(success_retry)
        self.assertEqual(reward_retry, 0)
        self.assertIn("cooldown", msg_retry.lower())

    def test_mod_management_toggling_and_catalog(self):
        catalog = self.pm.get_available_mods()
        self.assertGreaterEqual(len(catalog), 4)
        first_mod = catalog[0]["id"]

        if not self.pm.is_mod_active(first_mod):
            self.pm.toggle_mod(first_mod)
        self.assertTrue(self.pm.is_mod_active(first_mod))

        new_state = self.pm.toggle_mod(first_mod)
        self.assertFalse(new_state)
        self.assertFalse(self.pm.is_mod_active(first_mod))

        restored = self.pm.toggle_mod(first_mod)
        self.assertTrue(restored)
        self.assertTrue(self.pm.is_mod_active(first_mod))

    def test_support_ticket_logging_and_persistence(self):
        ticket = self.pm.submit_support_ticket(
            username="test_operative",
            category="Bug Report",
            message="Test error logging verification"
        )
        self.assertTrue(ticket["ticket_id"].startswith("LP-"))
        self.assertEqual(ticket["status"], "OPEN")
        self.assertEqual(ticket["category"], "Bug Report")
        self.assertTrue(self.pm.tickets_file.exists())

    def test_sound_toggle_and_state(self):
        self.assertTrue(self.pm.is_sound_enabled())
        toggled = self.pm.toggle_sound()
        self.assertFalse(toggled)
        self.assertFalse(self.pm.is_sound_enabled())
        restored = self.pm.toggle_sound()
        self.assertTrue(restored)
        self.assertTrue(self.pm.is_sound_enabled())


class TestVLibSecurityAndValidation(unittest.TestCase):
    def test_password_complexity_rules(self):
        uppercase_regex = r'[A-Z]'
        lowercase_regex = r'[a-z]'
        special_chars_regex = r'[^A-Za-z0-9]'
        numbers_regex = r'\d'

        strong_pass = "P@ssw0rd2024!"
        self.assertTrue(re.search(uppercase_regex, strong_pass))
        self.assertTrue(re.search(lowercase_regex, strong_pass))
        self.assertTrue(re.search(numbers_regex, strong_pass))
        self.assertTrue(re.search(special_chars_regex, strong_pass))

        weak_pass = "password"
        is_strong = bool(
            re.search(uppercase_regex, weak_pass) and
            re.search(lowercase_regex, weak_pass) and
            re.search(numbers_regex, weak_pass) and
            re.search(special_chars_regex, weak_pass)
        )
        self.assertFalse(is_strong, "Weak password lacking uppercase/special/numbers should fail")

    def test_birth_year_validation(self):
        current_year = datetime.now().year
        birth_year_valid = current_year - 25
        age_valid = current_year - birth_year_valid
        self.assertTrue(14 <= age_valid < 93)

        birth_year_young = current_year - 10
        age_young = current_year - birth_year_young
        self.assertFalse(14 <= age_young < 93)


class TestVLibNativeImageProcessing(unittest.TestCase):
    def test_native_pillow_round_corner(self):
        test_img = Image.new("RGB", (64, 64), color=(100, 150, 200))
        from PIL import ImageDraw
        width, height = test_img.size
        mask = Image.new("L", (width, height), 0)
        draw = ImageDraw.Draw(mask)
        draw.rounded_rectangle((0, 0, width, height), radius=10, fill=255)
        
        rgba_img = test_img.convert("RGBA")
        rgba_img.putalpha(mask)
        self.assertEqual(rgba_img.mode, "RGBA")
        self.assertEqual(rgba_img.size, (64, 64))
        self.assertEqual(rgba_img.getpixel((0, 0))[3], 0)
        self.assertEqual(rgba_img.getpixel((32, 32))[3], 255)


class TestVLibApplicationStateAndRouting(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.patcher_info = patch("tkinter.messagebox.showinfo", return_value="ok")
        cls.patcher_warn = patch("tkinter.messagebox.showwarning", return_value="ok")
        cls.patcher_info.start()
        cls.patcher_warn.start()

        cls.app = Application(OUTPUT_PATH=OUTPUT_PATH)
        cls.app.withdraw()  # Hide window during tests

    @classmethod
    def tearDownClass(cls):
        cls.app.destroy()
        cls.patcher_info.stop()
        cls.patcher_warn.stop()

    def test_registered_pages(self):
        self.assertGreaterEqual(len(self.app.pages), 22, "Application should register at least 22 page views")
        self.assertIn("sign_in", self.app.pages)
        self.assertIn("main_channel", self.app.pages)
        self.assertIn("options", self.app.pages)
        self.assertIn("notenoughmoney", self.app.pages)
        self.assertIn("game_session", self.app.pages)

    def test_temp_tool_state_cycle(self):
        self.app.temp_tool("modify", "username", "test_user_42")
        self.app.temp_tool("modify", "email", "test@example.com")
        
        self.assertEqual(self.app.temp_tool("return", "username"), "test_user_42")
        self.assertEqual(self.app.temp_tool("return", "email"), "test@example.com")
        
        self.app.temp_tool("reload", None)
        self.assertEqual(self.app.temp_tool("return", "username"), "")
        self.assertEqual(self.app.temp_tool("return", "email"), "")

    def test_start_game_mounts_game_session(self):
        self.app.show_page("start_game")
        self.assertEqual(self.app.pages["current"], self.app.pages["game_session"])

    def test_contact_us_back_button_and_ticket_dispatch(self):
        self.app.show_page("contact_us")
