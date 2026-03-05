# PulseScan

A modular, high‑performance toolkit for system visibility, safe network diagnostics, and workflow automation.  
Built for developers, researchers, and system architects who need clarity, speed, and actionable insights across devices and environments.

---

## 🚀 Features

- **Safe Network Diagnostics**  
  Modular scanning utilities designed for legitimate research, auditing, and educational use.

- **System Visibility Engine**  
  Collects and organizes system‑level signals for analysis and monitoring.

- **Workflow Automation**  
  Build repeatable pipelines for diagnostics, reporting, and environment checks.

- **Extensible Architecture**  
  Add modules in Python, Flask, or external tools (Nmap, Wireshark, etc.) while maintaining safe boundaries.

- **Developer‑First Design**  
  Clean structure, readable code, and VS Code‑friendly layout.

---

## 🧩 Architecture Overview

PulseScan is designed as a modular Python package with a clean, extensible architecture. The toolkit is organized into core modules that can be used independently or combined for comprehensive system analysis:

### Core Modules

- **`pulsescan.diagnostics`**  
  Safe network diagnostics utilities including port scanning, service enumeration, and connectivity testing. Designed for ethical use in research, auditing, and education.

- **`pulsescan.visibility`**  
  System visibility engine that collects and analyzes system-level metrics including CPU usage, memory statistics, network interfaces, and process information.

- **`pulsescan.automation`**  
  Workflow automation framework for building repeatable diagnostic pipelines, scheduled monitoring, and automated reporting.

- **`pulsescan.web`**  
  Optional Flask-based web interface providing a user-friendly dashboard for interactive diagnostics and real-time monitoring.

### Design Principles

- **Modularity**: Each component can be used independently
- **Safety First**: All network operations are designed to be non-intrusive and ethical
- **Extensibility**: Easy to add new modules or integrate external tools
- **Developer-Friendly**: Clean APIs, comprehensive documentation, and VS Code integration

---

## 📦 Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Install from Source
```bash
git clone https://github.com/yourusername/pulsescan.git
cd pulsescan
pip install -r requirements.txt
pip install -e .
```

### Requirements
- `psutil` - System monitoring
- `flask` - Web interface (optional)
- `requests` - HTTP utilities

---

## 🚀 Usage

### Basic System Visibility
```python
from pulsescan.visibility import SystemMonitor

monitor = SystemMonitor()
stats = monitor.get_system_stats()
print(f"CPU Usage: {stats['cpu_percent']}%")
print(f"Memory Used: {stats['memory_percent']}%")
```

### Network Diagnostics
```python
from pulsescan.diagnostics import NetworkScanner

scanner = NetworkScanner()
results = scanner.scan_ports('localhost', [80, 443, 22])
for port, status in results.items():
    print(f"Port {port}: {status}")
```

### Workflow Automation
```python
from pulsescan.automation import DiagnosticWorkflow

workflow = DiagnosticWorkflow()
workflow.add_step('system_check', monitor.get_system_stats)
workflow.add_step('network_scan', lambda: scanner.scan_ports('localhost', [80, 443]))
results = workflow.run()
```

### Web Interface
```bash
python -m pulsescan.web
```
Then open http://localhost:5000 in your browser.

---

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

---

## 📄 License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

---

## ⚠️ Disclaimer

PulseScan is designed for legitimate, ethical use only. Users are responsible for complying with applicable laws and regulations. The authors assume no liability for misuse.


