# QAOA Max-Cut — Quantum Approximate Optimization Algorithm
# Finds the optimal partition of a network to maximize cut edges
# Executed on local simulator and IBM Quantum real hardware (ibm_fez, 156 qubits)

import numpy as np
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from scipy.optimize import minimize

# Graph definition: list of edges (connections between nodes)
edges = [(0,1), (1,2), (2,3), (3,0), (0,2)]
n_qubits = 4  # one qubit per node

def build_circuit(gamma, beta):
    """Build QAOA circuit with given parameters gamma and beta."""
    qc = QuantumCircuit(n_qubits)

    # Initial superposition — explore all partitions simultaneously
    for i in range(n_qubits):
        qc.h(i)

    # Problem layer — encode the graph structure
    for (u, v) in edges:
        qc.cx(u, v)
        qc.rz(2 * gamma, v)
        qc.cx(u, v)

    # Mixing layer — explore neighboring solutions
    for i in range(n_qubits):
        qc.rx(2 * beta, i)

    qc.measure_all()
    return qc

def compute_cut(state, edges):
    """Count how many edges are cut between the two groups."""
    cut = 0
    for (u, v) in edges:
        if state[u] != state[v]:
            cut += 1
    return cut

def run_qaoa(params):
    """Run QAOA circuit and return negative expected cut value."""
    gamma, beta = params
    qc = build_circuit(gamma, beta)
    simulator = AerSimulator()
    result = simulator.run(qc, shots=1000).result()
    counts = result.get_counts()

    # Compute expected cut value
    total_cut = 0
    total_shots = sum(counts.values())
    for state, times in counts.items():
        cut = compute_cut(state, edges)
        total_cut += cut * times
    return -total_cut / total_shots  # negative because minimize seeks minimum

# Optimize gamma and beta parameters
print("Optimizing quantum parameters...")
initial_params = [0.5, 0.5]
opt_result = minimize(
    run_qaoa,
    initial_params,
    method='COBYLA',
    options={'maxiter': 100}
)

gamma_opt, beta_opt = opt_result.x
print(f"Optimal gamma: {gamma_opt:.3f}")
print(f"Optimal beta:  {beta_opt:.3f}")

# Run final circuit with optimal parameters
print("\nRunning with optimal parameters...")
qc_final = build_circuit(gamma_opt, beta_opt)
simulator = AerSimulator()
final_result = simulator.run(qc_final, shots=1000).result()
final_counts = final_result.get_counts()

# Display best partitions found
print("\n=== BEST PARTITIONS FOUND ===\n")
solutions = []
for state, times in final_counts.items():
    cut = compute_cut(state, edges)
    solutions.append((state, cut, times))

solutions.sort(key=lambda x: (-x[1], -x[2]))

for state, cut, times in solutions[:5]:
    group0 = [i for i,b in enumerate(state) if b=='0']
    group1 = [i for i,b in enumerate(state) if b=='1']
    bar = '█' * (times // 20)
    print(f"|{state}⟩  cut={cut}  {bar} {times} times")
    print(f"       Group A: nodes {group0}  |  Group B: nodes {group1}")
    print()