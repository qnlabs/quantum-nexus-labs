import pytest
import numpy as np
from src.quantum.array_b7 import ArrayB7

def test_array_b7_initialization():
    """Test basic initialization of Array B-7"""
    processor = ArrayB7()
    assert processor.qubit_count == 7
    assert processor.circuit is not None

def test_quantum_state_preparation():
    """Test quantum state preparation"""
    processor = ArrayB7()
    processor.initialize_quantum_state()
    assert processor.circuit.depth() > 0

def test_neural_pattern_application():
    """Test applying neural pattern to quantum circuit"""
    processor = ArrayB7()
    test_pattern = np.random.rand(7)
    processor.initialize_quantum_state()
    processor.apply_neural_pattern(test_pattern)
    assert processor.get_circuit_depth() > 1

def test_circuit_reset():
    """Test circuit reset functionality"""
    processor = ArrayB7()
    processor.initialize_quantum_state()
    initial_depth = processor.get_circuit_depth()
    processor.reset_circuit()
    assert processor.get_circuit_depth() < initial_depth

def test_circuit_measurements():
    """Test quantum measurements"""
    processor = ArrayB7()
    processor.initialize_quantum_state()
    results = processor.measure_quantum_state()
    assert results is not None
    assert len(results) > 0
