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
        elif username.lower() == "poldo":
            self.data["rank"] = "VIP #0012"
            self.data["is_vip"] = True
        elif username.lower() == "scandaloah":
            self.data["rank"] = "PRO #0077"
        else:
            self.data["rank"] = f"MEMBER #{abs(hash(username)) % 1000:04d}"
        self.save_profile()

    def get_username(self) -> str:
        return self.data.get("username", "Guest")

    def get_credits(self) -> int:
        return int(self.data.get("credits", 0))

    def get_formatted_credits(self) -> str:
        return f"{self.get_credits():,} CR"

    def get_rank(self) -> str:
        return str(self.data.get("rank", "MEMBER #0001"))

    def is_vip(self) -> bool:
        return bool(self.data.get("is_vip", False))

    def set_vip(self, active: bool = True):
        self.data["is_vip"] = active
        if active and "VIP" not in self.data.get("rank", ""):
            self.data["rank"] = f"VIP {self.data.get('rank', '#0001')}"
        self.save_profile()

    def add_credits(self, amount: int) -> int:
        if amount > 0:
            self.data["credits"] = self.get_credits() + amount
            self.save_profile()
            print(f"[Profile Manager] Added {amount} CR. New balance: {self.get_formatted_credits()}")
        return self.get_credits()

    def spend_credits(self, amount: int) -> bool:
        if 0 < amount <= self.get_credits():
            self.data["credits"] = self.get_credits() - amount
            self.save_profile()
            print(f"[Profile Manager] Spent {amount} CR. New balance: {self.get_formatted_credits()}")
            return True
        return False

    def claim_daily_allowance(self) -> tuple:
        """
        Awards a daily credit dividend (+250 CR base, +500 CR for VIPs).
        Returns: (success: bool, reward: int, balance: int, message: str)
        """
        now = time.time()
        last_claim = float(self.data.get("last_daily_claim", 0))
        cooldown = 86400  # 24 hours

        if now - last_claim < cooldown:
            remaining = int(cooldown - (now - last_claim))
            hours = remaining // 3600
            minutes = (remaining % 3600) // 60
            msg = f"Dividend on cooldown. Check back in {hours}h {minutes}m."
            return (False, 0, self.get_credits(), msg)

        reward = 500 if self.is_vip() else 250
        self.data["last_daily_claim"] = now
        self.add_credits(reward)
        vip_tag = " (VIP 2x Bonus!)" if self.is_vip() else ""
        msg = f"Daily Syndicate Dividend Claimed! +{reward} CR{vip_tag}"
        return (True, reward, self.get_credits(), msg)

    def get_available_mods(self) -> list:
        return AVAILABLE_MODS

    def is_mod_active(self, mod_id: str) -> bool:
        return mod_id in self.data.get("active_mods", [])

    def toggle_mod(self, mod_id: str) -> bool:
        active = self.data.setdefault("active_mods", [])
        if mod_id in active:
            active.remove(mod_id)
            status = False
        else:
            active.append(mod_id)
            status = True
        self.save_profile()
        return status

    def get_active_mods(self) -> list:
        return list(self.data.get("active_mods", []))

    def is_sound_enabled(self) -> bool:
        return bool(self.data.get("sound_fx_enabled", True))

    def toggle_sound(self) -> bool:
        new_state = not self.is_sound_enabled()
        self.data["sound_fx_enabled"] = new_state
        self.save_profile()
        return new_state

    def submit_support_ticket(self, username: str, category: str, message: str) -> dict:
        ticket_id = f"LP-{int(time.time()) % 100000:05d}"
        ticket = {
            "ticket_id": ticket_id,
            "username": username or self.get_username(),
            "category": category,
            "message": message,
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            "status": "OPEN"
        }
