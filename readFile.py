# Read from txt file
import os
from pathlib import Path

# Open file
path = os.path.dirname(Path(__file__).absolute())
print(f'path: {path}')

source_file = "soal.txt"
file_name = os.path.join(path, 'test' ,source_file)

# Read file
with open(file_name, "r") as file:
    buffer_size = int(file.readline().strip())
    matrix_size = file.readline().split()
    matrix_width = int(matrix_size[0])
    matrix_height = int(matrix_size[1])

    matrix = []

    for i in range(matrix_height):
        matrix.append(file.readline().strip().split())

    n_sequences = int(file.readline().strip())

    sequences_and_reward = []
    sequence = []
    # Data: [[[sequence1], reward1], [[sequence2], reward2], ...]
    for i in range(n_sequences):
        sequence = [file.readline().strip().split()]
        sequence.append(int(file.readline().strip()))
        sequences_and_reward.append(sequence)
        # print(f'len matrix: {len(matrix)}')

# Test, del
print(f'sequences: {sequence}')
print(f'sequences_and_reward: {sequences_and_reward}')
print(f'seq reward 1: {sequences_and_reward[0]}')
print(f'seq 1 tokens: {sequences_and_reward[0][0]}')
print(f'seq 1 tokens 1: {sequences_and_reward[0][0][0]}')
print(f'seq 1 reward: {sequences_and_reward[0][1]}')
print(f'n_sequences: {n_sequences}')
print(f'matrix: {matrix}') 
print(f'first row: {matrix[0]}')    
print(f'first row first collumn: {matrix[0][0]}')   
print(f'buffer_size: {buffer_size}')
print(f'matrix_size: {matrix_size}')
print(f'matrix_width: {matrix_width}')
print(f'matrix_height: {matrix_height}')




