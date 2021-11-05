import random
import tkinter as tk
import pandas

# Creating window
window = tk.Tk()
# Reading our spanish data

try:
    data = pandas.read_csv('Data/Words_to_learn.csv')
except (FileNotFoundError, pandas.errors.EmptyDataError):
    data = pandas.read_csv('Data/Spanish_Practice.csv')

to_learn = data.to_dict(orient='records')
current_card = random.choice(to_learn)

# ------------------------------CONSTANT---------------------------------
NAME = 'Flasher'
WINDOW_WIDTH = 700
WINDOW_HEIGHT = 500
WINDOW_BG_COLOR = '#B1DDC6'
WINDOW_PAD_X = 50
WINDOW_PAD_Y = 50
CARD_IMAGE_WIDTH = 800
CARD_IMAGE_HEIGHT = 526
FONT_FOR_TITLE = ('Arial', 30, 'italic')
FONT_FOR_WORD = ('Arial', 50, 'bold')
LENGTH_OF_WORD_LIST = len(to_learn)
FLIP_TIME = 3000


def flip_card():
    canvas.itemconfig(canvas_img, image=card_back_img)
    canvas.itemconfig(canvas_title, text='English', fill='white')
    canvas.itemconfig(canvas_word, text=current_card['English'], fill='white')


flip_timer = window.after(FLIP_TIME, flip_card)


# -------------------------------------KNOWN BUTTON FUNCTIONALITY------------------------------------
def known():
    global current_card
    if to_learn:
        to_learn.remove(current_card)
        new_data = pandas.DataFrame(to_learn)
        new_data.to_csv("Data/Words_to_learn.csv", index=False)
        unknown()
    else:
        canvas.itemconfig(canvas_word, text='Completed🥳🎉')
    known_word.config(text=f'Known Words {LENGTH_OF_WORD_LIST - len(to_learn)}')


# -------------------------------------UNKNOWN BUTTON FUNCTIONALITY------------------------------------
def unknown():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    if to_learn:
        current_card = random.choice(to_learn)
        canvas.itemconfig(canvas_img, image=card_front_img)
        canvas.itemconfig(canvas_title, text='Spanish', fill='black')
        canvas.itemconfig(canvas_word, text=current_card['Spanish'], fill='black')
        flip_timer = window.after(FLIP_TIME, flip_card)
    else:
        canvas.itemconfig(canvas_word, text='Completed🥳🎉')
    unknown_words.config(text=f'Unknown Words {len(to_learn)}')


# ------------------------------UI-----------------------------------------
window.title(NAME)
# window.minsize(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
window.config(bg=WINDOW_BG_COLOR, padx=WINDOW_PAD_X, pady=WINDOW_PAD_Y)

# Initializing of image path
card_front_img = tk.PhotoImage(file='images/card_front.png')
card_back_img = tk.PhotoImage(file='images/card_back.png')
unknown_button_img = tk.PhotoImage(file='images/wrong.png')
known_button_img = tk.PhotoImage(file='images/right.png')

# All Stuff related to canvas
canvas = tk.Canvas(width=CARD_IMAGE_WIDTH, height=CARD_IMAGE_HEIGHT, highlightthickness=0, bg=WINDOW_BG_COLOR)
canvas_img = canvas.create_image(CARD_IMAGE_WIDTH // 2, CARD_IMAGE_HEIGHT // 2, image=card_front_img)
canvas_title = canvas.create_text(CARD_IMAGE_WIDTH // 2, CARD_IMAGE_HEIGHT // 2 - 150, text='Spanish',
                                  font=FONT_FOR_TITLE)
canvas_word = canvas.create_text(CARD_IMAGE_WIDTH // 2, CARD_IMAGE_HEIGHT // 2,
                                 text=current_card['Spanish'],
                                 font=FONT_FOR_WORD)

# Creating Labels
unknown_words = tk.Label(text=f'Unknown Words {len(to_learn)}', font=('Arial', 15), bg=WINDOW_BG_COLOR)
known_word = tk.Label(text=f'Known Words {0}', font=('Arial', 15), bg=WINDOW_BG_COLOR)
# Creating Button
unknown_button = tk.Button(image=unknown_button_img, command=unknown)
known_button = tk.Button(image=known_button_img, command=known)

# Positioning
canvas.grid(row=1, column=0, columnspan=3)
unknown_words.grid(row=0, column=0)
known_word.grid(row=0, column=2)
unknown_button.grid(row=2, column=0)
known_button.grid(row=2, column=2)
# For window to appear continuously
window.mainloop()
