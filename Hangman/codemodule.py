import random
# variables
dict = "words.txt"
msgs = ['Welcome to Hangman - Lets play a round',
        'Please enter a letter you wish to guess:',
        'You have already guessed that letter',
        'Validating the letter entered',
        'Number of guesses made:',
        'Oops the letter guessed is not part of the word'
    
]
# display a message from the msgs list
def printmsg(m):
    print msgs[m]

# print the number of guesses the user has made
def print_guesses(x):
    print msgs[m]

# get the list of words
def getwords():
    words = []
    with open(dict) as file:
        for line in file: 
            line = line.strip() #or some other preprocessing
            words.append(line) 
    return words

# get a random value : maximum passed 
def getRandomValue(max):
    return random.randint(1,max)

#print the word
def printWord(compword, guessed_letters):
    for g in compword:
        if g not in guessed_letters:
            compword = compword.replace(g, "#")        
    return compword
    
    