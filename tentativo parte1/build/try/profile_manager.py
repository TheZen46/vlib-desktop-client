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
