"""
Network diagnostics module for safe, ethical network scanning.
"""

import socket
import time
from typing import Dict, List


class NetworkScanner:
    """
    Safe network scanning utilities for diagnostics and research.
    """

    def __init__(self, timeout: float = 1.0):
        self.timeout = timeout

    def scan_port(self, host: str, port: int) -> str:
        """
        Scan a single port on a host.

        Args:
            host: Target hostname or IP
            port: Port number to scan

        Returns:
            "open" if port is open, "closed" otherwise
        """
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(self.timeout)
            result = sock.connect_ex((host, port))
            sock.close()
            return "open" if result == 0 else "closed"
        except Exception:
            return "error"

    def scan_ports(self, host: str, ports: List[int]) -> Dict[int, str]:
        """
        Scan multiple ports on a host.

        Args:
            host: Target hostname or IP
            ports: List of port numbers to scan

        Returns:
            Dictionary mapping port numbers to their status
        """
        results = {}
        for port in ports:
            results[port] = self.scan_port(host, port)
            time.sleep(0.1)  # Rate limiting for safety
        return results

    def ping_host(self, host: str) -> bool:
        """
        Simple connectivity check using socket.

        Args:
            host: Target hostname or IP

        Returns:
            True if host is reachable, False otherwise
        """
        try:
            socket.gethostbyname(host)
            return True
        except socket.gaierror:
            return False