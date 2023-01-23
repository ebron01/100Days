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
REPS = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    timerlbl.config(text="Timer")
    checklbl.config(text="")
    canvas.itemconfig(canvas_text, text="00:00")
    global REPS
    REPS = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global REPS
    REPS += 1
    
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    
    if REPS % 8 == 0:
        count_down(long_break_sec)
        timerlbl.config(text="Break", fg=RED)
        window.bell()
    elif REPS % 2 == 0 :
        count_down(short_break_sec)
        timerlbl.config(text="Break", fg=PINK)
        window.bell()
    else:
        count_down(work_sec)
        timerlbl.config(text="WORK", fg=GREEN)
        window.bell()
        

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    minutes = count // 60
    seconds = count % 60
    show = f"{minutes:02}:{seconds:02}"
    canvas.itemconfig(canvas_text, text=show)
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        check_marks = ""
        work_sess = math.floor(REPS/2)
        for index in range(work_sess):
            check_marks += "+"
        checklbl.config(text=check_marks)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pamadoro")
window.config(padx=100, pady=50, bg=YELLOW)



canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="/home/beast/100Days/pamadora/tomato.png")
canvas.create_image(100, 112, image=tomato_img)
canvas_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

timerlbl = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, "bold"))
timerlbl.grid(column=1, row=0)

startbtn = Button(text="Start", highlightthickness=0, command=start_timer)
startbtn.grid(column=0, row=2)
resetbtn = Button(text="Reset", highlightthickness=0, command=reset_timer)
resetbtn.grid(column=2, row=2)


checklbl = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, "bold"))
checklbl.grid(column=1, row=3)

window.mainloop()