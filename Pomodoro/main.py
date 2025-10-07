import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.25
SHORT_BREAK_MIN = 0.15
LONG_BREAK_MIN = 20
timer = None
rep = 0

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global rep


    window.after_cancel(timer)
    rep = 0
    canvas.itemconfig(timer1, text=f"00:00")
    title1.config(text="TIMER",fg=RED)
    emoji.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global rep
    rep += 1
    emoji_text = ""

    work_sec = WORK_MIN * 60
    nor_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    if rep % 8 == 0:
        fun(long_break)
        title1.config(text="LONG BREAK",fg=RED)

    elif rep % 2 == 0:
        fun(nor_break)
        title1.config(text="BREAK", fg=PINK)


    else:

        title1.config(text="WORK", fg=GREEN)

        work_session = math.floor(rep/2)
        for _ in range(work_session):
            emoji_text += "🔻"

            emoji.config(text=emoji_text)
        fun(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def fun(a):
    b = math.floor(a / 60)
    c = a % 60
    if c < 10:
        c = f"0{c}"

    canvas.itemconfig(timer1, text=f"{b}:{c}")

    if a > 0:
        global timer

        timer = window.after(1000,fun,a-1)
    else:
        start_timer()
    

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Tomato")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=209,height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(103,112, image= tomato_img)

timer1 = canvas.create_text(103,130,text="00:00",fill="white",font=("Arial",23,"bold"))

canvas.grid(column=1,row=1)

title1 = Label(text="Timer",fg=GREEN,bg=YELLOW,font=(FONT_NAME,30,"bold"))
title1.grid(column=1,row=0)

emoji = Label(fg=RED,bg=YELLOW,font=(FONT_NAME,15,"bold"),pady=30)
emoji.grid(column=1,row=2)

button = Button(text="Start", highlightthickness = 0, command=start_timer)
button.grid(column=0,row=2)

button = Button(text="Reset", command=reset_timer)
button.grid(column=2, row=2)



window.mainloop()