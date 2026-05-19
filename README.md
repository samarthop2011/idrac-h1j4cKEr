# SAM iDRAC Security Audit Toolkit

> Educational and authorized security assessment toolkit for identifying exposed or misconfigured iDRAC interfaces.

---

## ⚠️ Disclaimer

This project is intended **only** for:

* Authorized penetration testing
* Security research
* Lab environments
* Asset auditing on systems you own or have permission to test

Unauthorized access attempts against systems you do not own may violate laws and regulations.

---

# Features

* 🔍 iDRAC endpoint detection
* 🌐 Network scanning support
* 📡 Response fingerprinting
* 🛡️ Security misconfiguration checks
* 📊 Fast threaded scanning
* 🧪 Testing support for lab environments

---

# Supported Targets

* Dell iDRAC
* MegaRAC
* Supermicro BMC interfaces

---

# Installation

```bash
git clone https://github.com/samarthop2011/idrac-h1j4cKEr.git
cd idrac-h1j4cKEr
pip install -r requirements.txt
```

---

# Usage

## Single Target

```bash
python3 h1kr.py <ip>
```

## Multiple Targets

```bash
python3 h1kr.py <ip>
```

## Port Selection

```bash
none
```

---

# Example Output

```text
[*] Starting iDRAC Exploit...
[*] Targeting: https://112.29.189.31:443

============================================================
✅ SUCCESS! Exploit successful in 1.85 seconds.
============================================================

--- 🔑 Extracted Credentials ---
  🔑 Username: root
  🔒 Password: password123
----------------------------------

[Full settings.xml content (raw response) is also available above]
============================================================

[+] Interface: Dell iDRAC
[+] Status: Reachable
[+] Security Headers: Missing
[+] Risk Level: Medium
```

---

# Project Structure

```text
.
├── main.py
├── scanner/
├── modules/
├── output/
├── requirements.txt
└── README.md
```

---

# Roadmap

*

---

# Screenshots

Add screenshots of your terminal, dashboard, or scanner results here.

---

# Contributing

Pull requests and improvements are welcome.

---

# License

MIT License

---

# Author

### SAM

Security Research & Infrastructure Tools
