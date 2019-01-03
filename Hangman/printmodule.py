
# list of messages that can be displayed
msgs = ['### W E L C O M E  T O  H A N G M A N ###\n'
        '-----------------------------------------',       #0
        'Please enter a letter you wish to guess:',       #1
        'You have already guessed that letter',           #2
        'Validating the letter entered',                  #3
        'Number of guesses left:',                        #4
        'Great! You have found a letter of the word!',     #5
        'Sorry the letter guessed is not part of the word',#6
        'Well done! You have guessed the entire word!',   #7 
        'Sorry! You did not guess the word',              #8
        'The correct word was ',                          #9
        'Please enter single letter of the alphabet.',    #10 
        'An error occurred please restart the program',   #11
        'Good bye! Thanks for Playing                ',   #12
        'HIDDEN WORD:'    #13
]
# display a message from the msgs list
def printmsg(m):
    print msgs[m]

# print the number of guesses the user has made
def print_guesses(msgno, val):
    print msgs[msgno] + str(val)
        
    