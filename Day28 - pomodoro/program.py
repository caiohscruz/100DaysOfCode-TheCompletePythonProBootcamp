import tkinter as tk
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

# ---------------------------- TIMER RESET ------------------------------- # 



# ---------------------------- TIMER MECHANISM ------------------------------- #

def work_time():
    lbl_text.config(text="It's Work Time!",fg=GREEN)
    count_down(WORK_MIN)


def short_break_time():
    lbl_text.config(text="Make a break", fg=PINK)
    count_down(SHORT_BREAK_MIN)


def long_break_time():
    lbl_text.config(text="Get some rest!", fg=RED)
    count_down(LONG_BREAK_MIN)


def start_timer():
    global reps
    reps += 1
    if reps % 2 == 1:
        work_time()
    else:
        lbl_check.config(text=f"{lbl_check['text']}✔")
        if reps % 2 == 8:
            long_break_time()
        else:
            short_break_time()


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    minutes = math.floor(count / 60)
    seconds = count % 60
    canvas.itemconfig(timer_text, text=f"{minutes:02d}:{seconds:02d}")
    if count > 0:
        window.after(1000, count_down, count - 1)
    else:
        start_timer()# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tk.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

lbl_text = tk.Label(text="Timer", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)
lbl_text.grid(column=1, row=0)

btn_start = tk.Button(text="Start", command=start_timer)
btn_start.grid(column=0, row=2)

btn_reset = tk.Button(text="Reset")
btn_reset.grid(column=2, row=2)

lbl_check = tk.Label(text="", font=(FONT_NAME, 15, "bold"), fg=GREEN, bg=YELLOW)
lbl_check.grid(column=1, row=3)


window.mainloop()