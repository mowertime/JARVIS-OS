#!/usr/bin/env python3
import subprocess, json, re
from typing import Dict, Any, List

class HardwareAbstractionLayer:
    def get_devices(self) -> Dict[str, Any]:
        return {"cpu": self.get_cpu(), "gpu": self.get_gpu(), "memory": self.get_memory(),
                "storage": self.get_storage(), "network": self.get_network(), "audio": self.get_audio_devices()}
    
    def get_cpu(self) -> Dict[str, Any]:
        info = {"vendor": "", "model": "", "cores": 0, "features": []}
        try:
            with open("/proc/cpuinfo") as f: data = f.read()
            info["vendor"] = self._grep(data, "vendor_id")
            info["model"] = self._grep(data, "model name")
            info["cores"] = len(re.findall("^processor", data, re.M))
            flags = self._grep(data, "flags")
            if "avx512" in flags: info["features"].append("avx512")
            if "avx2" in flags: info["features"].append("avx2")
        except: pass
        return info
    
    def get_gpu(self) -> List[Dict]:
        gpus = []
        try:
            for line in subprocess.run(["lspci", "-k"], capture_output=True, text=True).stdout.split("\n"):
                if "VGA" in line or "3D" in line:
                    gpus.append({"device": line.split(":")[-1].strip(), "vendor": line.split()[1] if len(line.split())>1 else ""})
        except: pass
        return gpus
    
    def get_memory(self) -> Dict:
        mem = {"total_kb": 0, "free_kb": 0}
        try:
            with open("/proc/meminfo") as f: data = f.read()
            mem["total_kb"] = int(self._grep(data, "MemTotal").split()[0])
            mem["free_kb"] = int(self._grep(data, "MemFree").split()[0])
        except: pass
        return mem
    
    def get_storage(self) -> List[Dict]:
        disks = []
        try:
            result = subprocess.run(["lsblk", "-J", "-o", "NAME,SIZE,TYPE,MODEL"], capture_output=True, text=True)
            for dev in json.loads(result.stdout).get("blockdevices", []):
                if dev.get("type") == "disk":
                    disks.append({"name": dev["name"], "size": dev.get("size",""), "model": dev.get("model","")})
        except: pass
        return disks
    
    def get_network(self) -> List[Dict]:
        ifaces = []
        try:
            for iface in os.listdir("/sys/class/net"):
                if iface == "lo": continue
                ifaces.append({"name": iface, "address": self._read(f"/sys/class/net/{iface}/address"),
                              "state": self._read(f"/sys/class/net/{iface}/operstate")})
        except: pass
        return ifaces
    
    def get_audio_devices(self) -> List[Dict]:
        devices = []
        try:
            for line in subprocess.run(["lspci"], capture_output=True, text=True).stdout.split("\n"):
                if "Audio" in line: devices.append({"device": line.split(":")[-1].strip()})
        except: pass
        return devices
    
    def _grep(self, data: str, pattern: str) -> str:
        for line in data.split("\n"):
            if line.startswith(pattern) or pattern in line:
                return line.split(":")[-1].strip() if ":" in line else line.strip()
        return ""
    
    def _read(self, path: str) -> str:
        try: return open(path).read().strip()
        except: return ""

if __name__ == "__main__":
    print(json.dumps(HardwareAbstractionLayer().get_devices(), indent=2))
