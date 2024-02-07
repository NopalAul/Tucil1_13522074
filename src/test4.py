def enumerate_matrix_combinations(matrix, current_combination=[], row_index=0, col_index=0, direction="horizontal", used_coordinates=set()):
    if len(current_combination) == len(matrix) * len(matrix[0]):
        print([matrix[row][col] for row, col in current_combination])
        return

    if direction == "horizontal":
        for j in range(col_index, len(matrix[row_index])):
            if (row_index, j) not in used_coordinates:
                new_combination = current_combination + [(row_index, j)]
                new_used_coordinates = used_coordinates.copy()
                new_used_coordinates.add((row_index, j))
                enumerate_matrix_combinations(matrix, new_combination, row_index, j, "vertical", new_used_coordinates)
    elif direction == "vertical":
        for i in range(row_index + 1, len(matrix)):
            if (i, col_index) not in used_coordinates:
                new_combination = current_combination + [(i, col_index)]
                new_used_coordinates = used_coordinates.copy()
                new_used_coordinates.add((i, col_index))
                enumerate_matrix_combinations(matrix, new_combination, i, col_index, "horizontal", new_used_coordinates)
    else:
        raise ValueError("Invalid direction")

# Example usage
matrix = [
    [1, 2],
    [3, 4],
    [5, 6]
]

enumerate_matrix_combinations(matrix)
