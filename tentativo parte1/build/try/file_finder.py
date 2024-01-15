"""
VLib Universal Frame Asset Resolver
Dynamically locates frame assets across all environments and development paths.
"""

from pathlib import Path
from typing import Optional


def find_frame_assets(frame_name: str) -> Optional[Path]:
    """
    Locates the asset directory for a given frame name (e.g., 'frame0', 'frame12').
    Intelligently traverses directory hierarchies to support both modular builds
    and root executions.
    """
    current_dir = Path(__file__).resolve().parent
    candidate_paths = [
        current_dir.parent / "assets" / frame_name,               # build/assets/frameX (from try/)
        current_dir.parent.parent / "build" / "assets" / frame_name, # from root or sub-module
        current_dir / "assets" / frame_name                      # local assets/frameX
    ]
    for p in candidate_paths:
        if p.exists() and p.is_dir():
            return p
    return None


def relative_to_frame(frame_name: str, asset_filename: str) -> Optional[Path]:
    """
    Returns the resolved Path for a specific asset inside a frame folder.
    """
    frame_dir = find_frame_assets(frame_name)
    if frame_dir:
        asset_path = frame_dir / asset_filename
        if asset_path.exists():
            return asset_path
    return None


if __name__ == "__main__":
    test_frame = "frame0"
    resolved = find_frame_assets(test_frame)
    if resolved:
        print(f"[file_finder] Successfully resolved '{test_frame}' to: {resolved}")
    else:
        print(f"[file_finder] Frame '{test_frame}' not found.")
