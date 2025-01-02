"""
Quantum Nexus Labs - Quantum Processing Package
Handles quantum circuit operations and processing
"""

from .array_b7 import ArrayB7
from .quantum_processor import QuantumProcessor

__version__ = '1.0.0'
__all__ = ['ArrayB7', 'QuantumProcessor']

# Package level constants
MAX_QUBITS = 7
DEFAULT_ERROR_RATE = 0.001
COHERENCE_TIME_US = 100  # microseconds
