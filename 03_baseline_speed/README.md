# Baseline speed

Run `system_monitor.py` in one terminal and the actual detector in another.

The final detector benchmark must use:
- 20 warm-up iterations minimum
- 100 or more timed runs
- Batch size 1
- Same device, input size, model and test conditions
- Median and p95 latency, FPS, CPU/RAM, accelerator utilization if available, and temperature

Do not submit the starter frame-copy timing as detector performance.
