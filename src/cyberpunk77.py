from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import os
import random
from time import process_time
import sys

# program ini menggunakan library-library berikut:
# - tkinter: untuk membuat GUI
# - os: untuk mengakses file
# - random: untuk menghasilkan angka random
# - time: untuk menghitung waktu eksekusi
# - sys: untuk mengakses path file

################### ALGORITHM FUNCTION ###################
# BRUTE FORCE ALGORITHM
def solve():
    # Error
    if matrix_arr == []:
        messagebox.showerror("Error", "Please complete the input")
        return
    # Inisialisasi penyimpan koordinat yang sudah digunakan/dikunjungi 
    used_coordinates = set()

    # Fungsi untuk mengecek gerakan enumerasi kombinasi adalah valid
    def is_valid_move(row, col, direction):
        if direction == 'horizontal':
            return col < len(matrix_arr[0]) and (row, col) not in used_coordinates
        elif direction == 'vertical':
            return row < len(matrix_arr) and (row, col) not in used_coordinates

    # Fungsi untuk mengenumerasi kombinasi dari matrix token
    sequences_result = []
    coordinate_result = []
    def enumerate_combinations(row, col, direction, buffer_size, combination, combination_coord):
        # Sudah mencukupi buffer size, tambahkan kombinasi dan koordinatnya ke dalam list hasil
        if buffer_size == 0:
            coordinate_result.append(combination_coord)
            return sequences_result.append(combination)

        # Enumerasi tiap sel matrix secara berarah sesuai aturan, horizontal lalu vertikal
        if direction == 'horizontal':    
            for i in range(len(matrix_arr[0])):
                if is_valid_move(row, i, direction):
                    used_coordinates.add((row, i))
                    enumerate_combinations(row, i, 'vertical', buffer_size - 1, combination + [matrix_arr[row][i]], combination_coord + [(row, i)])
                    used_coordinates.remove((row, i))
        elif direction == 'vertical': 
            for i in range(len(matrix_arr)):
                if is_valid_move(i, col, direction):
                    used_coordinates.add((i, col))
                    enumerate_combinations(i, col, 'horizontal', buffer_size - 1, combination + [matrix_arr[i][col]], combination_coord + [(i, col)]) 
                    used_coordinates.remove((i, col))

    # Timer proses
    start_time = process_time()

    # Melakukan enumerasi kombinasi dari setiap sel dimulai dari row pertama sel pertama
    for i in range(len(matrix_arr[0])):
        used_coordinates.clear()       
        used_coordinates.add((0, i))   
        enumerate_combinations(0, i, 'vertical', buffer_size - 1, [matrix_arr[0][i]], [(0, i)]) 

    # Update hasil koordinat (dari 0-based ke 1-based)
    coordinate_result_update = []
    for sub_list in coordinate_result:
        updated_sub_list = []
        for tup in sub_list:
            updated_tuple = tuple(element + 1 for element in tup)
            updated_sub_list.append(updated_tuple)
        coordinate_result_update.append(updated_sub_list)
    
    # Swap elemen koordinat (row, col) ke (col, row)
    coordinate_result_reversed = []
    for sub_list in coordinate_result_update:
        reversed_sub_list = [(tup[1], tup[0]) for tup in sub_list]
        coordinate_result_reversed.append(reversed_sub_list)

    # Fungsi untuk mekanisme rewarding
    def rewarding(sequences_result, sequences_list, reward_list):
        reward_candidate = []
        for array_result in sequences_result:
            sum_reward = 0
            for index in range(len(sequences_list)):
                array_list = sequences_list[index]
                reward = reward_list[index]

                array_result_str = ' '.join(array_result)
                array_list_str = ' '.join(array_list)
                if array_list_str in array_result_str:
                    print()
                    sum_reward += reward      

            reward_candidate.append(sum_reward) 
        return reward_candidate

    # FINAL SOLUTION
    global max_reward
    global sequences_result_final
    global coordinate_result_final
    global timer

    # cari index reward maksimal dari list reward_candidate
    rewarding(sequences_result, sequence_list, reward_list)
    index_reward = rewarding(sequences_result, sequence_list, reward_list).index(max(rewarding(sequences_result, sequence_list, reward_list)))  
    max_reward = max(rewarding(sequences_result, sequence_list, reward_list))

    # hasil solusi
    sequences_result_final = ' '.join(sequences_result[index_reward])
    coordinate_result_final = coordinate_result_reversed[index_reward]

    stop_time = process_time()
    timer = round((stop_time - start_time)*1000, 2)

    # OUTPUTING SOLUTION
    print("\nHASIL: ")
    if(max_reward == 0):
        print(f'Reward maksimal: {max_reward}')
        print('Sekuens: - ')
        print('Koordinat: - ')
        print(f'\nWaktu eksekusi: {timer} ms')

        coordinate_result[index_reward] = []
        sequences_result_final = '                      -'

    else:
        print(f'Reward maksimal: {max_reward}')
        print(f'Sekuens: {sequences_result_final}')
        print('Koordinat: ')
        for coord in coordinate_result_final:
            print(f'{coord}')
        print(f'\nWaktu eksekusi: {timer} ms')
    
    # Display GUI
    draw_matrix_with_lines(matrix_arr, coordinate_result[index_reward], page2)
    max_reward_result.config(text=max_reward)
    sequence_result.config(text=sequences_result_final)
    time_result.config(text=f'{timer} ms')

    draw_matrix_with_lines(matrix_arr, coordinate_result[index_reward], page3)
    max_reward_result3.config(text=max_reward)
    sequence_result3.config(text=sequences_result_final)
    time_result3.config(text=f'{timer} ms')

    # Save Button
    save_path = resource_path("assets/save.png")
    save_btn_img = PhotoImage(file=save_path)
    save_label = Label(page2, image=save_btn_img, bg='#0B0F28')
    save_label.image = save_btn_img
    save_label.place(x=64.8, y=595)

    save_label3 = Label(page3, image=save_btn_img, bg='#0B0F28')
    save_label3.image = save_btn_img
    save_label3.place(x=64.8, y=595)

    save_btn = Button(page2, text='S A V E', font=('Microsoft YaHei UI',13), bg='#1C2A41', fg='#95EFFA', relief=FLAT, command=save_file)
    save_btn.place(x=137, y=624)

    save_btn3 = Button(page3, text='S A V E', font=('Microsoft YaHei UI',13), bg='#1C2A41', fg='#95EFFA', relief=FLAT, command=save_file)
    save_btn3.place(x=137, y=624)

    solve_label.destroy()
    solve_btn.destroy()
    solve_label3.destroy()
    solve_btn3.destroy()

    browse_label.destroy()
    browse_btn.destroy()

