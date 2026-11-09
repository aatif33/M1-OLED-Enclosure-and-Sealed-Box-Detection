"""Create deterministic 70/20/10 image splits.

For video-derived datasets, split by source video/session/group first to prevent
near-identical adjacent frames leaking across splits. This simple script is for
independent images only; adapt grouping before use when images share a source.
"""
import argparse
import random
import shutil
from pathlib import Path

EXTS = {".jpg", ".jpeg", ".png", ".bmp"}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", required=True, help="Folder containing images")
    parser.add_argument("--output", required=True, help="Output dataset folder")
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()

    source = Path(args.source)
    output = Path(args.output)
    images = sorted(p for p in source.iterdir() if p.suffix.lower() in EXTS)
    if len(images) < 10:
        raise SystemExit("Use at least 10 images; preferably substantially more.")

    random.Random(args.seed).shuffle(images)
    n = len(images)
    n_train = int(n * 0.7)
    n_val = int(n * 0.2)
    groups = {
        "train": images[:n_train],
        "val": images[n_train:n_train+n_val],
        "test": images[n_train+n_val:],
    }
    for split, paths in groups.items():
        dest = output / "images" / split
        dest.mkdir(parents=True, exist_ok=True)
        for path in paths:
            shutil.copy2(path, dest / path.name)
        print(f"{split}: {len(paths)}")

    print(f"Total: {n} | seed: {args.seed}")
    print("WARNING: This script copies images only, not labels. Extend it to copy matching labels.")
    print("WARNING: Group related frames by capture session/video before splitting to avoid leakage.")

if __name__ == "__main__":
    main()
