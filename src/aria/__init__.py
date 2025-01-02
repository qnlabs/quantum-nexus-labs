"""
Quantum Nexus Labs - ARIA Protocol Package
Core implementation of the ARIA (Advanced Recursive Intelligence Architecture)
"""

from .core import CoreProtocol
from .neural_patterns import NeuralPatternRecognition

__version__ = '1.0.0'
__all__ = ['CoreProtocol', 'NeuralPatternRecognition']

# Package level constants
PATTERN_DIMENSIONS = (7, 7)
DEFAULT_ACTIVATION_THRESHOLD = 0.75
OPTIMIZATION_INTERVAL_MS = 100  # milliseconds
