"""
VLib (Las Purgas) User Profile & Virtual Economy Engine
Manages persistent user profile state, virtual credits, VIP tiers, mod ecosystem, and support tickets.
"""

from pathlib import Path
import json
import time

AVAILABLE_MODS = [
    {
        "id": "neon_reshade",
        "name": "Cyberpunk Re-Shade Neon FX",
        "version": "v2.4",
        "desc": "Post-processing shader pack with holographic bloom and scanlines.",
        "category": "Graphics"
    },
    {
        "id": "night_radio",
        "name": "Las Purgas Radio Extended",
        "version": "v1.8",
        "desc": "12 new dark-synth and vaporwave audio streams for the deck.",
        "category": "Audio"
    },
    {
        "id": "holo_dice",
        "name": "High-Roller Hologram Dice",
        "version": "v3.0",
        "desc": "3D particle emitter and cyber glow animations for dice rolls.",
        "category": "Visuals"
    },
    {
        "id": "neural_hack",
        "name": "Neural Net Fast-Hack Tools",
        "version": "v1.2",
        "desc": "Visual exploit matrix and terminal speed-assist for hacking.",
        "category": "Tools"
    }
]


class ProfileManager:
    def __init__(self, controller=None):
        self.controller = controller
        self.profile_dir = Path(__file__).resolve().parent.parent.parent / "local_temp_files"
        self.profile_dir.mkdir(parents=True, exist_ok=True)
        self.profile_file = self.profile_dir / "user_profile.json"
        self.tickets_file = self.profile_dir / "support_tickets.json"

        self.default_data = {
            "username": "thezen46",
            "credits": 2500,
            "rank": "LVL 5",
            "member_id": "#0046",
            "is_vip": False,
            "active_language": "ENG",
            "active_mods": ["neon_reshade", "night_radio"],
            "installed_mods": [
                "Cyberpunk Night City HUD v2.1",
                "Enhanced Shader Pack (Neon Edition)"
            ],
            "last_daily_claim": 0,
            "sound_fx_enabled": True
        }
        self.data = self.load_profile()

    def load_profile(self) -> dict:
        if self.profile_file.exists():
            try:
                with open(self.profile_file, "r", encoding="utf-8") as f:
                    saved = json.load(f)
                    merged = dict(self.default_data)
                    merged.update(saved)
                    if "active_mods" not in merged:
                        merged["active_mods"] = list(self.default_data["active_mods"])
                    return merged
            except Exception as e:
                print(f"[Profile Manager] Notice loading profile: {e}")
        return dict(self.default_data)

    def save_profile(self):
        try:
            with open(self.profile_file, "w", encoding="utf-8") as f:
                json.dump(self.data, f, indent=4)
        except Exception as e:
            print(f"[Profile Manager] Failed saving profile: {e}")

    def set_user(self, username: str):
        if not username:
            return
        self.data["username"] = username
        if username.lower() == "thezen46":
            self.data["rank"] = "ADMIN #0046"
            self.data["is_vip"] = True
