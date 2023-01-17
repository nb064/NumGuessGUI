import tkinter as tk
import random as rand
from engines import audioplayer

playable = True
num = rand.randrange(1, 100)

def hint():
    if playable:
        global hints

        if hints > 0:
            if hints == 2:
                text.config(text="The number is somewhere between " + str(num - rand.randint(3, 8)) + " and " + str(num + rand.randint(3, 8)) + ".")
            elif hints == 1:
                text.config(text="The number is somewhere between " + str(num - rand.randint(2, 5)) + " and " + str(num + rand.randint(2, 5)) + ".")

            hints -= 1
            hintText.config(text="Hints: " + str(hints))

def guess(guess):
    global playable
    if playable:
        global guesses
        guesses -= 1
        guessText.config(text="Guesses: " + str(guesses))

        if num == guess:
            text.config(text="Impossible! You got it correct!")
            playable = False
        else:
            text.config(text="Try again.")

def click():
    if playable:
        if guesses > 0:
            global numGuess
            try:
                numGuess = int(guesser.get())
                print(numGuess)
                guess(numGuess)
            except ValueError:
                print("Error getting a valid int value from the text field.")
        else:
            text.config(text="Out of guesses! Better luck next time...")

win = tk.Tk()
win.title("NumGuessGUI")
win.geometry('400x300')
win.resizable(False, False)

guesses = 5
hints = 2

guessText = tk.Label(win, text="Guesses: " + str(guesses))
guessText.pack()
guessText.place(x=30, y=5, anchor='center')

text = tk.Label(win, text = "I'm thinking of a number between 1-100, give it a guess.")
text.pack()
text.place(x=200, y=100, anchor='center')

guesser = tk.Entry(win)
guesser.pack()
guesser.place(x=200, y=125, anchor='center')

submit = tk.Button(win, text="Submit", command=click)
submit.pack()
submit.place(x=200, y=160, anchor='center')

hintButton = tk.Button(win, text="Hint", command=hint)
hintButton.pack()
hintButton.place(x=360, y=0)

hintText = tk.Label(win, text="Hints: " + str(hints))
hintText.pack()
hintText.place(x=350, y=25)

win.mainloop()
