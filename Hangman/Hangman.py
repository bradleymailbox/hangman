# DEVELOPER: Bradley Stevens
# DATE: 2019
# ABOUT: classic game of hangman
import os
import codemodule as cm
import printmodule as pm
import ascii_print as ap

pm.printmsg(0)
# initialize variables
letter =""
numguesses = 5
totalwords = 0
compword = ""
guessed_letters = []
words = []
hashedword = ""
alphabet = 'abcdefghijklmnopqrstuvwxyz'
game_end = False
answer = ''
counter = 0
# get the words and count
words = cm.getwords()
totalwords = len(words)
try:
    # get a random word from the data file
    compword = words[cm.getRandomValue(totalwords)]
    # print compword
    # loop through the number of times user can guess
    while numguesses <> 0:

        #display the word guesssed state
        hashedword = cm.printWord(compword, guessed_letters)
        pm.print_guesses(13,hashedword)
        counter = hashedword.count('#')
        # if all letters have been guessed
        if counter == 0: 
            game_end = True
        else:
            # give the user the opportunity to guess
            pm.printmsg(1)
            letter= raw_input().lower()


            # check if letter guessed
            if len(letter) != 1:
                pm.printmsg(10)
            elif letter not in alphabet:
                pm.printmsg(10)
            elif letter in guessed_letters:
                pm.printmsg(2)
            else:
         # if the letter entered is not in the list then increment the number of guesses  
                if letter in compword:
                    pm.printmsg(5)
                else:
                    numguesses = numguesses - 1
                    if numguesses == 0: game_end = True
                    pm.printmsg(6)
                    ap.print_hangman(numguesses)
                # add the letter to the list of letters    
            guessed_letters.append(letter)
            cm.print_guesses(guessed_letters)
            pm.print_guesses(4, numguesses)
        # end the game
        if game_end == True:
            if numguesses > 0: 
                pm.printmsg(7) 
            else: 
                pm.printmsg(8)
            
            pm.print_guesses(9, compword)
            answer = ''
            #prompt for restart
            while answer not in ['y','n']:
                print "Do you wish to try again?y/n"
                answer = raw_input()
                if answer == 'y':
                    os.system('cls')
                    pm.printmsg(0)
                    game_end = False
                    guessed_letters = []
                    numguesses = 5
                    compword = words[cm.getRandomValue(totalwords)]
                    counter = 0
                    #print compword
                    break
                else:
                    pm.printmsg(12) 
                    break  
except: 
    pm.printmsg(11)
  

    
    
