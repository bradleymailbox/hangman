# DEVELOPER: Bradley Stevens
# DATE: 2019
# ABOUT: classic game of hangman

import codemodule as cm

cm.printmsg(0)

# initialize variables
letter =""
numguesses = 0
totalwords = 0
compword = ""
# empty lists
guessed_letters = []
words = []
# get the words and count
words = cm.getwords()
totalwords = len(words)
# get a random word from the data file
compword = words[cm.getRandomValue(totalwords)]

# loop through the number of times user can guess
while numguesses < 5:
    #display the current message
    print cm.printWord(compword, guessed_letters)
    # give the user the opportunity to guess
    cm.printmsg(1)
    letter= raw_input()
    # check if the user has guessed the currrent letter
    if letter in guessed_letters:
        cm.printmsg(2)
    else:
        guessed_letters.append(letter)
        cm.printmsg(3)
  
    # if the letter entered is not in the list then increment the number of guesses

    # add the letter to the list of wrong letters
    
    # else 
    # build the list of correct guesses
    # display the word with the letters guessed
