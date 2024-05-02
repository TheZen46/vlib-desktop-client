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
