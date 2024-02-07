def enumerate_matrix_combinations(matrix, current_combination=[], row_index=0, col_index=0, direction="horizontal", used_coordinates=set()):
    if len(current_combination) == len(matrix):
        print([matrix[row][col] for row, col in current_combination])
        return

    if direction == "horizontal":
        for j in range(col_index, len(matrix[row_index])):
            new_combination = current_combination + [(row_index, j)]
            new_used_coordinates = used_coordinates.copy()
            new_used_coordinates.add((row_index, j))
            enumerate_matrix_combinations(matrix, new_combination, row_index, j, "vertical", new_used_coordinates)
    elif direction == "vertical":
        for i in range(row_index + 1, len(matrix)):
            new_combination = current_combination + [(i, col_index)]
            new_used_coordinates = used_coordinates.copy()
            new_used_coordinates.add((i, col_index))
            enumerate_matrix_combinations(matrix, new_combination, i, col_index, "horizontal", new_used_coordinates)

# Example usage
matrix = [
    ['7A', '55', 'E9', 'E9', '1C', '55'], 
    ['55', '7A', '1C', '7A', 'E9', '55'], 
    ['55', '1C', '1C', '55', 'E9', 'BD'], 
    ['BD', '1C', '7A', '1C', '55', 'BD'], 
    ['BD', '55', 'BD', '7A', '1C', '1C'], 
    ['1C', '55', '55', '7A', '55', '7A']]

enumerate_matrix_combinations(matrix)
