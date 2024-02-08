# ------- File solver.py: Main program to resolve the problem using brute force algorithm
from time import process_time
from input import *

# TIMER
start_time = process_time()

# INPUT OPTION
input_option = input("Input from file (f) or CLI (c): ")
if input_option == 'f':
    data = input_from_file()
    print(data) # del 
    matrix = data[0]
    matrix_width = data[1]
    matrix_height = data[2]
    buffer_size = data[3]
    matrix_size = data[4]
    n_sequences = data[5]
    sequence_list = data[6]
    reward_list = data[7]

    # # test
    # print(f'matrix: {matrix}')
    # print("Matrix:")
    # print_matrix(matrix)
    # print(f'matrix_width: {matrix_width}')
    # print(f'matrix_height: {matrix_height}')
    # print(f'buffer_size: {buffer_size}')
    # print(f'matrix_size: {matrix_size}')
    # print(f'n_sequences: {n_sequences}')
    # print(f'sequence_list: {sequence_list}')
    # print(f'reward_list: {reward_list}')

elif input_option == 'c':
    data = input_from_cli()
    print(data) # del
    matrix = data[0]
    token_arr = data[1]
    matrix_width = data[2]
    matrix_height = data[3]
    n_token = data[4]
    token = data[5]
    buffer_size = data[6]
    matrix_size = data[7]
    n_sequences = data[8]
    max_sequence_size = data[9]
    sequence_list = data[10]
    reward_list = data[11]

    # # test
    # print(f'matrix: {matrix}')
    # print("Matrix:")
    # print_matrix(matrix)
    # print(f'token_arr: {token_arr}')
    # print(f'matrix_width: {matrix_width}')
    # print(f'matrix_height: {matrix_height}')
    # print(f'n_token: {n_token}')
    # print(f'token: {token}')
    # print(f'buffer_size: {buffer_size}')
    # print(f'matrix_size: {matrix_size}')
    # print(f'n_sequences: {n_sequences}')
    # print(f'max_sequence_size: {max_sequence_size}')
    # print(f'sequence_list: {sequence_list}')
    # print(f'reward_list: {reward_list}')

# BRUTE FORCE ALGORITHM

# Inisialisasi variabel untuk menyimpan koordinat yang sudah digunakan/dikunjungi
used_coordinates = set()

# Fungsi untuk mengecek apakah suatu koordinat valid untuk digunakan (gerakan enumerasi kombinasi adalah valid)
def is_valid_move(row, col, direction):
    if direction == 'horizontal':
        return col < len(matrix[0]) and (row, col) not in used_coordinates
    elif direction == 'vertical':
        return row < len(matrix) and (row, col) not in used_coordinates

# Fungsi untuk mengenumerasi kombinasi dari matrix token
# hasil enumerasi berupa kemungkinan sequence dan koordinatnya
sequences_result = []
coordinate_result = []
def enumerate_combinations(row, col, direction, buffer_size, combination, combination_coord):
    if buffer_size == 0:
        coordinate_result.append(combination_coord)
        return sequences_result.append(combination)

    if direction == 'horizontal':
        for i in range(len(matrix[0])):
            if is_valid_move(row, i, direction):
                used_coordinates.add((row, i))
                enumerate_combinations(row, i, 'vertical', buffer_size - 1, combination + [matrix[row][i]], combination_coord + [(row, i)])
                used_coordinates.remove((row, i))
    elif direction == 'vertical':
        for i in range(len(matrix)):
            if is_valid_move(i, col, direction):
                used_coordinates.add((i, col))
                enumerate_combinations(i, col, 'horizontal', buffer_size - 1, combination + [matrix[i][col]], combination_coord + [(i, col)])
                used_coordinates.remove((i, col))

# Start enumerating combinations from each cell in the first row
for i in range(len(matrix[0])):
    used_coordinates.clear()
    used_coordinates.add((0, i))  # Mark the starting cell as used
    enumerate_combinations(0, i, 'vertical', buffer_size - 1, [matrix[0][i]], [(0, i)])

# Update coordinate result (increment by 1)
coordinate_result_update = []
for sub_list in coordinate_result:
    updated_sub_list = []
    for tup in sub_list:
        updated_tuple = tuple(element + 1 for element in tup)
        updated_sub_list.append(updated_tuple)
    coordinate_result_update.append(updated_sub_list)

# print(coordinate_result_update)

# # File Output
# def write_sequences_to_file(sequences, file_name):
#     with open(file_name, 'w') as file:
#         for sequence in sequences:
#             file.write(str(sequence) + '\n')

# write_sequences_to_file(sequences_result, 'output.txt') # del
# write_sequences_to_file(coordinate_result, 'outputCoord.txt') # del

# Rewarding mechanism
def rewarding(sequences_result, sequences_list, reward_list):
    reward_candidate = []
    for array_result in sequences_result:
        sum_reward = 0
        for index in range(len(sequences_list)):
            array_list = sequences_list[index]
            reward = reward_list[index]
            # print(f'array result: {array_result}')
            # print(f'array list: {array_list}')

            # Array to string
            array_result_str = ' '.join(array_result)
            array_list_str = ' '.join(array_list)

            if array_list_str in array_result_str:
                # print('ada')
                sum_reward += reward

        reward_candidate.append(sum_reward)
                # reward += reward_list[sequences_list.index(array_list)]
    
    # print(f'Reward candidate: {reward_candidate}')
    return reward_candidate

# Final solution
rewarding(sequences_result, sequence_list, reward_list)
index_reward = rewarding(sequences_result, sequence_list, reward_list).index(max(rewarding(sequences_result, sequence_list, reward_list)))
max_reward = max(rewarding(sequences_result, sequence_list, reward_list))
sequences_result_final = ' '.join(sequences_result[index_reward])
coordinate_result_final = coordinate_result_update[index_reward]

print(f'indeks reward: {index_reward}')
print(f'reward: {max_reward}')
print(f'sequences: {sequences_result_final}')
print(f'coordinate: {coordinate_result_final}')

stop_time = process_time()
timer = (stop_time - start_time)*1000

# OUTPUTING SOLUTION
print("Hasil: ")
if(max_reward == 0):
    print(f'Reward maksimal: {max_reward}')
    print(f'Waktu eksekusi: {timer} ms')

else:
    print(f'Reward maksimal: {max_reward}')
    print(f'Sequences: {sequences_result_final}')
    print(f'Coordinate: {coordinate_result_final}')
    print(f'Waktu eksekuasi: {timer} ms')

# OUTPUT SOLUTION TO FILE
choice = input("Apakah anda ingin menyimpan solusi ke dalam file? (y/n): ")

if choice == 'y':
    file_name = str(input("Masukkan nama file (contoh.txt): "))
    with open('test/'+ file_name, 'w') as file:
        file.write(f'{max_reward}\n')
        file.write(f'{sequences_result_final}\n')
        for coord in coordinate_result_final:
            file.write(f'{coord}\n')
        file.write(f'\n{timer} ms\n')
    print(f'Solusi berhasil disimpan ke dalam file {file_name}')
