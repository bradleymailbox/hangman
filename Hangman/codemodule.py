import random
# variables
dict = "words.txt"

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
    return random.randint(0,max-1)

#print the word
def printWord(compword, guessed_letters):
    for g in compword:
        if g not in guessed_letters:
            compword = compword.replace(g, "#")        
    return compword

def print_guesses(gl):
    for ele in enumerate(gl): 
        print ele 
    