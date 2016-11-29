# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "C:/Users/avs/6.00.1x Files/HangMan/words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    count = 0
    for i in lettersGuessed:
        if i in secretWord:
            count +=1
    return count == len(secretWord)        



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    secretWord = list(secretWord)
    for i in range(len(secretWord)):
        if ( (secretWord[i] in lettersGuessed)==False ):
            secretWord[i] = '_ '
    return "".join(secretWord)


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    import string
    List = list(string.ascii_lowercase)
    for i in range(len(lettersGuessed)):
        if lettersGuessed[i] in List:
            List.remove(lettersGuessed[i])
    return ''.join(List)       

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    import string
    print 'Welcome to the game, of Hangman!'
    print 'I am thinking of a word that is ' + str(len(secretWord)) + ' letters long.'
    print '-----------'
    guess = 8
    i=0
    #print 'You have 8 guesses left.'
    lettersGuessed = ['0']
    index = len(secretWord)
    while guess>1 :
        
        if i==0 or (lettersGuessed[i] in secretWord) or (lettersGuessed[i] in lettersGuessed[:i]) :
            print 'You have ' + str(guess) + ' guesses left.'
        else:       
            guess-=1
            print 'You have ' + str(guess) + ' guesses left.'
            
        if i==0 :
            print 'Available letters: ' + string.ascii_lowercase
        else :
            print 'Available letters: ' + getAvailableLetters(lettersGuessed)
                 
        input1  = raw_input("Please guess a letter: " ).lower()
        lettersGuessed.append(input1)
        
        if (lettersGuessed[i+1] in secretWord) and (lettersGuessed[i+1] not in lettersGuessed[:i+1]) :
            print 'Good guess: ' + getGuessedWord(secretWord, lettersGuessed)
            print '-----------'
        elif lettersGuessed[i+1] in lettersGuessed[:i+1] :
            print "Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed)
            print '-----------'
        else:
            print 'Oops! That letter is not in my word: ' + getGuessedWord(secretWord, lettersGuessed)
            print '-----------'
        i += 1
        index -= 1       
        if guess == 1 and isWordGuessed(secretWord, lettersGuessed)==False:
            print 'Sorry, you ran out of guesses. The word was ' + secretWord
            
        else:
            if guess>0 and isWordGuessed(secretWord, lettersGuessed):
                print 'Congratulations, you won!'
                break
                  
                          




# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
#secretWord = 'apple'
hangman(secretWord)
