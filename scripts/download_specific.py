#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Download a subset of the OmniWorld-Game dataset based on UIDs listed in a CSV
(or passed explicitly via CLI).

Examples
--------
Download rows 0 and 1 (0-based, header excluded):

    python download_specific.py \
        --csv omniworld_game_metadata.csv \
        --repo InternRobotics/OmniWorld \
        --local_dir ./OmniWorld_subset \
        --rows 0 1

Or specify the UIDs directly, bypassing the CSV:

    python download_specific.py \
        --uids 0b3caf48b79d 0c3cefcf3a15
"""

import argparse
import csv
import sys
from pathlib import Path
from typing import List

from huggingface_hub import snapshot_download, login


# ----------------------------------------------------------------------
def parse_args() -> argparse.Namespace:
    """CLI argument parser."""
    ap = argparse.ArgumentParser("Partial downloader for OmniWorld")
    ap.add_argument(
        "--csv",
        default="omniworld_game_metadata.csv",
        help="Path to the CSV file that contains UIDs",
    )
    ap.add_argument(
        "--repo",
        default="InternRobotics/OmniWorld",
        help="HF dataset repository ID",
    )
    ap.add_argument(
        "--local_dir",
        required=True,
        help="Destination directory for the downloaded files",
    )
    ap.add_argument(
        "--rows",
        nargs="+",
        type=int,
        help="Row numbers to download (0-based, header excluded)",
    )
    ap.add_argument(
        "--uids",
        nargs="+",
        help="Explicit list of UIDs; overrides --rows if provided",
    )
    ap.add_argument(
        "--token",
        help="HF access token, only required for private repos",
    )
    return ap.parse_args()


# ----------------------------------------------------------------------
def read_uids_from_csv(csv_path: Path, row_ids: List[int]) -> List[str]:
    """Extract the UID column (first column) for the requested row indices."""
    wanted = set(row_ids)
    uids: List[str] = []
    with csv_path.open(newline="") as f:
        reader = csv.reader(f)
        next(reader)  # skip header
        for idx, row in enumerate(reader):
            if idx in wanted:
                uids.append(row[0].strip())
                wanted.remove(idx)
            if not wanted:  # exit early when all rows found
                break
    if wanted:
        missing = ", ".join(map(str, sorted(wanted)))
        sys.exit(f"❌ Missing rows in CSV: {missing}")
    return uids


# ----------------------------------------------------------------------
def main() -> None:
    args = parse_args()

    # Determine which UIDs to download
    if args.uids:
        uids = [u.strip() for u in args.uids]
    elif args.rows:
        csv_path = Path(args.csv).expanduser()
        if not csv_path.is_file():
            sys.exit(f"❌ CSV not found: {csv_path}")
        uids = read_uids_from_csv(csv_path, args.rows)
    else:
        sys.exit("Please specify scenes to download using --rows or --uids")

    print("UIDs to be downloaded:", ", ".join(uids))

    # Authenticate if a token is supplied (needed for private repos)
    if args.token:
        login(args.token)

    # Build allow_patterns used by snapshot_download
    allow_patterns: List[str] = []
    for uid in uids:
        allow_patterns += [
            f"videos/OmniWorld-Game/{uid}/**",
            f"annotations/OmniWorld-Game/{uid}/**",
        ]

    # Download
    local_dir = Path(args.local_dir).expanduser()
    print(f"📥 Downloading to: {local_dir.resolve()}")
    snapshot_download(
        repo_id=args.repo,
        repo_type="dataset",
        local_dir=local_dir,
        allow_patterns=allow_patterns,
        local_dir_use_symlinks=False,  # copy files directly instead of symlinking
        tqdm_class=None,  # remove this line to enable the progress bar
    )
    print("✅ Download complete")


# ----------------------------------------------------------------------
if __name__ == "__main__":
    main()