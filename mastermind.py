import numpy as np
from qiskit_aer import AerSimulator
from qiskit import QuantumCircuit, transpile

def create_mastermind_circuit(n):
    
    circuit = QuantumCircuit(n, n)

    for i in range(n):
        circuit.h(i)

    secret_sequence = ['red', 'blue', 'green', 'yellow']  # Example secret sequence
   
    guess = ['red', 'blue', 'yellow', 'green']  # Example guess

    for i in range(n):
        if guess[i] == secret_sequence[i]:
            circuit.x(i)  # Flip the qubit if the guess is correct
    circuit.measure(range(n), range(n))
    return circuit

n_positions_colors = 4  # Number of positions/colors
mastermind_circuit = create_mastermind_circuit(n_positions_colors)

simulator = AerSimulator()
transpiled_circuit = transpile(mastermind_circuit, simulator)
result = simulator.run(transpiled_circuit, shots=10).result()

counts = result.get_counts(mastermind_circuit)
print("Measurement results:", counts)
