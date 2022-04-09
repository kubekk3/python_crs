from email.mime import image
from itertools import count
import tkinter
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    check_lbl.config(text="")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps+=1
    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60

    if reps % 8 ==0:
        count_down(long_break_sec)
        label.config(text = "Long Break", fg=PINK)
    elif reps % 2 ==0 or reps % 4 ==0 or reps % 6 ==0:
        count_down(short_break_sec)
        check_lbl.config(text="✓")
        label.config(text = "Short Break", fg=YELLOW)
    elif reps % 1 ==0 or reps % 3 ==0 or reps % 5 ==0:
        count_down(work_sec)
        label.config(text = "Work", fg=RED)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count%60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=GREEN)

label = tkinter.Label()
label.config(text="Timer", fg=YELLOW, bg=GREEN, font=(FONT_NAME, 35, "bold"))
label.grid(column = 2,row = 0)

canvas = tkinter.Canvas(width=200, height=224, bg=GREEN, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image = tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2, row=3)


start_btn = tkinter.Button(command=start_timer)
start_btn.config(text="Start", fg=RED, bg=YELLOW, font=(FONT_NAME, 10, "bold"), highlightthickness=0)
start_btn.grid(column=1, row= 4)

reset_btn = tkinter.Button()    
reset_btn.config(text="Reset", fg=RED, bg=YELLOW, font=(FONT_NAME, 10, "bold"),highlightthickness=0, command=reset_timer)
reset_btn.grid(column=3, row= 4)

check_lbl = tkinter.Label()
check_lbl.config(bg=GREEN, font=(FONT_NAME, 30))
check_lbl.grid(column=2, row=5)

window.mainloop()