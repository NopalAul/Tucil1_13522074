matrix = [
    ['7A', '55', 'E9', 'E9', '1C', '55'],
    ['55', '7A', '1C', '7A', 'E9', '55'],
    ['55', '1C', '1C', '55', 'E9', 'BD'],
    ['BD', '1C', '7A', '1C', '55', 'BD'],
    ['BD', '55', 'BD', '7A', '1C', '1C'],
    ['1C', '55', '55', '7A', '55', '7A']   
]

buffer_size = 7
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up

def is_valid_move(row, col, used_coords):
    return 0 <= row < len(matrix) and 0 <= col < len(matrix[0]) and (row, col) not in used_coords

sequences_result = []
def find_combinations(start_row, start_col, buffer_size, used_coords, combination):
    if len(combination) == buffer_size:
        sequences_result.append(combination)
        # print(combination)
        # with open('output.txt', 'a+') as file:
        #     file.write(str(combination) + '\n')
        return sequences_result
    
    for direction in directions:
        next_row = start_row + direction[0]
        next_col = start_col + direction[1]
        
        if is_valid_move(next_row, next_col, used_coords):
            used_coords.add((next_row, next_col))
            find_combinations(next_row, next_col, buffer_size, used_coords, combination + [matrix[next_row][next_col]])
            used_coords.remove((next_row, next_col))

# Starting from each cell in the matrix
for row in range(len(matrix)):
    for col in range(len(matrix[0])):
        used_coords = set()
        used_coords.add((row, col))
        find_combinations(row, col, buffer_size, used_coords, [matrix[row][col]])

print(sequences_result)