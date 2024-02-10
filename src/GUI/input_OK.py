import tkinter as tk
from tkinter import filedialog
import os

def open_file_dialog():
    file_path = filedialog.askopenfilename()
    if file_path:
        file_name = os.path.basename(file_path) # Extract file name from path
        selected_file_label.config(text="Selected file: " + file_name)
        with open(file_path, 'r') as file:
            buffer_size = int(file.readline().strip())
            matrix_size = file.readline().split()
            matrix_width = int(matrix_size[0])
            matrix_height = int(matrix_size[1])

            text_widget.insert(tk.END, buffer_size)

            # content = file.read()
            # text_widget.delete(1.0, tk.END)  # Clear previous content
            # text_widget.insert(tk.END, content)

# Create the Tkinter application
root = tk.Tk()

# Create a button to open the file dialog
button = tk.Button(root, text="Open File", command=open_file_dialog)
button.pack()

# Create a text widget to display file content
text_widget = tk.Text(root, height=10, width=40)
text_widget.pack()

# Create a label to display the selected file
selected_file_label = tk.Label(root, text="Selected file: ")
selected_file_label.pack()

# Run the Tkinter event loop
root.mainloop()
