"""Minimal live OpenCV camera pipeline for M1 evidence."""
import argparse
import time
import cv2

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--camera", type=int, default=0)
    args = parser.parse_args()

    cap = cv2.VideoCapture(args.camera)
    if not cap.isOpened():
        raise SystemExit(f"Cannot open camera index {args.camera}")

    previous = time.perf_counter()
    fps_ema = 0.0
    print("Press q to quit.")
    while True:
        ok, frame = cap.read()
        if not ok:
            print("Frame read failed; stopping safely.")
            break

        now = time.perf_counter()
        latency_ms = (now - previous) * 1000.0
        previous = now
        instantaneous_fps = 1000.0 / latency_ms if latency_ms > 0 else 0.0
        fps_ema = instantaneous_fps if fps_ema == 0 else 0.9 * fps_ema + 0.1 * instantaneous_fps

        cv2.putText(frame, f"FPS: {fps_ema:.1f}", (15, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        cv2.putText(frame, f"Frame interval: {latency_ms:.1f} ms", (15, 60),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
        cv2.imshow("M1 - OLED Enclosure OpenCV Pipeline", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
