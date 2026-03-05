"""
Web interface module using Flask for interactive diagnostics.
"""

from flask import Flask, render_template_string, jsonify
import json

# Import our modules
from ..visibility import SystemMonitor
from ..diagnostics import NetworkScanner

app = Flask(__name__)

monitor = SystemMonitor()
scanner = NetworkScanner()

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>PulseScan Dashboard</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        .metric { background: #f0f0f0; padding: 10px; margin: 10px 0; border-radius: 5px; }
        .status { padding: 5px; border-radius: 3px; }
        .open { background: #d4edda; color: #155724; }
        .closed { background: #f8d7da; color: #721c24; }
    </style>
</head>
<body>
    <h1>PulseScan System Dashboard</h1>

    <div id="system-stats" class="metric">
        <h2>System Statistics</h2>
        <div id="stats-content">Loading...</div>
    </div>

    <div class="metric">
        <h2>Network Diagnostics</h2>
        <button onclick="scanPorts()">Scan Common Ports</button>
        <div id="scan-results"></div>
    </div>

    <script>
        function updateStats() {
            fetch('/api/system')
                .then(response => response.json())
                .then(data => {
                    document.getElementById('stats-content').innerHTML = `
                        <p><strong>CPU Usage:</strong> ${data.cpu_percent}%</p>
                        <p><strong>Memory Usage:</strong> ${data.memory_percent}%</p>
                        <p><strong>Platform:</strong> ${data.platform}</p>
                        <p><strong>Hostname:</strong> ${data.hostname}</p>
                    `;
                });
        }

        function scanPorts() {
            document.getElementById('scan-results').innerHTML = 'Scanning...';
            fetch('/api/scan/localhost')
                .then(response => response.json())
                .then(data => {
                    let html = '<h3>Port Scan Results:</h3>';
                    for (const [port, status] of Object.entries(data)) {
                        html += `<p>Port ${port}: <span class="status ${status}">${status}</span></p>`;
                    }
                    document.getElementById('scan-results').innerHTML = html;
                });
        }

        // Update stats every 5 seconds
        updateStats();
        setInterval(updateStats, 5000);
    </script>
</body>
</html>
"""

@app.route('/')
def dashboard():
    """Main dashboard page."""
    return render_template_string(HTML_TEMPLATE)

@app.route('/api/system')
def api_system():
    """API endpoint for system statistics."""
    return jsonify(monitor.get_system_stats())

@app.route('/api/scan/<host>')
def api_scan(host):
    """API endpoint for port scanning."""
    # Only scan safe ports for demo
    ports = [80, 443, 22, 21, 25, 53]
    results = scanner.scan_ports(host, ports)
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)