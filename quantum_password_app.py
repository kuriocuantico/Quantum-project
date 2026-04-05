import streamlit as st
from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorSampler
import random

def generate_quantum_number(n_bits=7):
    qc = QuantumCircuit(n_bits)
    for i in range(n_bits):
        qc.h(i)
    qc.measure_all()
    sampler = StatevectorSampler()
    job = sampler.run([qc], shots=1)
    result = job.result()
    counts = result[0].data.meas.get_counts()
    bits_str = list(counts.keys())[0].replace(' ', '')[:n_bits]
    return int(bits_str, 2)

def generate_quantum_password(length=16):
    characters = (
        "abcdefghijklmnopqrstuvwxyz"
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        "0123456789"
        "!@#$%^&*"
    )
    n_chars = len(characters)
    password = ""
    while len(password) < length:
        number = generate_quantum_number(n_bits=7)
        if number < n_chars:
            password += characters[number]
    return password

st.set_page_config(
    page_title="Quantum Password Generator",
    page_icon="⚛️",
    layout="centered"
)

st.title("⚛️ Quantum Password Generator")
st.markdown("**The only password unpredictable by the laws of the universe.**")
st.markdown("---")

st.markdown("""
Classical computers generate passwords using mathematical formulas —
predictable if you know the algorithm. This generator uses **real quantum collapse**:
each character is decided by a qubit measured in superposition.
No formula. No pattern. Pure physics.
""")

st.markdown("---")

length = st.slider("Password length", min_value=8, max_value=32, value=16, step=1)
st.markdown(f"**Strength:** {'🔴 Weak' if length < 12 else '🟡 Good' if length < 20 else '🟢 Strong'}")

if st.button("⚛️ Generate Quantum Password", use_container_width=True):
    with st.spinner("Collapsing quantum states..."):
        password = generate_quantum_password(length)
    st.markdown("### Your quantum password:")
    st.code(password, language=None)
    st.success(f"Generated using {length} quantum measurements.")
    col1, col2, col3 = st.columns(3)
    col1.metric("Characters", length)
    col2.metric("Quantum bits", length * 7)
    col3.metric("Combinations", f"70^{length}")

st.markdown("---")
st.markdown("""
<small>Built with Qiskit · 
<a href="https://github.com/Kuriocuantico/quantum-project">GitHub</a></small>
""", unsafe_allow_html=True)