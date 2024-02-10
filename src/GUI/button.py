import tkinter as tk

def on_enter(e):
    button.config(fill='gray')

def on_leave(e):
    button.config(fill='lightgray')

def on_click(e):
    print("Button clicked!")

root = tk.Tk()
root.geometry("200x100")

canvas = tk.Canvas(root, width=200, height=100, bg='lightgray', highlightthickness=0)
canvas.pack()

button = canvas.create_rectangle(10, 10, 190, 90, fill='lightgray', outline='black', width=2, tags='button')
canvas.tag_bind('button', '<Enter>', on_enter)
canvas.tag_bind('button', '<Leave>', on_leave)
canvas.tag_bind('button', '<Button-1>', on_click)

root.mainloop()
