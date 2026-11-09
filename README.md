# M1 — OLED Enclosure + Sealed Box Detection

**Milestone:** M1 — Detect  
**Package type:** Planning/demo assets and evidence organization starter.

This repository is organized around the six M1 assessment criteria. The included annotated screenshots are references supplied for this project. Other generated visuals are clearly marked as concepts/templates, not measurements or completed experiments.

## M1 criteria
1. `01_camera_and_repo/` — camera setup, specification, first frame, repository history.
2. `02_opencv_pipeline/` — live OpenCV pipeline and detection overlay.
3. `03_baseline_speed/` — measured FPS, latency, CPU/accelerator utilization and temperature.
4. `04_dataset_v1/` — labelled dataset and data card.
5. `05_correct_split/` — 70/20/10 split and leakage checks.
6. `06_train_and_run_detector/` — model training, mAP@0.5, precision, recall, confusion matrix and error review.

## Important evidence status
- Supplied screenshots are reference screenshots, not newly captured by this package.
- Dashboard and dataset/validation visuals in `demo_only/` are illustrative mockups.
- No benchmark values, dataset counts, training metrics, or hardware test results are asserted by this package.
- Replace all placeholders with genuine outputs before presenting the criteria as completed.

## Project terminology
The enclosure target is the OLED display enclosure. The sealed/opened box detector is a separate workstream. Keep class labels and datasets distinct; do not relabel one model's detections as the other.
