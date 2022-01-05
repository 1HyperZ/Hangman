HANGMAN_PHOTOS = {"picture 1" : '''x-------x''', "picture 2" : '''
    x-------x
    |
    |
    |
    |
    |''', 'picture 3' : '''
    x-------x
    |       |
    |       0
    |
    |
    |
''', 'picture 4' : '''
    x-------x
    |       |
    |       0
    |       |
    |
    |''', 'picture 5' : '''
    x-------x
    |       |
    |       0
    |       |
    |
    |''', 'picture 6' : r''' 
    x-------x
    |       |
    |       0
    |      /|\
    |      / \
    |''' , 'picture 7' : r''' 
    x-------x
    |       |
    |       0
    |      /|\
    |      / \
    |'''}
def print_hangman(num_of_tries):
    if num_of_tries == 1:
        return(HANGMAN_PHOTOS["picture 1"])
    elif num_of_tries == 2:
        return(HANGMAN_PHOTOS["picture 2"])
    elif num_of_tries == 3:
        return(HANGMAN_PHOTOS["picture 3"])
    elif num_of_tries == 3:
        return(HANGMAN_PHOTOS["picture 4"])
    elif num_of_tries == 4:
        return HANGMAN_PHOTOS["picture 4"]
    elif num_of_tries == 5:
        return(HANGMAN_PHOTOS["picture 5"])
    elif num_of_tries == 6:
        return(HANGMAN_PHOTOS["picture 6"])
    elif num_of_tries == 7:
        return(HANGMAN_PHOTOS["picture 7"])

num_of_tries = 6
print(print_hangman(num_of_tries))







