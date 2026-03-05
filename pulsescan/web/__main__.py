"""
Main entry point for running the PulseScan web interface.
"""

from . import app

if __name__ == '__main__':
    print("Starting PulseScan Web Dashboard...")
    print("Open http://localhost:5000 in your browser")
    app.run(host='0.0.0.0', port=5000, debug=False)