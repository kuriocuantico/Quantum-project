# Generador Cuántico de Números Aleatorios (QRNG) — versión corregida
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

def generar_numero_cuantico(bits=8):
    """Genera un número aleatorio cuántico de N bits."""
    qc = QuantumCircuit(bits, bits)
    for i in range(bits):
        qc.h(i)
    qc.measure(list(range(bits)), list(range(bits)))

    simulador = AerSimulator()
    resultado = simulador.run(qc, shots=1).result()
    bits_str = list(resultado.get_counts().keys())[0].replace(' ', '')
    # Tomar solo los primeros N bits
    bits_str = bits_str[:bits]
    return int(bits_str, 2), bits_str

def generar_contrasena_cuantica(longitud=12):
    """Genera una contraseña aleatoria cuántica."""
    caracteres = (
        "abcdefghijklmnopqrstuvwxyz"
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        "0123456789"
        "!@#$%^&*"
    )
    n_chars = len(caracteres)

    contrasena = ""
    while len(contrasena) < longitud:
        numero, _ = generar_numero_cuantico(bits=7)
        if numero < n_chars:
            contrasena += caracteres[numero]
    return contrasena

def generar_clave_cifrado(n_bytes=32):
    """Genera una clave AES-256 cuántica en hexadecimal."""
    clave = ""
    for _ in range(n_bytes):
        numero, _ = generar_numero_cuantico(bits=8)
        numero = numero % 256
        clave += format(numero, '02x')
    return clave

def generar_bit_cuantico():
    """Un solo bit aleatorio cuántico."""
    qc = QuantumCircuit(1, 1)
    qc.h(0)
    qc.measure(0, 0)
    simulador = AerSimulator()
    resultado = simulador.run(qc, shots=1).result()
    return int(list(resultado.get_counts().keys())[0])

# ═══════════════════════════════
# DEMOSTRACIÓN
# ═══════════════════════════════
print("=" * 50)
print("GENERADOR CUÁNTICO DE NÚMEROS ALEATORIOS")
print("=" * 50)
print()

# 1. Bits individuales
print("1. BITS CUÁNTICOS INDIVIDUALES (10 mediciones):")
bits = [generar_bit_cuantico() for _ in range(10)]
print(f"   {''.join(map(str, bits))}")
print()

# 2. Números de diferentes tamaños
print("2. NÚMEROS ALEATORIOS CUÁNTICOS:")
for n_bits in [8, 16, 32]:
    numero, bits_str = generar_numero_cuantico(bits=n_bits)
    maximo = 2**n_bits - 1
    print(f"   {n_bits} bits → {numero:>12} / {maximo}  (binario: {bits_str})")
print()

# 3. Contraseñas cuánticas
print("3. CONTRASEÑAS CUÁNTICAS:")
for i in range(3):
    pwd = generar_contrasena_cuantica(longitud=16)
    print(f"   Contraseña {i+1}: {pwd}")
print()

# 4. Clave AES-256
print("4. CLAVE DE CIFRADO AES-256 CUÁNTICA:")
clave = generar_clave_cifrado(n_bytes=32)
print(f"   {clave[:32]}")
print(f"   {clave[32:]}")
print()

# 5. Comparación cuántico vs clásico
import random
print("5. CUÁNTICO vs CLÁSICO (10 números del 1 al 100):")
cuanticos = [generar_numero_cuantico(bits=7)[0] % 100 + 1 for _ in range(10)]
clasicos  = [random.randint(1, 100) for _ in range(10)]
print(f"   Cuántico: {cuanticos}")
print(f"   Clásico:  {clasicos}")
print()
print("   Diferencia física:")
print("   Cuántico → impredecible por las leyes del universo")
print("   Clásico  → impredecible solo por complejidad matemática")