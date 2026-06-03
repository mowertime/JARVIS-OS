#!/usr/bin/env python3
import subprocess, json, re, logging
from typing import Dict, Any, List, Optional

logger = logging.getLogger("jarvis.driver-manager")

class DriverManager:
    def __init__(self):
        self.devices = []
    
    def detect_devices(self) -> List[Dict]:
        devices = []
        try:
            result = subprocess.run(["lspci", "-nn"], capture_output=True, text=True)
            for line in result.stdout.strip().split("\n"):
                if not line.strip(): continue
                parts = line.strip().split()
                device = {"vendor_id": "", "device_id": "", "name": line.split(":")[-1].strip() if ":" in line else line, "driver": ""}
                ids = re.search(r'\[([0-9a-fA-F]{4}):([0-9a-fA-F]{4})\]', line)
                if ids: device["vendor_id"], device["device_id"] = ids.group(1), ids.group(2)
                try:
                    drv = subprocess.run(["lspci", "-k", "-s", parts[0]], capture_output=True, text=True)
                    for dline in drv.stdout.split("\n"):
                        if "Kernel driver in use" in dline: device["driver"] = dline.split(":")[-1].strip()
                except: pass
                devices.append(device)
        except: pass
        self.devices = devices
        return devices
    
    def check_drivers(self) -> List[Dict]:
        results = []
        try:
            loaded = set()
            for line in subprocess.run(["lsmod"], capture_output=True, text=True).stdout.strip().split("\n")[1:]:
                if line.strip(): loaded.add(line.split()[0])
            for d in self.devices:
                results.append({"device": d["name"], "vendor": d["vendor_id"], "driver": d["driver"] or "none",
                               "status": "ok" if d["driver"] and d["driver"] in loaded else "missing"})
        except: pass
        return results

def main():
    mgr = DriverManager()
    devices = mgr.detect_devices()
    status = mgr.check_drivers()
    print(json.dumps({"devices": len(devices), "drivers": status}, indent=2))
    missing = [d for d in status if d["status"] == "missing"]
    if missing: print(f"\n{len(missing)} drivers need attention")

if __name__ == "__main__": main()
