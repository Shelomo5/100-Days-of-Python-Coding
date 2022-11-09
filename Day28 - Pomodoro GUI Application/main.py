from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #

#hexcodes for colors
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
# Pomodoro work for 25 min then 5 min break then after 4 x 25 min take 20 min break
# each cycle consists of 8 reps 25(rep 1),5,25,5,25,5,25,20(rep 8)
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
# function resets timer functionalities when reset button is pressed
def reset_timer():

    # cancels timer global variable previously setup which stops timer from running
    window.after_cancel(timer)
    # reset time, use canvas.itemconfig bc created in canvas
    canvas.itemconfig(timer_text, text="00:00")
    # reset title label to Timer
    title_label.config(text="Timer")
    # remove check marks
    check_marks.config(text="")

    #enables button after reset button pressed
    start_button.config(state="normal")

    # use the global keyword if you want to change a global variable inside your function.
    global reps
    # reset global variable reps back to 0 so that variable isn't just changed locally
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
# Function starts timer by triggering count down function below
# with a specific count depending on rep #
def start_timer():
    global reps
    # increases by 1 every time function is called
    reps += 1

    # convert to seconds
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # disables button so it's not pressed twice accidentally
    start_button.config(state="disabled")

    # time for a long break if no remainder bc it's the 8th rep
    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Break", fg=RED)
    # time fore short break if no remainder bc it's 2/4/ or 6th rep
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Break", fg=PINK)
    # time for normal 25 min work period
    else:
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
# count down is responsible for reducing timer display
# count is a constant which differs based on the reps total modified in start_timer()
# after is a method, which after a specific amount of time, calls particular function w/ *args
def count_down(count):
    # returns largest whole number after dividing by 60, minutes
    count_min = math.floor(count / 60)
    # will give us the remainder (seconds remaining) after dividing by 60
    count_sec = count % 60
    # using dynamic typing to change variable from an int to a string
    # makes sure two digits displayed, ex: 01
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    # change canvas text to update count using f string to display min and seconds
    canvas.itemconfigure(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        # after 1000 ms calls function count_down passing argument count after
        # subtracting 1 from it every time until count goes to 0
        timer = window.after(1000, count_down, count-1)
    # when count goes to 0, else is triggered it starts timer again to go to the next rep
    else:
        # starts timer function and rep will be increased by one there
        start_timer()
        marks = ""
        # math.floor ensures we get lower whole number which is the session number
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            # adding one mark to list after two reps or one work_sessions
            marks += "✓"
            # Updating check_marks object
        check_marks.config(text=marks)

        # ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
# apply padding around image
window.config(padx=100, pady=50, bg=YELLOW)

# Creating Timer label
title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)

# creating canvas widget, allows to place text on top of image
# last two key arguments ensure background is yellow
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
# get hold of PhotoImage, a class from tkinter
tomato_image = PhotoImage(file="tomato.png")
# adding image to canvas in the format of a PhotoImage
canvas.create_image(100, 112, image=tomato_image)
# adding text to image
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
# places image at the center
canvas.grid(column=1, row=1)

# creating start button, has a command to start_timer function
start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

# creating reset button, it has a command which stops timer from running
reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

# creating check marks
check_marks = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold"))
check_marks.grid(column=1, row=3)

# every ms it's checking if there was a change to the GUI
window.mainloop()