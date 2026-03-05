"""
System visibility module for collecting system metrics and monitoring.
"""

import platform
import psutil
from typing import Dict, Any, List


class SystemMonitor:
    """
    System monitoring and data collection utilities.
    """

    def get_system_stats(self) -> Dict[str, Any]:
        """
        Get comprehensive system statistics.

        Returns:
            Dictionary containing CPU, memory, disk, and network stats
        """
        return {
            "cpu_percent": psutil.cpu_percent(interval=1),
            "cpu_count": psutil.cpu_count(),
            "memory_percent": psutil.virtual_memory().percent,
            "memory_total": psutil.virtual_memory().total,
            "memory_used": psutil.virtual_memory().used,
            "disk_usage": psutil.disk_usage('/').percent,
            "network_connections": len(psutil.net_connections()),
            "platform": platform.system(),
            "hostname": platform.node()
        }

    def get_process_info(self, limit: int = 10) -> List[Dict[str, Any]]:
        """
        Get information about running processes.

        Args:
            limit: Maximum number of processes to return

        Returns:
            List of dictionaries with process information
        """
        processes = []
        for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
            try:
                processes.append(proc.info)
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue
        # Sort by CPU usage and limit
        processes.sort(key=lambda x: x.get('cpu_percent', 0), reverse=True)
        return processes[:limit]

    def get_network_interfaces(self) -> Dict[str, Any]:
        """
        Get network interface information.

        Returns:
            Dictionary of network interface details
        """
        return psutil.net_if_addrs()