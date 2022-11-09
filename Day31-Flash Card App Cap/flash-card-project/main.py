from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
# global variable whbbich starts out as an empty dictionary
learn_word_list = {}

try:
    # reading csv into a data frame where rows are indexed and columns have headings
    words = pandas.read_csv("data/words_to_learn.csv")
# Error will emerge if program has never been used before since csv file not created
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    learn_word_list = original_data.to_dict(orient="records")
else:
    # convert words data frame using records orientation to dictionaries nested within a list
    learn_word_list = words.to_dict(orient="records")


# function outputs a random french word from word_dict
def next_card():
    # global variable modified inside this function so its value can be accessed in flip_card function
    global current_card, flip_timer
    # invalidates flip timer every time button is pressed so that card only flips if it hasn't changed for 3 sec
    window.after_cancel(flip_timer)
    # method picks out random item(a dictionary with two key value pairs representing a rwo) within list
    current_card = random.choice(learn_word_list)
    canvas.itemconfig(card_title, text="French", fill="black")
    # Yields random French word
    canvas.itemconfig(card_word, text= current_card["French"], fill="black")
    # Flips image attribute back to front image everytime next card appears
    canvas.itemconfig(card_background, image=CardFront_Image)
    # triggers flip_card function after 3 sec every time there's a new card
    flip_timer=window.after(3000, func=flip_card)

# function flips card and updates it to the english version
def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    # yields the english word equivalent to the one stored in current_car dictionary
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    # image attribute of the card_background is changed to back image
    canvas.itemconfig(card_background, image=CardBack_Image)

# function removes words from learn_word_dict
def word_known():
    # using remove method to remove current card which is a dictionary item from learn_word_dict
    learn_word_list.remove(current_card)
    # data frame created from list
    data = pandas.DataFrame(learn_word_list)
    # save df to csv, turned off indexing
    data.to_csv("data/words_to_learn.csv", index=False)
    # moves to the next card
    next_card()

# UI
window = Tk()
window.title("Flashy")
window.config(padx=50,pady=50, bg=BACKGROUND_COLOR)
# triggers flip_card function after 3 sec, flip_timer is global
flip_timer = window.after(3000, func=flip_card)

# creating canvas
canvas = Canvas(width=800, height=526 )
# creating image from PhotoImage class
CardFront_Image = PhotoImage(file="images/card_front.png")
CardBack_Image = PhotoImage(file="images/card_back.png")
# created image is placed in the center, half of canvas dimensions
card_background = canvas.create_image(400, 263, image=CardFront_Image)
# creating text, saved into variable so item text can be modified in functions using itemconfig
card_title = canvas.create_text(400,150,text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400,263,text="", font=("Ariel", 60, "bold"))

# removes border around card
canvas.config(bg=BACKGROUND_COLOR,  highlightthickness=0)
# places canvas on grid
canvas.grid(row=0, column=0, columnspan=2)

# creating check and cross buttons
right_image = PhotoImage(file="./images/right.png")
check_button = Button(image=right_image, highlightthickness=0, command=word_known)
check_button.grid(row=1, column=0)

wrong_image = PhotoImage(file="./images/wrong.png")
cross_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
cross_button.grid(row=1, column=1)

# calls next_card function to show next card
next_card()

# updates UI
window.mainloop()