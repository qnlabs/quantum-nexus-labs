import pytest
import numpy as np
from src.protocols.autonomous_systems import AutonomousSystem, SystemState

def test_system_initialization():
    """Test autonomous system initialization"""
    system = AutonomousSystem()
    assert system.current_state == SystemState.INITIALIZING
    
    success = system.initialize()
    assert success is True
    assert system.current_state == SystemState.STANDBY

def test_system_activation():
    """Test system activation"""
    system = AutonomousSystem()
    system.initialize()
    
    state = system.activate()
    assert state == SystemState.ACTIVE
    assert system.safety_protocols_active is True

def test_quantum_results_processing():
    """Test processing of quantum computation results"""
    system = AutonomousSystem()
    system.initialize()
    system.activate()
    
    test_results = np.random.rand(10)
    metrics = system.process_quantum_results(test_results)
    
    assert "processing_efficiency" in metrics
    assert "quantum_utilization" in metrics
    assert "pattern_accuracy" in metrics

def test_performance_optimization():
    """Test system self-optimization"""
    system = AutonomousSystem()
    system.initialize()
    system.activate()
    
    # Process some data to generate metrics
    test_results = np.random.rand(10)
    system.process_quantum_results(test_results)
    
    # Test optimization
    optimization_results = system.optimize_performance()
    assert "optimization_status" in optimization_results

def test_safety_protocols():
    """Test safety protocol enforcement"""
    system = AutonomousSystem()
    system.initialize()
    
    assert system.safety_protocols_active is True
    with pytest.raises(RuntimeError):
        # Should raise error if trying to activate with safety protocols disabled
        system.safety_protocols_active = False
        system.activate()
