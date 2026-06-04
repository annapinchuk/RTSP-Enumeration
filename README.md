# RTSP Enumeration Tool 🎥

A lightweight Python-based utility for discovering and enumerating RTSP endpoints on IP cameras and streaming devices.  
Designed for security testing, lab environments, and research into exposed RTSP services.

---

## ⚡ Features

- Automated RTSP path enumeration  
- Single target or bulk scanning  
- Detection of valid RTSP responses (`200 OK`, SDP metadata)  
- Useful for IoT / IP camera security assessments  

---

## 📦 Installation

```bash
git clone https://github.com/annapinchuk/RTSP-Enumeration.git
cd RTSP-Enumeration
```
## 🚀 Usage

### Scan a single target
Modify target in code, look for
```bash
<IP_ADDRESS> <PORT>
```
Run
```bash
python rtsp_enum.py
```

## 🔍 How It Works

The tool sends RTSP `DESCRIBE` requests to common and vendor-specific endpoints used by IP cameras and streaming devices.

It checks for valid responses such as:

- `RTSP/1.0 200 OK`
- SDP (Session Description Protocol) metadata
- Authentication challenges (`401 Unauthorized`)

This helps identify hidden or undocumented RTSP streams.

---

## 🧪 Use Cases

- IP camera security testing
- IoT enumeration and reconnaissance
- CTF challenges
- Attack surface mapping
- RTSP service auditing in lab environments

---

## ⚠️ Disclaimer

This tool is intended for **educational and authorized security testing only**.  
Do not use it against systems you do not own or have explicit permission to test.

---

## 📜 License

MIT License 

---

## 👤 Author

Maintained by [@annapinchuk](https://github.com/annapinchuk)
