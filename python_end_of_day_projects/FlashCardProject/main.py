from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
curr_card = {}
to_learn = {}

try:
    file = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_file = pandas.read_csv("./data/french_words.csv")
    to_learn = original_file.to_dict(orient="records")
else:
    to_learn = file.to_dict(orient="records")



def next_card():
    global curr_card, flip_timer
    window.after_cancel(flip_timer)
    curr_card = random.choice(to_learn)
    french_word = curr_card["French"]
    canvas.itemconfig(card_bg, image=card_front_img)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=french_word, fill="black")
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_bg, image=card_back_img)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=curr_card["English"], fill="white")

def is_known():
    to_learn.remove(curr_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("./data/words_to_learn.csv", index=False)
    next_card()



window = Tk()
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
window.title("Flash Cards")

flip_timer = window.after(3000, func=flip_card)

cross_img = PhotoImage(file="./images/wrong.png")
unknown_button = Button(image=cross_img, highlightbackground=BACKGROUND_COLOR, command=next_card)
unknown_button.grid(column=0, row=1)

check_img = PhotoImage(file="./images/right.png")
known_button = Button(image=check_img, highlightbackground=BACKGROUND_COLOR, command=is_known)
known_button.grid(column=1, row=1)

card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")
canvas = Canvas(width=800, height=526)
card_bg = canvas.create_image(400, 263, image=card_front_img)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_title = canvas.create_text(400, 150, text="French",font=("Ariel", 40, "italic"), fill="black")
card_word = canvas.create_text(400, 263, text="french_word", font=("Ariel", 60, "bold"), fill="black")
canvas.grid(column=0, row=0, columnspan=2)

next_card()

window.mainloop()
