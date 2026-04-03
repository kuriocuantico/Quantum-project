# QAOA — Max-Cut con 4 nodos
import numpy as np
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from scipy.optimize import minimize

# El grafo: lista de conexiones (aristas)
aristas = [(0,1), (1,2), (2,3), (3,0), (0,2)]

n_qubits = 4  # un qubit por nodo

def construir_circuito(gamma, beta):
    qc = QuantumCircuit(n_qubits)

    # Superposición inicial
    for i in range(n_qubits):
        qc.h(i)

    # Capa de problema
    for (u, v) in aristas:
        qc.cx(u, v)
        qc.rz(2 * gamma, v)
        qc.cx(u, v)

    # Capa de mezcla
    for i in range(n_qubits):
        qc.rx(2 * beta, i)

    qc.measure_all()
    return qc

def calcular_corte(estado, aristas):
    corte = 0
    for (u, v) in aristas:
        if estado[u] != estado[v]:
            corte += 1
    return corte

def ejecutar_qaoa(params):
    gamma, beta = params
    qc = construir_circuito(gamma, beta)
    simulador = AerSimulator()
    resultado = simulador.run(qc, shots=1000).result()
    conteos = resultado.get_counts()

    # Calcular valor esperado del corte
    valor_total = 0
    total_shots = sum(conteos.values())
    for estado, veces in conteos.items():
        corte = calcular_corte(estado, aristas)
        valor_total += corte * veces
    return -valor_total / total_shots  # negativo porque minimize busca mínimo

# Optimizar parámetros γ y β
print("Optimizando parámetros cuánticos...")
params_iniciales = [0.5, 0.5]
resultado_opt = minimize(
    ejecutar_qaoa,
    params_iniciales,
    method='COBYLA',
    options={'maxiter': 100}
)

gamma_opt, beta_opt = resultado_opt.x
print(f"γ óptimo: {gamma_opt:.3f}")
print(f"β óptimo: {beta_opt:.3f}")

# Ejecutar con parámetros óptimos
print("\nEjecutando con parámetros óptimos...")
qc_final = construir_circuito(gamma_opt, beta_opt)
simulador = AerSimulator()
resultado_final = simulador.run(qc_final, shots=1000).result()
conteos_final = resultado_final.get_counts()

# Mostrar mejores soluciones
print("\n=== MEJORES PARTICIONES ENCONTRADAS ===")
print()
soluciones = []
for estado, veces in conteos_final.items():
    corte = calcular_corte(estado, aristas)
    soluciones.append((estado, corte, veces))

soluciones.sort(key=lambda x: (-x[1], -x[2]))

for estado, corte, veces in soluciones[:5]:
    grupo0 = [i for i,b in enumerate(estado) if b=='0']
    grupo1 = [i for i,b in enumerate(estado) if b=='1']
    barra = '█' * (veces // 20)
    print(f"|{estado}⟩  corte={corte}  {barra} {veces} veces")
    print(f"       Grupo A: nodos {grupo0}  |  Grupo B: nodos {grupo1}")
    print()