import tkinter as tk
from tkinter import ttk

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
    '7A': 'red',
    '55': 'blue',
    'E9': 'green',
    '1C': 'yellow',
    'BD': 'orange'
}

# Define coordinates to colorize
coordinates_to_colorize = [(0, 0), (3, 0), (3, 2), (4, 2), (4, 5), (2, 5), (2, 0)]

def display_matrix():
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            cell_value = matrix[i][j]
            color = color_map.get(cell_value, 'white')
            label = tk.Label(root, text=cell_value, bg=color, padx=10, pady=5, borderwidth=1, relief="solid")
            label.grid(row=i, column=j)

def colorize_coordinates():
    for coordinate in coordinates_to_colorize:
        row, column = coordinate
        label = root.grid_slaves(row=row, column=column)[0]
        label.config(bg="cyan")  # Change the color to cyan

root = tk.Tk()
root.title("Matrix Display")

# Create a grid of labels to display the matrix
display_matrix()

# Colorize the coordinates
colorize_coordinates()

root.mainloop()
