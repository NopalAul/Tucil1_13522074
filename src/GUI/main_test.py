from tkinter import *

# set awal
window = Tk()

widht = 990
height = 704
x = (window.winfo_screenwidth()//2) - (widht//2) 
y = (window.winfo_screenheight()//2) - (height//2)
window.geometry(f'{widht}x{height}+{x}+{y}')
window.resizable(False, False)
window.title('Cyberpunk 2077 - Breach Protocol Solver')
window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)

# window.minsize(990, 704)
# window.maxsize(990, 704)

# window.geometry('990x704') 
# window.rowconfigure(0, weight=1)
# window.columnconfigure(0, weight=1)
# window.state('zoomed')

page1 = Frame(window)
page2 = Frame(window)
page3 = Frame(window)

for frame in (page1, page2, page3):
    frame.grid(row=0, column=0, sticky='nsew')

# buat munculin page/frame lain
def show_frame(frame):
    frame.tkraise()

show_frame(page1)

################### PAGE 1: HOME ###################
# Background
page1.configure(bg='#0B0F28')

# Title
img_title = PhotoImage(file='assets/title.png')
Label(page1, image=img_title, bg='#0B0F28').pack(pady=(158, 0))

img_solver = PhotoImage(file='assets/solvertxt.png')
Label(page1, image=img_solver, bg='#0B0F28').pack(pady=(20, 0))

chooseTxt = Label(page1, text='CHOOSE YOUR INPUT :', font=('Microsoft YaHei UI',12), bg='#0B0F28', fg='white').pack(pady=(86, 0))

# Button
txt_btn_img = PhotoImage(file='assets/txtbtn.png')
Label(page1, image=txt_btn_img, bg='#0B0F28').pack(pady=(0, 0))

txt_btn = Button(page1, text='T X T  F I L E', font=('Microsoft YaHei UI',12), bg='#95EFFA', fg='#0B0F28', relief=FLAT, command=lambda: show_frame(page2)).place(relx=0.5, rely=0.6, y=-1, anchor=CENTER)

auto_btn_img = PhotoImage(file='assets/autobtn.png')
Label(page1, image=auto_btn_img, bg='#0B0F28').pack(pady=(0, 0))
auto_btn = Button(page1, text='A U T O M A T I C', font=('Microsoft YaHei UI',12), bg='#95EFFA', fg='#0B0F28', relief=FLAT, command=lambda: show_frame(page3)).place(relx=0.5, rely=0.7, y=6, anchor=CENTER)


################### PAGE 2: TXT INPUT ###################
# Background
page2.configure(bg='#0B0F28')

# Title
img_title_page2 = PhotoImage(file='assets/titletxt.png')
Label(page2, image=img_title_page2, bg='#0B0F28').pack(pady=(61, 0))

# Browse Button
browse_btn_img = PhotoImage(file='assets/browse.png')
Label(page2, image=browse_btn_img, bg='#0B0F28').place(x=64.8, y=146)
browse_btn = Button(page2, text='B R O W S E', font=('Microsoft YaHei UI',13), bg='#95EFFA', fg='#0B0F28', relief=FLAT).place(x=119, y=174)

# Uploaded File
uploaded_file_img = PhotoImage(file='assets/uploaded.png')
Label(page2, image=uploaded_file_img, bg='#0B0F28').place(x=59.8, y=261)
uploaded_file_text = Label(page2, text='UPLOADED FILE : ', font=('Microsoft YaHei UI',12), bg='#95EFFA', fg='#0B0F28').place(x=105, y=270)

# Solve Button
solve_btn_img = PhotoImage(file='assets/solvebtn.png')
Label(page2, image=solve_btn_img, bg='#0B0F28').place(x=64.8, y=591)
solve_btn = Button(page2, text='S O L V E', font=('Microsoft YaHei UI',13), bg='#F0A0F9', fg='#0B0F28', relief=FLAT).place(x=130, y=620)

# Matrix
matrix_text = Label(page2, text='M A T R I X :', font=('Microsoft YaHei UI',12), bg='#0B0F28', fg='white').place(x=350, y=130)
matrix_container = PhotoImage(file='assets/mtrx.png')
Label(page2, image=matrix_container, bg='#0B0F28').place(x=350, y=160)

# Result
max_reward_img = PhotoImage(file='assets/maxreward.png')
Label(page2, image=max_reward_img, bg='#0B0F28').place(x=380, y=590)
max_reward_text = Label(page2, text='MAXIMUM REWARD :', font=('Microsoft YaHei UI',11), bg='#95EFFA', fg='#0B0F28').place(x=395, y=600)
sequence_img = PhotoImage(file='assets/sequence.png')
Label(page2, image=sequence_img, bg='#0B0F28').place(x=625, y=590)
sequence_text = Label(page2, text='SEQUENCE :', font=('Microsoft YaHei UI',11), bg='#95EFFA', fg='#0B0F28').place(x=720, y=600)




################### PAGE 3: AUTO INPUT ###################
# Background
page3.configure(bg='#0B0F28')

# Title
img_title_page3 = PhotoImage(file='assets/autoinput.png')
Label(page3, image=img_title_page3, bg='#0B0F28').pack(pady=(55, 0))

#

# Matrix
matrix_text3 = Label(page3, text='M A T R I X :', font=('Microsoft YaHei UI',12), bg='#0B0F28', fg='white').place(x=350, y=130)
matrix_container3 = PhotoImage(file='assets/mtrx.png')
Label(page3, image=matrix_container3, bg='#0B0F28').place(x=350, y=160)

# Solve Button
solve_btn_img3 = PhotoImage(file='assets/solvebtn.png')
Label(page3, image=solve_btn_img3, bg='#0B0F28').place(x=64.8, y=591)
solve_btn3 = Button(page3, text='S O L V E', font=('Microsoft YaHei UI',13), bg='#F0A0F9', fg='#0B0F28', relief=FLAT).place(x=130, y=620)

# Result
max_reward_img3 = PhotoImage(file='assets/maxreward.png')
Label(page3, image=max_reward_img3, bg='#0B0F28').place(x=380, y=590)
max_reward_text3 = Label(page3, text='MAXIMUM REWARD :', font=('Microsoft YaHei UI',11), bg='#95EFFA', fg='#0B0F28').place(x=395, y=600)
sequence_img3 = PhotoImage(file='assets/sequence.png')
Label(page3, image=sequence_img3, bg='#0B0F28').place(x=625, y=590)
sequence_text3 = Label(page3, text='SEQUENCE :', font=('Microsoft YaHei UI',11), bg='#95EFFA', fg='#0B0F28').place(x=720, y=600)

# END
window.mainloop()