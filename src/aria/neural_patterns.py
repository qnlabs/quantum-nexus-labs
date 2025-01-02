import numpy as np
from typing import Dict, List, Optional
from dataclasses import dataclass
from datetime import datetime

@dataclass
class PatternMetadata:
    """Metadata for neural patterns"""
    created_at: datetime
    last_modified: datetime
    complexity_score: float
    stability_index: float
    quantum_affinity: float

class NeuralPatternRecognition:
    """
    Neural Pattern Recognition System
    Handles pattern detection, analysis, and optimization
    """
    
    def __init__(self):
        self.patterns: Dict[str, np.ndarray] = {}
        self.pattern_metadata: Dict[str, PatternMetadata] = {}
        self.activation_threshold = 0.75
        
    def register_pattern(self, pattern_id: str, pattern_data: np.ndarray) -> PatternMetadata:
        """Register a new neural pattern"""
        if pattern_id in self.patterns:
            raise ValueError(f"Pattern {pattern_id} already exists")
            
        # Normalize pattern data
        normalized_pattern = self._normalize_pattern(pattern_data)
        
        # Calculate pattern metrics
        complexity = self._calculate_complexity(normalized_pattern)
        stability = self._calculate_stability(normalized_pattern)
        q_affinity = self._calculate_quantum_affinity(normalized_pattern)
        
        # Create metadata
        metadata = PatternMetadata(
            created_at=datetime.now(),
            last_modified=datetime.now(),
            complexity_score=complexity,
            stability_index=stability,
            quantum_affinity=q_affinity
        )
        
        # Store pattern and metadata
        self.patterns[pattern_id] = normalized_pattern
        self.pattern_metadata[pattern_id] = metadata
        
        return metadata
        
    def _normalize_pattern(self, pattern: np.ndarray) -> np.ndarray:
        """Normalize pattern data to quantum-compatible format"""
        return (pattern - np.min(pattern)) / (np.max(pattern) - np.min(pattern))
        
    def _calculate_complexity(self, pattern: np.ndarray) -> float:
        """Calculate pattern complexity score"""
        return float(np.std(pattern) * np.log(len(pattern)))
        
    def _calculate_stability(self, pattern: np.ndarray) -> float:
        """Calculate pattern stability index"""
        gradient = np.gradient(pattern)
        return float(1.0 / (1.0 + np.std(gradient)))
        
    def _calculate_quantum_affinity(self, pattern: np.ndarray) -> float:
        """Calculate quantum processing affinity score"""
        # Higher scores indicate better quantum processing potential
        entropy = -np.sum(pattern * np.log2(pattern + 1e-10))
        return float(1.0 / (1.0 + entropy))
        
    def analyze_pattern(self, pattern_id: str) -> Dict[str, float]:
        """Analyze a registered pattern"""
        if pattern_id not in self.patterns:
            raise KeyError(f"Pattern {pattern_id} not found")
            
        pattern = self.patterns[pattern_id]
        metadata = self.pattern_metadata[pattern_id]
        
        return {
            "complexity": metadata.complexity_score,
            "stability": metadata.stability_index,
            "quantum_affinity": metadata.quantum_affinity,
            "activation_potential": float(np.mean(pattern) > self.activation_threshold)
        }
        
    def optimize_pattern(self, pattern_id: str) -> np.ndarray:
        """Optimize pattern for quantum processing"""
        if pattern_id not in self.patterns:
            raise KeyError(f"Pattern {pattern_id} not found")
            
        pattern = self.patterns[pattern_id]
        
        # Apply quantum-oriented optimization
        optimized = pattern.copy()
        mask = optimized < self.activation_threshold
        optimized[mask] *= 0.5  # Reduce sub-threshold activations
        
        return optimized
