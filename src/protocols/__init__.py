"""
Quantum Nexus Labs - Protocols Package
Implementation of system protocols and autonomous operations
"""

from .autonomous_systems import AutonomousSystem, SystemState, SystemMetrics

__version__ = '1.0.0'
__all__ = ['AutonomousSystem', 'SystemState', 'SystemMetrics']

# Package level constants
DEFAULT_OPTIMIZATION_THRESHOLD = 0.85
SAFETY_CHECK_INTERVAL_MS = 100  # milliseconds
MAX_RESPONSE_TIME_MS = 10  # milliseconds
