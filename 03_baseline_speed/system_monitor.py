"""Print live CPU, RAM and temperature where exposed by the OS."""
import time
import psutil
from pathlib import Path

def read_cpu_temperature():
    candidates = [
        Path("/sys/class/thermal/thermal_zone0/temp"),
        Path("/sys/devices/virtual/thermal/thermal_zone0/temp"),
    ]
    for path in candidates:
        try:
            return float(path.read_text().strip()) / 1000.0
        except (OSError, ValueError):
            pass
    return None

while True:
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    temp = read_cpu_temperature()
    temp_text = f"{temp:.1f} C" if temp is not None else "unavailable"
    print(f"CPU: {cpu:.1f}% | RAM: {ram:.1f}% | Temperature: {temp_text}")
