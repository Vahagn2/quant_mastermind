import numpy as np
import itertools

n_colors = 4
sequence_length = 4

secret_sequence = np.random.randint(1, n_colors + 1, sequence_length)

def generate_possible_sequences(n_colors, sequence_length):
    return list(itertools.product(range(1, n_colors + 1), repeat=sequence_length))

def grade_guess(secret, guess):
    grade = sum(1 for i in range(sequence_length) if secret[i] == guess[i])
    return grade

def play_game():
    print("The secret sequence is:", secret_sequence)
    attempts = 0
    possible_sequences = generate_possible_sequences(n_colors, sequence_length)
    while True:
        guess = possible_sequences[0]  # Choose the first guess
        grade = grade_guess(secret_sequence, guess)
        print("Guess:", guess, "Grade:", grade)
        attempts += 1
        if grade == sequence_length:
            print("Congratulations! You guessed the sequence in", attempts, "attempts.")
            break
        possible_sequences = [seq for seq in possible_sequences if grade_guess(seq, guess) == grade]

play_game()
