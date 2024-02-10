import tkinter as tk

matrix = [
    ['7A', '55', 'E9', 'E9', '1C', '55'],
    ['55', '7A', '1C', '7A', 'E9', '55'],
    ['55', '1C', '1C', '55', 'E9', 'BD'],
    ['BD', '1C', '7A', '1C', '55', 'BD'],
    ['BD', '55', 'BD', '7A', '1C', '1C'],
    ['1C', '55', '55', '7A', '55', '7A']
]

coordinates = [(0, 0), (3, 0), (3, 2), (4, 2), (4, 5), (2, 5), (2, 0)]

def draw_matrix_with_lines(matrix, coordinates):
    root = tk.Tk()
    canvas = tk.Canvas(root, width=300, height=300)
    canvas.pack()

    cell_width = 40
    cell_height = 40

    # Draw matrix
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            x0 = j * cell_width
            y0 = i * cell_height
            x1 = x0 + cell_width
            y1 = y0 + cell_height
            if (i, j) in coordinates:
                if (i, j) == coordinates[-1]:
                    canvas.create_rectangle(x0, y0, x1, y1, outline="black", fill="lightblue")
                elif (i, j) == coordinates[0]:
                    canvas.create_rectangle(x0, y0, x1, y1, outline="black", fill="lightgreen")
                else:
                    canvas.create_rectangle(x0, y0, x1, y1, outline="black", fill="yellow")
            else:
                canvas.create_rectangle(x0, y0, x1, y1, outline="black", fill="white")
            canvas.create_text((x0 + x1) // 2, (y0 + y1) // 2, text=matrix[i][j])

    # Draw lines
    for i in range(len(coordinates) - 1):
        x0 = coordinates[i][1] * cell_width + cell_width // 2
        y0 = coordinates[i][0] * cell_height + cell_height // 2
        x1 = coordinates[i+1][1] * cell_width + cell_width // 2
        y1 = coordinates[i+1][0] * cell_height + cell_height // 2
        canvas.create_line(x0, y0, x1, y1, fill="red", width=2)

    root.mainloop()

draw_matrix_with_lines(matrix, coordinates)