def starting():
    global matrix_arr
    global buffer_size
    global sequence_list
    global reward_list
    global n_token, token, matrix_size, n_sequences, max_sequence_size
    matrix_arr = []
    buffer_size = 0
    sequence_list = []
    reward_list = []
    n_token = 0 
    token = '' 
    matrix_size = '' 
    n_sequences = 0 
    max_sequence_size = 0

# ASSETS PATH
def resource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

# MATRIX DISPLAYER
def draw_matrix_with_lines(matrix, coordinates, page):
    cell_width = 50
    cell_height = 50
    canvas_widht = len(matrix[0]) * cell_width
    canvas_height = len(matrix) * cell_height
    canvas = Canvas(page, width=canvas_widht, height=canvas_height, bg='#E5FDFF', border=0)
    canvas.pack(expand=True, pady=(0, 60), padx=(280, 0))

    # Gambar matrix
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            x0 = j * cell_width
            y0 = i * cell_height
            x1 = x0 + cell_width
            y1 = y0 + cell_height
            if (i, j) in coordinates:
                if (i, j) == coordinates[-1]:
                    canvas.create_rectangle(x0, y0, x1, y1, outline="black", fill="#632828")
                elif (i, j) == coordinates[0]:
                    canvas.create_rectangle(x0, y0, x1, y1, outline="black", fill="#3B6328")
                else:
                    canvas.create_rectangle(x0, y0, x1, y1, outline="black", fill="#626328")
            else:
                canvas.create_rectangle(x0, y0, x1, y1, outline="black", fill="#1C2A41")
            canvas.create_text((x0 + x1) // 2, (y0 + y1) // 2, text=matrix[i][j], fill="#95EFFA")

        # Gambar garis lintasan
        for i in range(len(coordinates) - 1):
            x0 = coordinates[i][1] * cell_width + cell_width // 2
            y0 = coordinates[i][0] * cell_height + cell_height // 2
            x1 = coordinates[i+1][1] * cell_width + cell_width // 2
            y1 = coordinates[i+1][0] * cell_height + cell_height // 2
            canvas.create_line(x0, y0, x1, y1, fill="#F0A0F9", width=2)

# INPUT FILE
def open_file_dialog():
    global matrix_arr
    global buffer_size
    global sequence_list
    global reward_list
    file_path = filedialog.askopenfilename()
    if file_path:
        file_name = os.path.basename(file_path)
        selected_file_label.config(text=file_name)
        with open(file_path, 'r') as file:
            buffer_size = int(file.readline().strip())
            matrix_size = file.readline().split()
            matrix_width = int(matrix_size[0])
            matrix_height = int(matrix_size[1])
            matrix_arr = []
            for i in range(matrix_height):
                matrix_arr.append(file.readline().strip().split())

            n_sequences = int(file.readline().strip())

            # Data: 2 array: 1 array untuk sequence, 1 array untuk reward
            sequence_list = []
            reward_list = []
            for i in range(n_sequences):
                sequence = file.readline().strip().split()
                reward_list.append(int(file.readline().strip()))
                sequence_list.append(sequence)

    # return matrix_arr, matrix_width, matrix_height, buffer_size, matrix_size, n_sequences, sequence_list, reward_list

# INPUT KEYBOARD 
def open_keyboard_input():
    global matrix_arr
    global buffer_size
    global sequence_list
    global reward_list
    global n_token, token, matrix_size, n_sequences, max_sequence_size

    
    n_token = (token_amount_input.get())
    token = (token_input.get())
    buffer_size = (buffer_size_input.get())
    matrix_size = (matrix_size_input.get())
    n_sequences = (sequence_amount_input.get())
    max_sequence_size = (max_sequence_input.get())

    if n_token == '' or token == '' or buffer_size == '' or matrix_size == '' or n_sequences == '' or max_sequence_size == '':
        return None

    n_token = int(token_amount_input.get())
    token = str(token_input.get())
    buffer_size = int(buffer_size_input.get())
    matrix_size = str(matrix_size_input.get())
    n_sequences = int(sequence_amount_input.get())
    max_sequence_size = int(max_sequence_input.get())

    token_arr = token.split()
    matrix_width = int(matrix_size.split()[1])
    matrix_height = int(matrix_size.split()[0])

    # Matrix generator
    matrix_arr = [['' for i in range(matrix_height)] for j in range(matrix_width)]
    for i in range(matrix_width):
        for j in range(matrix_height):
            random_token = random.choice(token_arr) 
            matrix_arr[i][j] = random_token

    # Sequence & reward generator
    sequence_list = []
    reward_list = []
    for i in range(n_sequences):
        sequence = []
        for j in range(random.randint(2, max_sequence_size)):
            random_token = random.choice(token_arr)
            sequence.append(random_token)
        sequence_list.append(sequence)
        reward_list.append(random.randint(10, 100))

    return matrix_arr, token_arr, matrix_width, matrix_height, n_token, token, buffer_size, matrix_size, n_sequences, max_sequence_size, sequence_list, reward_list

def solve_keyboard():
    if open_keyboard_input() == None:
        messagebox.showerror("Error", "Please complete the input")
        return
    solve()


# SAVE FILE GUI
def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        with open(file_path, 'w') as file:
            file.write(f'{max_reward}\n')
            if(max_reward != 0):
                file.write(f'{sequences_result_final}\n')
                for coord in coordinate_result_final:
                    file.write(f'{coord}\n')
            file.write(f'\n{timer} ms\n')
        
        messagebox.showinfo("Save", f"Saved on {file_path}")



################### TKINTER GUI ###################
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

page1 = Frame(window)
page2 = Frame(window)
page3 = Frame(window)

for frame in (page1, page2, page3):
    frame.grid(row=0, column=0, sticky='nsew')

# Munculkan page lain
def show_frame(frame):
    frame.tkraise()

show_frame(page1)
starting()

############## PAGE 1: HOME ##############
# Background
page1.configure(bg='#0B0F28')

# Title
# img_path = resource_path("title.png")
img_path = resource_path("assets/title.png")
img_title = PhotoImage(file=img_path)
Label(page1, image=img_title, bg='#0B0F28').pack(pady=(158, 0))

solver_path = resource_path("assets/solvertxt.png")
img_solver = PhotoImage(file=solver_path)
Label(page1, image=img_solver, bg='#0B0F28').pack(pady=(20, 0))

chooseTxt = Label(page1, text='CHOOSE YOUR INPUT :', font=('Microsoft YaHei UI',12), bg='#0B0F28', fg='white').pack(pady=(86, 0))

# Button
txt_path = resource_path("assets/txtbtn.png")
txt_btn_img = PhotoImage(file=txt_path)
# Label(page1, image=txt_btn_img, bg='#0B0F28').pack(pady=(0, 0))

txt_btn = Button(page1, image=txt_btn_img, bg='#0B0F28', relief=FLAT, command=lambda: show_frame(page2)).place(relx=0.5, rely=0.6, y=-10, anchor=CENTER)

auto_path = resource_path("assets/autobtn.png")
auto_btn_img = PhotoImage(file=auto_path)
# Label(page1, image=auto_btn_img, bg='#0B0F28').pack(pady=(0, 0))
auto_btn = Button(page1, image=auto_btn_img, bg='#0B0F28', relief=FLAT, command=lambda: show_frame(page3)).place(relx=0.5, rely=0.7, y=6, anchor=CENTER)


############## PAGE 2: TXT INPUT ##############
# Background
page2.configure(bg='#0B0F28')

# Back button
back_path = resource_path("assets/back.png")
back_btn_img2 = PhotoImage(file=back_path)
back_btn2 = Button(page2, image=back_btn_img2, bg='#0B0F28', relief=FLAT, command=lambda: show_frame(page1)).place(x=82, y=62+110)

# Title
titletext_path = resource_path("assets/titletxt.png")
img_title_page2 = PhotoImage(file=titletext_path)
Label(page2, image=img_title_page2, bg='#0B0F28').pack(pady=(61, 0))

# Browse Button
browse_path = resource_path("assets/browse.png")
browse_btn_img = PhotoImage(file=browse_path)
browse_label = Label(page2, image=browse_btn_img, bg='#0B0F28')
browse_label.place(x=64.8, y=146+110)
browse_btn = Button(page2, text='B R O W S E', font=('Microsoft YaHei UI',13), bg='#95EFFA', fg='#0B0F28', relief=FLAT, command=open_file_dialog)
browse_btn.place(x=119, y=174+110)

# Uploaded File
upload_path = resource_path("assets/uploaded.png")
uploaded_file_img = PhotoImage(file=upload_path)
Label(page2, image=uploaded_file_img, bg='#0B0F28').place(x=59.8, y=261+110)
uploaded_file_text = Label(page2, text='UPLOADED FILE : ', font=('Microsoft YaHei UI',12), bg='#95EFFA', fg='#0B0F28').place(x=105, y=270+110)

selected_file_label = Label(page2, text="", font=('Microsoft YaHei UI',12), bg='#1C2A41', fg='#95EFFA')
selected_file_label.place(x=135, y=310+110)

# Solve Button
solve_path = resource_path("assets/solvebtn.png")
solve_btn_img = PhotoImage(file=solve_path)
solve_label = Label(page2, image=solve_btn_img, bg='#0B0F28')
solve_label.place(x=64.8, y=591)
solve_btn = Button(page2, text='S O L V E', font=('Microsoft YaHei UI',13), bg='#F0A0F9', fg='#0B0F28', relief=FLAT, command=solve)
solve_btn.place(x=130, y=620)

# Matrix
matrix_text = Label(page2, text='M A T R I X :', font=('Microsoft YaHei UI',12), bg='#0B0F28', fg='white').place(x=350, y=130)
container_path = resource_path("assets/mtrx.png")
matrix_container = PhotoImage(file=container_path)
Label(page2, image=matrix_container, bg='#0B0F28').place(x=350, y=160)

# Result
max_path = resource_path("assets/maxreward.png")
max_reward_img = PhotoImage(file=max_path)
Label(page2, image=max_reward_img, bg='#0B0F28').place(x=310, y=590)
max_reward_text = Label(page2, text='MAXIMUM REWARD :', font=('Microsoft YaHei UI',11), bg='#95EFFA', fg='#0B0F28').place(x=335, y=600)
max_reward_result = Label(page2, text="", font=('Microsoft YaHei UI',12), bg='#1C2A41', fg='#95EFFA')
max_reward_result.place(x=407, y=635)

sequence_path = resource_path("assets/sequence.png")
sequence_img = PhotoImage(file=sequence_path)
Label(page2, image=sequence_img, bg='#0B0F28').place(x=538, y=590)
sequence_text = Label(page2, text='SEQUENCE :', font=('Microsoft YaHei UI',11), bg='#95EFFA', fg='#0B0F28').place(x=633, y=600)
sequence_result = Label(page2, text="", font=('Microsoft YaHei UI',12), bg='#1C2A41', fg='#95EFFA')
sequence_result.place(x=563, y=635)

time_path = resource_path("assets/time.png")
time_img = PhotoImage(file=time_path)
Label(page2, image=time_img, bg='#0B0F28').place(x=826, y=590)
time_text = Label(page2, text='TIME :', font=('Microsoft YaHei UI',11), bg='#95EFFA', fg='#0B0F28').place(x=860, y=600)
time_result = Label(page2, text="", font=('Microsoft YaHei UI',12), bg='#1C2A41', fg='#95EFFA')
time_result.place(x=842, y=635)


############## PAGE 3: AUTO INPUT ##############
# Background
page3.configure(bg='#0B0F28')

# Back button
back_path3 = resource_path("assets/back.png")
back_btn_img = PhotoImage(file=back_path3)
back_btn = Button(page3, image=back_btn_img, bg='#0B0F28', relief=FLAT, command=lambda: show_frame(page1)).place(x=82, y=62)

# Title
titletext_path3 = resource_path("assets/autoinput.png")
img_title_page3 = PhotoImage(file=titletext_path3)
Label(page3, image=img_title_page3, bg='#0B0F28').pack(pady=(55, 0))

# Token
token_path = resource_path("assets/inputamt.png")
token_amount_img = PhotoImage(file=token_path)
Label(page3, image=token_amount_img, bg='#0B0F28').place(x=59.8, y=171)
token_amount_text = Label(page3, text='TOKEN AMOUNT:', font=('Microsoft YaHei UI',12), bg='#95EFFA', fg='#0B0F28').place(x=85, y=181)
token_amount_input = Entry(page3, width=2, border=0, font=('Microsoft YaHei UI',12), bg='#1C2A41', fg='#95EFFA')
token_amount_input.place(x=252, y=181)

tokenput_path = resource_path("assets/tokeninput.png")
token_img = PhotoImage(file=tokenput_path)
Label(page3, image=token_img, bg='#0B0F28').place(x=59.8, y=231)
token_text = Label(page3, text='TOKEN:', font=('Microsoft YaHei UI',12), bg='#95EFFA', fg='#0B0F28').place(x=140, y=241)
token_input = Entry(page3, width=20, border=0, font=('Microsoft YaHei UI',12), bg='#1C2A41', fg='#95EFFA')
token_input.place(x=80, y=281)

# Buffer size
buff_path = resource_path("assets/inputamt.png")
buffer_size_img = PhotoImage(file=buff_path)
Label(page3, image=buffer_size_img, bg='#0B0F28').place(x=59.8, y=333)
buffer_size_text = Label(page3, text='BUFFER SIZE:', font=('Microsoft YaHei UI',12), bg='#95EFFA', fg='#0B0F28').place(x=100, y=343)
buffer_size_input = Entry(page3, width=2, border=0, font=('Microsoft YaHei UI',12), bg='#1C2A41', fg='#95EFFA')
buffer_size_input.place(x=252, y=345)

# Matrix size
matrix_path = resource_path("assets/inputamt.png")
matrix_size_img = PhotoImage(file=matrix_path)
Label(page3, image=matrix_size_img, bg='#0B0F28').place(x=59.8, y=393)
matrix_size_text = Label(page3, text='MATRIX SIZE:', font=('Microsoft YaHei UI',12), bg='#95EFFA', fg='#0B0F28').place(x=100, y=403)
matrix_size_input = Entry(page3, width=3, border=0, font=('Microsoft YaHei UI',10), bg='#1C2A41', fg='#95EFFA')
matrix_size_input.place(x=249, y=406)

# Sequence amount
seqamt_path = resource_path("assets/inputamt.png")
sequence_amount_img = PhotoImage(file=seqamt_path)
Label(page3, image=sequence_amount_img, bg='#0B0F28').place(x=59.8, y=454)
sequence_amount_text = Label(page3, text='SEQUENCE AMT:', font=('Microsoft YaHei UI',12), bg='#95EFFA', fg='#0B0F28').place(x=86, y=464)
sequence_amount_input = Entry(page3, width=2, border=0, font=('Microsoft YaHei UI',12), bg='#1C2A41', fg='#95EFFA')
sequence_amount_input.place(x=252, y=466)

# Max sequence
maxseq_path = resource_path("assets/inputamt.png")
max_sequence_img = PhotoImage(file=maxseq_path)
Label(page3, image=max_sequence_img, bg='#0B0F28').place(x=59.8, y=515)
max_sequence_text = Label(page3, text='MAX SEQUENCE:', font=('Microsoft YaHei UI',12), bg='#95EFFA', fg='#0B0F28').place(x=86, y=525)
max_sequence_input = Entry(page3, width=2, border=0, font=('Microsoft YaHei UI',12), bg='#1C2A41', fg='#95EFFA')
max_sequence_input.place(x=252, y=527)

# Matrix
matext_path = resource_path("assets/mtrx.png")
matrix_text3 = Label(page3, text='M A T R I X :', font=('Microsoft YaHei UI',12), bg='#0B0F28', fg='white').place(x=350, y=130)
matrix_container3 = PhotoImage(file=matext_path)
Label(page3, image=matrix_container3, bg='#0B0F28').place(x=350, y=160)

# Solve Button
solve_path3 = resource_path("assets/solvebtn.png")
solve_btn_img3 = PhotoImage(file=solve_path3)
solve_label3 = Label(page3, image=solve_btn_img3, bg='#0B0F28')
solve_label3.place(x=64.8, y=591)
solve_btn3 = Button(page3, text='S O L V E', font=('Microsoft YaHei UI',13), bg='#F0A0F9', fg='#0B0F28', relief=FLAT, command=solve_keyboard)
solve_btn3.place(x=130, y=620)

# Result
res_path = resource_path("assets/maxreward.png")
max_reward_img3 = PhotoImage(file=res_path)
Label(page3, image=max_reward_img3, bg='#0B0F28').place(x=310, y=590)
max_reward_text3 = Label(page3, text='MAXIMUM REWARD :', font=('Microsoft YaHei UI',11), bg='#95EFFA', fg='#0B0F28').place(x=335, y=600)
max_reward_result3 = Label(page3, text="", font=('Microsoft YaHei UI',12), bg='#1C2A41', fg='#95EFFA')
max_reward_result3.place(x=400, y=635)

seq_path3 =  resource_path("assets/sequence.png")
sequence_img3 = PhotoImage(file=seq_path3)
Label(page3, image=sequence_img3, bg='#0B0F28').place(x=538, y=590)
sequence_text3 = Label(page3, text='SEQUENCE :', font=('Microsoft YaHei UI',11), bg='#95EFFA', fg='#0B0F28').place(x=633, y=600)
sequence_result3 = Label(page3, text="", font=('Microsoft YaHei UI',12), bg='#1C2A41', fg='#95EFFA')
sequence_result3.place(x=563, y=635)

time_path3 = resource_path("assets/time.png")
time_img3 = PhotoImage(file=time_path3)
Label(page3, image=time_img3, bg='#0B0F28').place(x=826, y=590)
time_text3 = Label(page3, text='TIME :', font=('Microsoft YaHei UI',11), bg='#95EFFA', fg='#0B0F28').place(x=860, y=600)
time_result3 = Label(page3, text="", font=('Microsoft YaHei UI',12), bg='#1C2A41', fg='#95EFFA')
time_result3.place(x=844, y=635)

# END
window.mainloop()