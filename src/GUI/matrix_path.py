import tkinter as tk

# Define the matrix
matrix = [
    ['7A', '55', 'E9', 'E9', '1C', '55'],
    ['55', '7A', '1C', '7A', 'E9', '55'],
    ['55', '1C', '1C', '55', 'E9', 'BD'],
    ['BD', '1C', '7A', '1C', '55', 'BD'],
    ['BD', '55', 'BD', '7A', '1C', '1C'],
    ['1C', '55', '55', '7A', '55', '7A']
]

# Define colors for each value
color_map = {

}

# Define coordinates to colorize and draw the path
coordinates_to_colorize = [(0, 0), (3, 0), (3, 2), (4, 2), (4, 5), (2, 5), (2, 0)]

def display_matrix_and_path():
    # # Draw the path on top of the matrix cells
    # for i in range(len(coordinates_to_colorize)-1):
    #     row1, col1 = coordinates_to_colorize[i]
    #     row2, col2 = coordinates_to_colorize[i+1]
    #     canvas.create_line(col1*60 + 30, row1*60 + 30, col2*60 + 30, row2*60 + 30, fill="red", width=2)
    
    
    cell_width = 40
    cell_height = 40

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            cell_value = matrix[i][j]
            color = color_map.get(cell_value, 'white')
            label = tk.Label(root, text=cell_value, bg=color, padx=cell_width, pady=cell_height, borderwidth=1, relief="solid")
            label.grid(row=i, column=j)
            
    for i in range(len(coordinates_to_colorize) - 1):
        x0 = coordinates_to_colorize[i][1] * cell_width + cell_width // 2
        y0 = coordinates_to_colorize[i][0] * cell_height + cell_height // 2
        x1 = coordinates_to_colorize[i+1][1] * cell_width + cell_width // 2
        y1 = coordinates_to_colorize[i+1][0] * cell_height + cell_height // 2
        canvas.create_line(x0, y0, x1, y1, fill="red", width=2)

root = tk.Tk()
root.title("Matrix Display with Path")

# Create a canvas to draw the path
canvas = tk.Canvas(root, width=360, height=360)
canvas.place(x=0, y=0)  # Position the canvas at the top-left corner of the window

# Display the matrix and draw the path
display_matrix_and_path()

root.mainloop()
