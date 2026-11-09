"""Capture and save one raw frame from the selected camera."""
import argparse
from datetime import datetime
from pathlib import Path
import cv2

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--camera", type=int, default=0, help="OpenCV camera index")
    parser.add_argument("--output", default="01_camera_and_repo/evidence")
    args = parser.parse_args()

    cap = cv2.VideoCapture(args.camera)
    if not cap.isOpened():
        raise SystemExit(f"Cannot open camera index {args.camera}")

    ok, frame = cap.read()
    cap.release()
    if not ok or frame is None:
        raise SystemExit("Camera opened, but frame capture failed.")

    out_dir = Path(args.output)
    out_dir.mkdir(parents=True, exist_ok=True)
    filename = f"first_frame_{datetime.now():%Y%m%d_%H%M%S}.jpg"
    output_path = out_dir / filename
    if not cv2.imwrite(str(output_path), frame):
        raise SystemExit("Could not write image.")
    print(f"Saved: {output_path}")
    print(f"Resolution: {frame.shape[1]}x{frame.shape[0]}")
    print(f"Image shape: {frame.shape}")

if __name__ == "__main__":
    main()
