sequences_result = []
coordinate_result = []
def enumerate_combinations(row, col, direction, buffer_size, combination, combination_coord):
    if buffer_size == 0:
        # print(f'combination_coord: {combination_coord}')
        coordinate_result.append(combination_coord)
        return sequences_result.append(combination)
        # print(combination)
        # return

    if direction == 'horizontal':
        for i in range(len(matrix[0])):
            if is_valid_move(row, i, direction):
                used_coordinates.append([row, i])
                enumerate_combinations(row, i, 'vertical', buffer_size - 1, combination + [matrix[row][i]], combination_coord + [[row, i]])
                used_coordinates.remove([row, i])
    elif direction == 'vertical':
        for i in range(len(matrix)):
            if is_valid_move(i, col, direction):
                used_coordinates.append([i, col])
                enumerate_combinations(i, col, 'horizontal', buffer_size - 1, combination + [matrix[i][col]], combination_coord + [[i, col]])
                used_coordinates.remove([i, col])

# Start enumerating combinations from each cell in the first row
for i in range(len(matrix[0])):
    used_coordinates.clear()
    used_coordinates.append((0, i))  # Mark the starting cell as used
    enumerate_combinations(0, i, 'vertical', buffer_size - 1, [matrix[0][i]], [[0, i]])