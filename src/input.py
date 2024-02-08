# File input.py: Handling input from file or CLI
import os
from pathlib import Path
import random

# INPUT FROM TXT FILE
def input_from_file():
    # File path
    path = os.path.dirname(Path(__file__).absolute())
    # print(f'path: {path}') # del
    source_file = input("Masukkan nama file: ")
    file_name = os.path.join(path, '../' ,source_file)

    # Membaca file
    with open(file_name, "r") as file:
        buffer_size = int(file.readline().strip())
        matrix_size = file.readline().split()
        matrix_width = int(matrix_size[0])
        matrix_height = int(matrix_size[1])

        matrix = []
        for i in range(matrix_height):
            matrix.append(file.readline().strip().split())

        n_sequences = int(file.readline().strip())

        # del
        # # Data: [[[sequence1], reward1], [[sequence2], reward2], ...]
        # sequences_and_reward = []
        # sequence = []
        # for i in range(n_sequences):
        #     sequence = [file.readline().strip().split()]
        #     sequence.append(int(file.readline().strip()))
        #     sequences_and_reward.append(sequence)
        #     # print(f'len matrix: {len(matrix)}')
        
        # Data: 2 array: 1 array untuk sequence, 1 array untuk reward
        sequence_list = []
        reward_list = []
        for i in range(n_sequences):
            sequence = file.readline().strip().split()
            reward_list.append(int(file.readline().strip()))
            sequence_list.append(sequence)
    # # test
    # print(f'sequences: {sequence}')
    # print(f'sequences_list: {sequence_list}')
    # print(f'reward_list: {reward_list}')
    # print(f'seq 1 tokens: {sequence_list[0]}')
    # print(f'seq 1 tokens 1: {sequence_list[0][0]}')
    # print(f'seq 1 reward: {reward_list[0]}')
    # print(f'n_sequences: {n_sequences}')
    # print(f'matrix: {matrix}') 
    # print("Matrix:")
    # print_matrix(matrix)
    # print(f'first row: {matrix[0]}')    
    # print(f'first row first collumn: {matrix[0][0]}')   
    # print(f'buffer_size: {buffer_size}')
    # print(f'matrix_size: {matrix_size}')
    # print(f'matrix_width: {matrix_width}')
    # print(f'matrix_height: {matrix_height}')
    return matrix, matrix_width, matrix_height, buffer_size, matrix_size, n_sequences, sequence_list, reward_list


# INPUT FROM CLI
def input_from_cli():
    n_token = int(input("Jumlah token: "))
    token = str(input("Token: "))
    buffer_size = int(input("Ukuran buffer: "))
    matrix_size = str(input("Ukuran matrix (m n): "))
    n_sequences = int(input("Jumlah sequence: "))
    max_sequence_size = int(input("Ukuran maksimal sequence: "))

    token_arr = token.split()
    matrix_width = int(matrix_size.split()[0])
    matrix_height = int(matrix_size.split()[1])

    # Matrix generator
    matrix = [['' for i in range(matrix_height)] for j in range(matrix_width)]
    print('\nMatrix:')
    for i in range(matrix_width):
        for j in range(matrix_height):
            random_token = random.choice(token_arr) 
            matrix[i][j] = random_token

    sequence_list = []
    reward_list = []
    for i in range(n_sequences):
        sequence = []
        for j in range(random.randint(2, max_sequence_size)):
            random_token = random.choice(token_arr)
            sequence.append(random_token)
        sequence_list.append(sequence)
        reward_list.append(random.randint(10, 100))

    return matrix, token_arr, matrix_width, matrix_height, n_token, token, buffer_size, matrix_size, n_sequences, max_sequence_size, sequence_list, reward_list

    # test 
    print()
    print(f'matrix: {matrix}')
    print("Matrix:")
    print_matrix(matrix)
    print(f'token_arr: {token_arr}')
    print(f'matrix_width: {matrix_width}')
    print(f'matrix_height: {matrix_height}')
    print(f'n_token: {n_token}')
    print(f'token: {token}')
    print(f'buffer_size: {buffer_size}')
    print(f'matrix_size: {matrix_size}')
    print (f'n_sequences: {n_sequences}')
    print(f'max_sequence_size: {max_sequence_size}')
    print(f'sequence_list: {sequence_list}')
    print(f'reward_list: {reward_list}')


# print matrix
def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(f'{matrix[i][j]}', end=' ')
        print()

