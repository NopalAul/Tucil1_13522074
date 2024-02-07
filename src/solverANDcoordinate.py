matrix = [
    ['7A', '55', 'E9', 'E9', '1C', '55'], 
    ['55', '7A', '1C', '7A', 'E9', '55'], 
    ['55', '1C', '1C', '55', 'E9', 'BD'], 
    ['BD', '1C', '7A', '1C', '55', 'BD'], 
    ['BD', '55', 'BD', '7A', '1C', '1C'], 
    ['1C', '55', '55', '7A', '55', '7A']
]

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]


buffer_size = 7
used_coordinates = set()

def is_valid_move(row, col, direction):
    if direction == 'horizontal':
        return col < len(matrix[0]) and (row, col) not in used_coordinates
    elif direction == 'vertical':
        return row < len(matrix) and (row, col) not in used_coordinates


sequences_result = []
coordinate_result = []
def enumerate_combinations(row, col, direction, buffer_size, combination,combination_coord):
    if buffer_size == 0:
        coordinate_result.append(combination_coord)
        return sequences_result.append(combination)
        # print(combination)
        # return

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

# print(coordinate_result)

def write_to_file(sequences, file_name):
    with open(file_name, 'w') as file:
        for sequence in sequences:
            file.write(str(sequence) + '\n')

write_to_file(sequences_result, 'output.txt')
write_to_file(coordinate_result, 'outputCoord.txt')