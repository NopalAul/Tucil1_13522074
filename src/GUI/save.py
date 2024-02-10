import tkinter as tk
from tkinter import filedialog

def save_output():
    file_name = entry.get()
    if file_name:
        # Perform save operation with the file name
        print("Saving output to:", file_name)
        # Close the Toplevel window
        save_window.destroy()

def cancel_save():
    # Close the Toplevel window without saving
    save_window.destroy()

def open_save_window():
    global save_window
    save_window = tk.Toplevel(root)

    # Entry widget for file name input
    global entry
    entry = tk.Entry(save_window)
    entry.pack()

    # Button to save the file
    save_button = tk.Button(save_window, text="Save", command=save_output)
    save_button.pack()

    # Button to cancel saving
    cancel_button = tk.Button(save_window, text="Cancel", command=cancel_save)
    cancel_button.pack()

# Create the Tkinter application
root = tk.Tk()

# Create a button to open the save window
save_button = tk.Button(root, text="Save Output", command=open_save_window)
save_button.pack()

# Run the Tkinter event loop
root.mainloop()
