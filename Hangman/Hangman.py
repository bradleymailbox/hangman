# DEVELOPER: Bradley Stevens
# DATE: 2019
# ABOUT: classic game of hangman

import codemodule

codemodule.printmsg(0)

# initialize variables
letter =""
numguesses = 0

# empty lists
guessed_letters = []
correct_letters = []
wrong_letters = []

while numguesses < 5:
    # give the user the opportunity to guess
    codemodule.printmsg(1)
    letter= input()
    # check if the user has guessed the currrent letter
    if letter in guessed_letters:
        codemodule.printmsg(2)
    else:
        guessed_letters.append(letter)
        codemodule.printmsg(3)
  
    # if the letter entered is not in the list then increment the number of guesses

    # add the letter to the list of wrong letters
    
    # else 
    # build the list of correct guesses
    # display the word with the letters guessed
