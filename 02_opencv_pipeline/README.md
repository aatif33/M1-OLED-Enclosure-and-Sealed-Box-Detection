# OpenCV pipeline

`main.py` currently proves camera streaming and a live telemetry overlay. It does **not** perform object detection yet.

Integrate the actual trained enclosure detector and sealed/opened-box detector here when their model weights and class mapping are confirmed. Keep the raw camera preview and detector output as separate evidence where possible.

Run:
```bash
python 02_opencv_pipeline/main.py --camera 0
```
