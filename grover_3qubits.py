# Grover con 3 qubits — búsqueda cuántica en 8 estados
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

def oracle(circuito, estado_objetivo):
    """
    Oráculo de Grover — marca el estado objetivo con fase negativa.
    estado_objetivo: string de 3 bits, ejemplo '101'
    """
    # Qiskit lee al revés — invertimos el string
    estado = estado_objetivo[::-1]
    
    # X en qubits que deben ser 0
    for i, bit in enumerate(estado):
        if bit == '0':
            circuito.x(i)
    
    # CCZ — marca el estado |111⟩
    circuito.ccz(0, 1, 2)
    
    # Deshacer X
    for i, bit in enumerate(estado):
        if bit == '0':
            circuito.x(i)

def difusion(circuito):
    """
    Difusión de Grover — amplifica el estado marcado.
    Igual para cualquier estado objetivo.
    """
    circuito.h(0)
    circuito.h(1)
    circuito.h(2)
    circuito.x(0)
    circuito.x(1)
    circuito.x(2)
    circuito.ccz(0, 1, 2)
    circuito.x(0)
    circuito.x(1)
    circuito.x(2)
    circuito.h(0)
    circuito.h(1)
    circuito.h(2)

def grover(estado_objetivo, shots=1000):
    """
    Algoritmo de Grover completo para 3 qubits.
    Busca estado_objetivo entre 8 posibles estados.
    """
    print(f"Buscando |{estado_objetivo}⟩ entre 8 estados...")
    print()

    # Crear circuito
    circuito = QuantumCircuit(3, 3)

    # Superposición inicial
    circuito.h(0)
    circuito.h(1)
    circuito.h(2)
    circuito.barrier()

    # 2 iteraciones — óptimo para N=8
    for i in range(2):
        oracle(circuito, estado_objetivo)
        circuito.barrier()
        difusion(circuito)
        circuito.barrier()

    # Medición
    circuito.measure(0, 0)
    circuito.measure(1, 1)
    circuito.measure(2, 2)

    # Ejecutar
    simulador = AerSimulator()
    resultado = simulador.run(circuito, shots=shots).result()
    conteos = resultado.get_counts()

    # Mostrar resultados
    print("=== RESULTADOS ===")
    print()
    for estado, veces in sorted(conteos.items(), key=lambda x: -x[1]):
        barra = '█' * (veces // 20)
        porcentaje = round(veces / shots * 100)
        marcado = " ← ENCONTRADO" if estado == estado_objetivo else ""
        print(f"|{estado}⟩  {barra} {veces} veces ({porcentaje}%){marcado}")

    print()
    print(circuito.draw(output='text'))
    return conteos

# Buscar los 8 estados posibles
estados = ['000', '001', '010', '011', '100', '101', '110', '111']

for estado in estados:
    grover(estado)
    print()
    print("=" * 50)
    print()