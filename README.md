# NumGuessGUI
A simple python GUI that lets the user guess a number between 1-100. Includes a sound engine.
## Program
The program uses `tkinter` and `random`. It is broken down into 3 functions.

`hint()` is where the programming for the hint button is stored.\
`guess()` is where the program handles the user's guessed number input.\
`click()` is basically where the program checks if the user input something valid, then plugs that into `guess()`.

## Sound engine
The sound engine uses the `playsound` module. It is simply used by typing `audioplayer.Play()` and putting in the 2 parameters.
The parameters include the directory, which searches in the folder of the `main.py` file, and the block parameter.

Example code:
```
audioplayer.Play('/sounds/example.wav', False)
```

This code will search the directory of the program for a folder called "sounds", and then search for "example.wav".
