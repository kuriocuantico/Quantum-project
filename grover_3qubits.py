# Grover's Algorithm — 3 qubits (8 possible states)
# Quantum search algorithm with reusable oracle
# Finds any target state with ~94% accuracy in 2 iterations
# vs 4 average attempts with classical search

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

def oracle(circuit, target_state):
    """
    Grover oracle — marks target state with negative phase.
    target_state: 3-bit string, e.g. '101'
    Note: Qiskit reads qubits in reverse order.
    """
    state = target_state[::-1]  # reverse for Qiskit ordering

    # Apply X to qubits that must be 0
    for i, bit in enumerate(state):
        if bit == '0':
            circuit.x(i)

    # CCZ — marks |111⟩ with negative phase
    circuit.ccz(0, 1, 2)

    # Undo X gates
    for i, bit in enumerate(state):
        if bit == '0':
            circuit.x(i)

def diffusion(circuit):
    """
    Grover diffusion operator — amplifies the marked state.
    Same for any target state — never changes.
    """
    circuit.h(0)
    circuit.h(1)
    circuit.h(2)
    circuit.x(0)
    circuit.x(1)
    circuit.x(2)
    circuit.ccz(0, 1, 2)
    circuit.x(0)
    circuit.x(1)
    circuit.x(2)
    circuit.h(0)
    circuit.h(1)
    circuit.h(2)

def grover_search(target_state, shots=1000):
    """
    Full Grover's algorithm for 3 qubits.
    Searches for target_state among 8 possible states.
    Optimal iterations: floor(pi/4 * sqrt(8)) = 2
    """
    print(f"Searching for |{target_state}⟩ among 8 states...")
    print()

    circuit = QuantumCircuit(3, 3)

    # Initial superposition — all 8 states at once
    circuit.h(0)
    circuit.h(1)
    circuit.h(2)
    circuit.barrier()

    # 2 iterations — optimal for N=8
    for _ in range(2):
        oracle(circuit, target_state)
        circuit.barrier()
        diffusion(circuit)
        circuit.barrier()

    # Measurement
    circuit.measure(0, 0)
    circuit.measure(1, 1)
    circuit.measure(2, 2)

    # Run simulation
    simulator = AerSimulator()
    result = simulator.run(circuit, shots=shots).result()
    counts = result.get_counts()

    # Display results
    print("=== RESULTS ===\n")
    for state, times in sorted(counts.items(), key=lambda x: -x[1]):
        bar = '█' * (times // 20)
        percentage = round(times / shots * 100)
        found = " ← FOUND" if state == target_state else ""
        print(f"|{state}⟩  {bar} {times} times ({percentage}%){found}")

    print()
    return counts

# Search all 8 possible states
all_states = ['000', '001', '010', '011', '100', '101', '110', '111']

for state in all_states:
    grover_search(state)
    print("=" * 50)
    print()