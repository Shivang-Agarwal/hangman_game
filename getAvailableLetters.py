lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
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
