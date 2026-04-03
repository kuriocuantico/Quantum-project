Portfolio Cuántico — Kuriocuantico

Implementaciones de algoritmos cuánticos utilizando Qiskit y hardware real de IBM Quantum.
Proyecto desarrollado desde cero como parte del aprendizaje en computación cuántica.

Proyectos
QAOA Max-Cut

Algoritmo de optimización cuántica diseñado para encontrar la partición óptima de una red, maximizando el número de conexiones cortadas. Tiene aplicaciones en logística, finanzas y telecomunicaciones.

Resultado
Partición óptima encontrada con un corte de 4 sobre 5, alcanzando un 94% de precisión.

Hardware
Simulador local y ejecución en IBM ibm_fez (156 qubits, Marruecos)

Conceptos clave
Optimización híbrida cuántico-clásica
QAOA
Parámetros gamma y beta

Algoritmo de Grover — 3 Qubits

Implementación del algoritmo de búsqueda cuántica sobre 8 estados posibles. Permite encontrar un estado específico con alta probabilidad en menos iteraciones que un método clásico.

Resultado
Estado encontrado con aproximadamente un 94% de precisión en 2 iteraciones, frente a 4 intentos promedio en búsqueda clásica.

Oráculo
Diseño parametrizable que permite buscar cualquier estado sin modificar el circuito.

Conceptos clave
Superposición
Interferencia
Amplificación de amplitud

QRNG — Generador Cuántico de Números Aleatorios

Sistema que genera números aleatorios basados en el colapso cuántico real, proporcionando verdadera aleatoriedad, no dependiente de algoritmos deterministas.

Capacidades
Generación de contraseñas de longitud variable
Generación de claves AES-256 de 256 bits

Aplicaciones
Ciberseguridad
Criptografía
Casinos online
Finanzas

Hardware

Simulador local: AerSimulator
Hardware real: IBM ibm_fez (156 qubits, Marruecos)

Tecnologías

Python
Qiskit
IBM Quantum
Scipy
Git

Cómo ejecutar

Instalar dependencias:

pip install qiskit qiskit-aer qiskit-ibm-runtime scipy

Ejecutar proyectos:

python qaoa_maxcut.py
python grover_3qubits.py
python qrng.py

Autor

Kuriocuantico
Aprendiendo computación cuántica desde cero


contacto: kuriocuantico@gmail.com

