# M1 — OLED Enclosure + Sealed Box Detection

Milestone: **M1 — Detect**

This repository collects the six M1 assessment workstreams:
1. Camera and repository
2. OpenCV pipeline
3. Baseline speed
4. Dataset v1
5. Correct dataset split
6. Train and run detector

## Project scope
- OLED enclosure camera setup and visual inspection evidence.
- Sealed/opened box detection dataset and detector work.
- Keep evidence for each workstream in its corresponding folder.

> Important: replace placeholders with measurements and outputs captured on your own device. Do not report estimated or example values as measured results.

## Quick start
```bash
python -m venv .venv
# Linux / Raspberry Pi:
source .venv/bin/activate
# Windows PowerShell:
# .venv\Scripts\Activate.ps1

pip install -r requirements.txt
python 01_camera_and_repo/camera_test.py
python 01_camera_and_repo/capture_frame.py
```

## Evidence checklist
- [ ] Camera model/specification and physical setup recorded
- [ ] First raw frame captured on target device
- [ ] Live OpenCV pipeline demonstrated
- [ ] Baseline FPS, latency, CPU, accelerator (if available), and temperature measured
- [ ] Dataset v1 labelled and data card completed
- [ ] 70/20/10 split verified with no leakage
- [ ] Detector metrics, confusion matrix, and 10 error examples documented

## Reproducibility
Record device model, OS, Python/OpenCV versions, camera index, image dimensions, model weights, commands, and date for every run.
