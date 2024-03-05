import threading
import tkinter as tk
import random
import response_generator
import auth

used_btn = []  # For trashing used keywords
rectangles = []  # For trashing placed button position
names = ['A', 'B', 'C']  # Enter names for real use
flag_name = None  # Flag for name(to auth.py)

question_list = []
answer_list = []

pairs = dict(zip(answer_list, question_list))


def on_enter(e):
    e.widget.config(background='lightgray')  # Change to the hover color


def on_leave(e):
    e.widget.config(background='white')  # Change back to the default color


def is_overlapping(x1, y1, x2, y2, rectangles): # Checks overlapping positions
    for rect in rectangles:
        if not (x1 >= rect[2] or x2 <= rect[0] or y1 >= rect[3] or y2 <= rect[1]):
            return True
    return False


def on_exit_click(item): # Returns to name page
    for widget in window.winfo_children():
        widget.destroy()

    used_btn.append(item)
    generate_buttons(rectangles)


def on_back_to_main():
    for widget in window.winfo_children():
        widget.destroy()

    generate_init()


def on_item_click(item_key): # When clicking keyword
    for widget in window.winfo_children():
        widget.destroy()

    answer = pairs[item_key]
    label = tk.Label(window, text=answer, font=('Sandoll 미생', 90), bg='white', wraplength=1000) # Set wraplength to around 0.9*screen_width
    label.pack(expand=True)

    exit_btn = tk.Button(window, text="뒤로가기", command=lambda item=item_key: on_exit_click(item),
                         width=8, height=1, background='white', borderwidth=0, font=('Sandoll 미생', 50))
    exit_btn.bind("<Enter>", on_enter)
    exit_btn.bind("<Leave>", on_leave)
    exit_btn.place(x=30, y=30)


def on_name_click(name): # When clicking name
    for widget in window.winfo_children():
        widget.destroy()

    global used_btn
    used_btn = []

    # Change wraplength to 0.9*screen_width
    label = tk.Label(window, text="로딩중...", font=('Sandoll 미생', 70), bg='white', wraplength=1000)
    # Fetching data from openai takes time
    label.pack(expand=True)

    threading.Thread(target=fetch_data, args=(name,)).start()


def fetch_data(name):
    global flag_name
    flag_name = name

    global question_list
    global answer_list
    global pairs
    question_list = auth.get_sheet_data(flag_name)
    answer_list = response_generator.generate_response(question_list)
    pairs = dict(zip(answer_list, question_list))

    generate_buttons(rectangles)


# Setup the main window
window = tk.Tk()
window.title("신임 리더 인터뷰")
window.configure(background='white')
# screen_width = window.winfo_screenwidth()
# screen_height = window.winfo_screenheight()
window.geometry("1280x700")
# print(f"윈도우 생성: {screen_width}x{screen_height}") <-- use this for general cases

def generate_init(): # Initialize names page(main page)
    for widget in window.winfo_children():
        widget.destroy()

    for index, name in enumerate(names):
        button = tk.Button(window, text=name, command=lambda name=name: on_name_click(name),
                           width=10, height=1, background='white', borderwidth=0, font=('Sandoll 미생', 50))
        button.grid(row=index // 3, column=index % 3, sticky='nsew', padx=50, pady=50)

    for i in range(3):
        window.grid_columnconfigure(i, weight=1)
        window.grid_rowconfigure(i, weight=1)

    print("이름 생성")


def generate_buttons(rectangles): # Random placement of keyword buttons
    rectangles.clear()
    for widget in window.winfo_children():
        widget.destroy()

    for item in answer_list:
        if item not in used_btn:
            while True:
                x = random.randint(100, 620)
                y = random.randint(100, 600)
                if not is_overlapping(x, y, x + 180, y + 100, rectangles):
                    # If not overlapping, place the button and update the list of rectangles
                    button = tk.Button(window, text=item, command=lambda item=item: on_item_click(item),
                                       width=10, height=1, background='white', borderwidth=0, font=('Sandoll 미생', 50))
                    button.bind("<Enter>", on_enter)
                    button.bind("<Leave>", on_leave)
                    button.place(x=x, y=y)
                    rectangles.append((x, y, x + 180, y + 100))
                    break

    backtomain_btn = tk.Button(window, text="처음으로", command=generate_init,
                               width=8, height=1, background='white', borderwidth=0, font=('Sandoll 미생', 50))
    backtomain_btn.bind("<Enter>", on_enter)
    backtomain_btn.bind("<Leave>", on_leave)
    backtomain_btn.place(x=30, y=30)
    print("버튼 생성")


generate_init()

# Start the GUI event loop
window.mainloop()
