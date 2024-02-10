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

def display_matrix():
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            cell_value = matrix[i][j]
            color = color_map.get(cell_value, 'white')
            label = tk.Label(root, text=cell_value, bg=color, padx=10, pady=10, borderwidth=1, relief="solid")
            label.grid(row=i, column=j)

root = tk.Tk()
root.title("Matrix Display")

# Create a grid of labels to display the matrix
display_matrix()

root.mainloop()
