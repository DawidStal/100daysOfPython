from tkinter import *
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
    canvas.itemconfig(timer_text, text="00:00")
    label.config(text="Timer", fg=GREEN)
    checkmarks.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1

    if reps == 8:
        label.config(text="Break", fg=RED)
        seconds = LONG_BREAK_MIN * 60
        countdown(seconds)
    elif reps % 2 == 0:
        label.config(text="Break", fg=PINK)
        seconds = SHORT_BREAK_MIN * 60
        countdown(seconds)
    else:
        label.config(text="Work", fg=GREEN)
        seconds = WORK_MIN * 60
        countdown(seconds)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    count_minutes = str(math.floor(count/60))
    count_seconds = str(math.floor(count % 60))
    canvas.itemconfig(timer_text, text=f"{count_minutes.zfill(2)}:{count_seconds.zfill(2)}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count-1)
    else:
        start_timer()
        marks = ""
        for i in range(math.floor(reps/2)):
            marks += "✔"

        checkmarks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=50, pady=50, bg=YELLOW)

label = Label(text="Timer", font=(FONT_NAME, 30, "bold"))
label.config(bg=YELLOW, fg=GREEN)
label.grid(column=1, row=0)

# Add image to UI
canvas = Canvas(width=200, height=223, highlightthickness=0)
canvas.config(bg=YELLOW)
tomato_img = PhotoImage(file="Day 28 Pomodoro\\tomato.png")
canvas.create_image(100, 111, image=tomato_img)
timer_text = canvas.create_text(100, 135, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

checkmarks = Label(text="")
checkmarks.config(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 15, "bold"))
checkmarks.grid(column=1, row=3)


window.mainloop()
