BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *
import pandas as pd
import random 

CURRENT_CARD = {}

def flip_card():
    canvas.itemconfig(card_background, image=card_back_png)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    
def next_card():#if i click check or x before 3seconds timer must be cancelled. 
    # After setting new car it must restart. thats why we cancel_after.
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_background, image=card_front_png)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    flip_timer = window.after(3000, flip_card)

def is_known():
    to_learn.remove(current_card)
    next_card()
    pd.DataFrame(to_learn).to_csv("/home/beast/100Days/flashcard/data/words_to_learn.csv", index=False)
    
#read the file 
try:
    data = pd.read_csv("/home/beast/100Days/flashcard/data/words_to_learn.csv")
except FileNotFoundError:
    data = pd.read_csv("/home/beast/100Days/flashcard/data/french_words.csv")
to_learn = data.to_dict(orient="records")

window = Tk()
window.title("FlashCard")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, flip_card)

#canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_png = PhotoImage(file="/home/beast/100Days/flashcard/images/card_front.png")
card_back_png = PhotoImage(file="/home/beast/100Days/flashcard/images/card_back.png")

card_background = canvas.create_image(400, 263, image=card_front_png)

card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "bold"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))

canvas.grid(column=1, columnspan=2, row=0)


#buttons 
cross_image = PhotoImage(file="/home/beast/100Days/flashcard/images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(column=1,row=1)

check_image = PhotoImage(file="/home/beast/100Days/flashcard/images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=is_known)
known_button.grid(column=2, row=1)

next_card()



window.mainloop()
