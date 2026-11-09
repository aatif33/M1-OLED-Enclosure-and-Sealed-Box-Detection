"""Simple repeatable timing harness for a callable frame-processing function.

This starter measures a placeholder operation (frame copy). Replace `process_frame`
with the actual inference call before reporting detector benchmark results.
"""
import argparse
import statistics
import time
import cv2

def process_frame(frame):
    return frame.copy()  # Replace with actual preprocessing + model inference.

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--camera", type=int, default=0)
    parser.add_argument("--warmup", type=int, default=20)
    parser.add_argument("--runs", type=int, default=100)
    args = parser.parse_args()

    cap = cv2.VideoCapture(args.camera)
    if not cap.isOpened():
        raise SystemExit("Could not open camera.")
    ok, frame = cap.read()
    cap.release()
    if not ok:
        raise SystemExit("Could not read benchmark frame.")

    for _ in range(args.warmup):
        process_frame(frame)

    timings = []
    for _ in range(args.runs):
        start = time.perf_counter()
        process_frame(frame)
        timings.append((time.perf_counter() - start) * 1000)

    ordered = sorted(timings)
    p95_index = min(len(ordered) - 1, int(0.95 * len(ordered)))
    print(f"Runs: {len(timings)}")
    print(f"Median: {statistics.median(timings):.2f} ms")
    print(f"P95: {ordered[p95_index]:.2f} ms")
    print("NOTE: These are frame-copy timings until process_frame uses the real detector.")

if __name__ == "__main__":
    main()
