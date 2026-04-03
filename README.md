Quantum Portfolio — Kuriocuantico

Implementations of quantum algorithms using Qiskit and real IBM Quantum hardware.
Built from scratch as part of a self-driven journey into quantum computing.

Projects
QAOA Max-Cut

A quantum optimization algorithm designed to find the optimal partition of a graph by maximizing the number of edges cut. It has applications in logistics, finance, and telecommunications.

Result
Optimal partition found with a cut value of 4 out of 5, achieving 94% accuracy.

Hardware
Local simulator and execution on IBM ibm_fez (156 qubits, Morocco)

Key Concepts
Hybrid quantum-classical optimization
QAOA
Gamma and beta parameters

Grover’s Algorithm — 3 Qubits

Implementation of a quantum search algorithm over 8 possible states. It finds a target state with high probability in fewer iterations than classical search methods.

Result
Target state found with approximately 94% accuracy in 2 iterations, compared to an average of 4 attempts classically.

Oracle
Parametrizable design that allows searching for any state without modifying the circuit.

Key Concepts
Superposition
Interference
Amplitude amplification

QRNG — Quantum Random Number Generator

A system that generates random numbers based on real quantum state collapse, providing true randomness rather than deterministic pseudo-randomness.

Capabilities
Generation of variable-length passwords
Generation of 256-bit AES-256 cryptographic keys

Applications
Cybersecurity
Cryptography
Online casinos
Finance

Hardware

Local simulator: AerSimulator
Real hardware: IBM ibm_fez (156 qubits, Morocco)

Technologies

Python
Qiskit
IBM Quantum
Scipy
Git

How to Run

Install dependencies:

pip install qiskit qiskit-aer qiskit-ibm-runtime scipy

Run the projects:

python qaoa_maxcut.py
python grover_3qubits.py
python qrng.py

Author

Kuriocuantico
Learning quantum computing from scratch

contact: kuriocuantico@gmail.com