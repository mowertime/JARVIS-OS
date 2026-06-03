#!/usr/bin/env python3
import subprocess, json, logging
from typing import Dict, Any, List

logger = logging.getLogger("jarvis.firmware")

class FirmwareManager:
    def __init__(self):
        try: self.available = subprocess.run(["fwupdmgr", "--version"], capture_output=True).returncode == 0
        except: self.available = False
    
    def get_devices(self) -> List[Dict]:
        if not self.available: return []
        try:
            r = subprocess.run(["fwupdmgr", "get-devices", "--json"], capture_output=True, text=True, timeout=15)
            return json.loads(r.stdout).get("Devices", []) if r.returncode == 0 and r.stdout.strip() else []
        except: return []
    
    def list_updates(self) -> List[Dict]:
        if not self.available: return []
        try:
            r = subprocess.run(["fwupdmgr", "get-updates", "--json"], capture_output=True, text=True, timeout=30)
            return json.loads(r.stdout).get("Devices", []) if r.returncode == 0 and r.stdout.strip() else []
        except: return []

def main():
    mgr = FirmwareManager()
    print(f"fwupd available: {mgr.available}")
    if mgr.available:
        for d in mgr.get_devices()[:5]:
            print(f"  {d.get('Name', '?')}: v{d.get('Version', '?')}")

if __name__ == "__main__": main()
