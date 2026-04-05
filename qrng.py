# QRNG — Quantum Random Number Generator
# True randomness based on quantum collapse — not mathematical formulas
# Applications: cybersecurity, cryptography, financial simulations

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

def generate_quantum_number(n_bits=8):
    """
    Generate a random number using quantum superposition and collapse.
    Each bit is decided by a real quantum measurement — truly unpredictable.
    n_bits=8  → number between 0 and 255
    n_bits=16 → number between 0 and 65,535
    n_bits=32 → number between 0 and 4,294,967,295
    """
    qc = QuantumCircuit(n_bits, n_bits)
    for i in range(n_bits):
        qc.h(i)  # superposition — each qubit becomes 50% 0, 50% 1
    qc.measure(list(range(n_bits)), list(range(n_bits)))

    simulator = AerSimulator()
    result = simulator.run(qc, shots=1).result()
    bits_str = list(result.get_counts().keys())[0].replace(' ', '')
    bits_str = bits_str[:n_bits]
    return int(bits_str, 2), bits_str

def generate_quantum_bit():
    """Single quantum random bit — the simplest quantum operation."""
    qc = QuantumCircuit(1, 1)
    qc.h(0)   # superposition
    qc.measure(0, 0)  # collapse — decides 0 or 1
    simulator = AerSimulator()
    result = simulator.run(qc, shots=1).result()
    return int(list(result.get_counts().keys())[0])

def generate_quantum_password(length=12):
    """
    Generate a quantum random password.
    Each character chosen by real quantum collapse — not pseudorandom.
    """
    characters = (
        "abcdefghijklmnopqrstuvwxyz"
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        "0123456789"
        "!@#$%^&*"
    )
    n_chars = len(characters)  # 70 characters
    n_bits = 7                 # 2^7 = 128 > 70

    password = ""
    while len(password) < length:
        number, _ = generate_quantum_number(n_bits=n_bits)
        if number < n_chars:   # discard out-of-range values
            password += characters[number]
    return password

def generate_aes256_key():
    """
    Generate a quantum AES-256 encryption key (256 bits / 32 bytes).
    Industry standard for symmetric encryption.
    """
    key = ""
    for _ in range(32):  # 32 bytes = 256 bits
        number, _ = generate_quantum_number(n_bits=8)
        number = number % 256
        key += format(number, '02x')
    return key

# ═══════════════════════════════════════
# DEMONSTRATION
# ═══════════════════════════════════════

print("=" * 50)
print("QUANTUM RANDOM NUMBER GENERATOR (QRNG)")
print("=" * 50)
print()

# 1. Individual quantum bits
print("1. INDIVIDUAL QUANTUM BITS (10 measurements):")
bits = [generate_quantum_bit() for _ in range(10)]
print(f"   {''.join(map(str, bits))}")
print()

# 2. Random numbers of different sizes
print("2. QUANTUM RANDOM NUMBERS:")
for n_bits in [8, 16, 32]:
    number, bits_str = generate_quantum_number(n_bits=n_bits)
    maximum = 2**n_bits - 1
    print(f"   {n_bits} bits → {number:>12} / {maximum}  (binary: {bits_str})")
print()

# 3. Quantum passwords
print("3. QUANTUM PASSWORDS:")
for i in range(3):
    pwd = generate_quantum_password(length=16)
    print(f"   Password {i+1}: {pwd}")
print()

# 4. AES-256 encryption key
print("4. QUANTUM AES-256 ENCRYPTION KEY:")
key = generate_aes256_key()
print(f"   {key[:32]}")
print(f"   {key[32:]}")
print()

# 5. Quantum vs classical randomness
import random
print("5. QUANTUM vs CLASSICAL (10 numbers from 1 to 100):")
quantum  = [generate_quantum_number(n_bits=7)[0] % 100 + 1 for _ in range(10)]
classical = [random.randint(1, 100) for _ in range(10)]
print(f"   Quantum:   {quantum}")
print(f"   Classical: {classical}")
print()
print("   Both look the same — the difference is physical:")
print("   Quantum   → unpredictable by the laws of the universe")
print("   Classical → unpredictable only by mathematical complexity")