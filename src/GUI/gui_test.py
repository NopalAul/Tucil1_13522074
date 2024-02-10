import tkinter as tk
from tkinter import ttk

def on_button_click():
    label.config(text="Hello, " + entry.get())

root = tk.Tk()
root.title("Modern Tkinter App")

style = ttk.Style()
style.theme_use("alt")  # Choose a theme ('clam', 'alt', 'default', etc.)

frame = ttk.Frame(root, padding="20")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

label = ttk.Label(frame, text="Enter your name:")
label.grid(row=0, column=0, sticky=tk.W)

entry = ttk.Entry(frame, width=20)
entry.grid(row=1, column=0, sticky=tk.W)

button = ttk.Button(frame, text="Say Hello", command=on_button_click)
button.grid(row=2, column=0, sticky=tk.W)

root.mainloop()
