import random
import tkinter as tk
import pandas

# Creating window
window = tk.Tk()
# Reading our spanish data
data = pandas.read_csv('data/Spanish_Practice.csv')
spanish_word_list = [row.Spanish for _, row in data.iterrows()]
english_word_list = [row.English for _, row in data.iterrows()]
length_of_spanish_list = len(spanish_word_list)
length_of_english_list = len(english_word_list)
index_for_spanish = index_for_english = random.randint(0, length_of_english_list - 1)


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


# -------------------------------------CHANGING OF WORD------------------------------------
def change_word():
    canvas.itemconfig(spanish_word_display, text=spanish_word_list[index_for_spanish])


# -------------------------------------KNOWN BUTTON FUNCTIONALITY------------------------------------
def known():
    global spanish_word_list, index_for_spanish
    if len(spanish_word_list) == 0:
        canvas.itemconfig(spanish_word_display, text='Completed🥳🎉')
    else:
        spanish_word_list.pop(index_for_spanish)
        if len(spanish_word_list) == 0:
            canvas.itemconfig(spanish_word_display, text='Completed🥳🎉')
        else:
            index_for_spanish = random.randint(0, len(spanish_word_list) - 1)
            change_word()


# -------------------------------------UNKNOWN BUTTON FUNCTIONALITY------------------------------------
def unknown():
    global spanish_word_list
    if len(spanish_word_list) != 0:
        spanish_word_list.append(spanish_word_list.pop(index_for_spanish))
        change_word()


# ------------------------------UI-----------------------------------------
window.title(NAME)
# window.minsize(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
window.config(bg=WINDOW_BG_COLOR, padx=WINDOW_PAD_X, pady=WINDOW_PAD_Y)

# Initializing of image path
card_front_img = tk.PhotoImage(file='images/card_front.png')
unknown_button_img = tk.PhotoImage(file='images/wrong.png')
known_button_img = tk.PhotoImage(file='images/right.png')

# All Stuff related to canvas
canvas = tk.Canvas(width=CARD_IMAGE_WIDTH, height=CARD_IMAGE_HEIGHT, highlightthickness=0, bg=WINDOW_BG_COLOR)
canvas.create_image(CARD_IMAGE_WIDTH // 2, CARD_IMAGE_HEIGHT // 2, image=card_front_img)
canvas.create_text(CARD_IMAGE_WIDTH // 2, CARD_IMAGE_HEIGHT // 2 - 150, text='Spanish', font=FONT_FOR_TITLE)
spanish_word_display = canvas.create_text(CARD_IMAGE_WIDTH // 2, CARD_IMAGE_HEIGHT // 2,
                                          text=spanish_word_list[index_for_spanish],
                                          font=FONT_FOR_WORD)

# Creating Button
unknown_button = tk.Button(image=unknown_button_img, command=unknown)
known_button = tk.Button(image=known_button_img, command=known)

# Positioning
canvas.grid(row=0, column=0, columnspan=3)
unknown_button.grid(row=1, column=0)
known_button.grid(row=1, column=2)
# For window to appear continuously
window.mainloop()
