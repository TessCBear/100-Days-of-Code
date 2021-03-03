import math
from tkinter import *
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
    timer_label.config(text="Timer", fg = GREEN)
    canvas.itemconfig(timer_text, text = "00:00")
    global reps
    reps = 0
    check_label.config(text = "")

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps 
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        countdown(long_break_sec)
        timer_label.config(text="Break", fg = RED)
    elif reps % 2 == 0:
        countdown(short_break_sec)
        timer_label.config(text="Break", fg = PINK)
    else:
        countdown(work_sec)
        timer_label.config(text="Work", fg = GREEN)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def countdown(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text = f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count -1 )
    else:
        start_timer()
        num_checks = reps // 2
        check_string = ""
        for checks in range(0, num_checks):
            check_string += "✔"
        check_label.config(text = check_string)



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(padx = 100, pady = 50, bg = YELLOW)

canvas = Canvas(width = 200, height = 224, bg = YELLOW, highlightthickness = 0)
tomato_img = PhotoImage(file=".\Intermediate\Day 28\\tomato.png")
canvas.create_image(100, 112, image = tomato_img)
timer_text = canvas.create_text(108, 130, text = "00:00", fill = "white", font = ("Courier", 30, "bold"))
canvas.grid(column = 1, row = 1)

timer_label = Label(text = "Timer", font = ("Courier", 40, "bold"), fg = GREEN, bg = YELLOW, highlightthickness = 0)
timer_label.grid(column = 1, row = 0)

check_label = Label(font = ("Courier", 15, "bold"), fg = GREEN, bg = YELLOW, highlightthickness = 0)
check_label.grid(column = 1, row = 3)

start_button = Button(text = "Start", font = ("Courier", 10, "normal"), command = start_timer)
start_button.grid(column = 0, row = 2)

reset_button = Button(text = "Reset", font = ("Courier", 10, "normal"), command = reset_timer)
reset_button.grid(column = 2, row = 2)


window.mainloop()