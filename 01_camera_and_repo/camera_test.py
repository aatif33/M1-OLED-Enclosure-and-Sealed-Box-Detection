"""Check available camera devices and display a live preview."""
import cv2
import platform
import sys

def main():
    print("Platform:", platform.platform())
    print("Python:", sys.version.split()[0])
    print("OpenCV:", cv2.__version__)

    cap = None
    selected = None
    for index in range(5):
        candidate = cv2.VideoCapture(index)
        if candidate.isOpened():
            ok, frame = candidate.read()
            if ok and frame is not None:
                cap, selected = candidate, index
                print(f"Camera index {index}: OK | frame={frame.shape[1]}x{frame.shape[0]}")
                break
        candidate.release()

    if cap is None:
        raise SystemExit("No working camera found. Check connection, permissions, and camera index.")

    print("Press q to quit the preview.")
    while True:
        ok, frame = cap.read()
        if not ok:
            print("Frame read failed.")
            break
        cv2.imshow("M1 - OLED Enclosure Camera Test", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()
    print(f"Camera test completed using index {selected}.")

if __name__ == "__main__":
    main()
