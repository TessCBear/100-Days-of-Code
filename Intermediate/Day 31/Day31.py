BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *
import pandas
import random

#-----------------Generate Words-------------#
try:
    vocab = pandas.read_csv(".\Intermediate\Day 31\\words_to_learn.csv")
except FileNotFoundError:
    vocab = pandas.read_csv(".\Intermediate\Day 31\\Russian.csv")
finally:
    vocab_dict = vocab.to_dict(orient = "records")

entry = None

def generate_word():
    global entry, flip_timer
    window.after_cancel(flip_timer)
    entry = random.choice(vocab_dict)
    word = entry["Russian"]
    canvas.itemconfig(current_title, text = "Russian", fill = "black")
    canvas.itemconfig(current_word, text = word, fill = "black")
    canvas.itemconfig(card, image = card_front)
    flip_timer = window.after(3000, flip_card)

#---------------Flip card---------------------#

def flip_card():
    canvas.itemconfig(card, image = card_back)
    canvas.itemconfig(current_title, text = "English", fill = "white")
    canvas.itemconfig(current_word, text = entry["English"] , fill = "white")

#------------Save Progress------------------#

def correct():
    vocab_dict.remove(entry)
    words_to_learn = pandas.DataFrame(vocab_dict)
    words_to_learn.to_csv(".\Intermediate\Day 31\words_to_learn.csv", index = False)

    generate_word()
 

# --------------------UI--------------------#
window = Tk()
window.title("Russian Flash Cards")
window.config(padx = 50, pady = 50, bg = BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)


canvas = Canvas(width = 800, height = 526, bg = BACKGROUND_COLOR, highlightthickness = 0)
card_front = PhotoImage(file = ".\Intermediate\Day 31\card_front.png")
card_back = PhotoImage(file = ".\Intermediate\Day 31\card_back.png")
card = canvas.create_image(400, 263, image = card_front)

current_title = canvas.create_text(400, 150, text = "", font = ("Arial", 40, "italic"))
current_word = canvas.create_text(400, 263, text = "", font = ("Arial", 60, "italic"))

canvas.grid(column = 0, row = 0, columnspan = 2)

tick_img = PhotoImage(file = ".\Intermediate\Day 31\\right.png")
tick_button = Button(image = tick_img, highlightthickness = 0, command = correct)
tick_button.grid(column = 1, row = 1)

cross_img = PhotoImage(file = ".\Intermediate\Day 31\\wrong.png")
cross_button = Button(image = cross_img, highlightthickness = 0, command = generate_word)
cross_button.grid(column = 0, row = 1)

generate_word()


window.mainloop()