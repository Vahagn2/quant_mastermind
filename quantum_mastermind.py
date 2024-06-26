import numpy as np


def hadamard(n):
    H = np.array([[1, 1], [1, -1]]) / np.sqrt(2)
    H_n = H
    for _ in range(n - 1):
        H_n = np.kron(H_n, H)
    return H_n

def pauli_x(n, target):
    I = np.eye(2)
    X = np.array([[0, 1], [1, 0]])
    gate = I
    for i in range(n):
        if i == target:
            gate = np.kron(gate, X)
        else:
            gate = np.kron(gate, I)
    return gate

def oracle(n):
    oracle_matrix = np.eye(2**n)
    index = int('010', 2)
    oracle_matrix[index, index] = -1
    return oracle_matrix

import random

def generate_hidden_sequence(n, num_colors):
    return [random.randint(0, num_colors - 1) for _ in range(n)]

def grade_guess(hidden_sequence, guess):
    correct_positions = sum(1 for h, g in zip(hidden_sequence, guess) if h == g)
    return correct_positions

def make_guess(n, num_colors):
    return [random.randint(0, num_colors - 1) for _ in range(n)]

def play_game(n, num_colors):
    hidden_sequence = generate_hidden_sequence(n, num_colors)
    attempts = 0
    while True:
        guess = make_guess(n, num_colors)
        attempts += 1
        correct_positions = grade_guess(hidden_sequence, guess)
        print(f"Attempt #{attempts}: Guess: {guess} - Correct Positions: {correct_positions}")
        if correct_positions == n:
            print(f"Guessed the correct sequence {hidden_sequence} in {attempts} attempts!")
            break


n = 3 
num_colors = 

play_game(n, num_colors)

#Sources
#https://github.com/humppamies/QCM/blob/master/QCMastermind.ipynb
#https://www.sourcecodester.com/c/16045/mastermind-game.html
