import pytest
import numpy as np
from src.aria.core import CoreProtocol
from src.quantum.array_b7 import ArrayB7

def test_core_protocol_initialization():
    """Test ARIA core protocol initialization"""
    protocol = CoreProtocol()
    assert protocol.initialization_complete is False
    assert protocol.current_state == "standby"

def test_system_initialization():
    """Test system initialization process"""
    protocol = CoreProtocol()
    protocol.initialize_system()
    assert protocol.initialization_complete is True
    assert protocol.current_state == "initialized"

def test_pattern_registration():
    """Test neural pattern registration"""
    protocol = CoreProtocol()
    protocol.initialize_system()
    
    test_pattern = np.random.rand(7)
    protocol.register_neural_pattern("test_pattern", test_pattern)
    
    assert "test_pattern" in protocol.neural_patterns

def test_pattern_processing():
    """Test pattern processing functionality"""
    protocol = CoreProtocol()
    protocol.initialize_system()
    
    test_pattern = np.random.rand(7)
    protocol.register_neural_pattern("test_pattern", test_pattern)
    
    results = protocol.process_pattern("test_pattern")
    assert "pattern_id" in results
    assert "quantum_state" in results

def test_system_status():
    """Test system status reporting"""
    protocol = CoreProtocol()
    status = protocol.get_system_status()
    
    assert "initialization_status" in status
    assert "current_state" in status
    assert "quantum_processor_status" in status
