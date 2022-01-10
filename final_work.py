old_letters_guessed = ['a', 'b', 'c']
def check_valid_input(letter_guessed, old_letters_guessed):
    #The function examines whether the character entered is correct
    if not letter_guessed.isalpha():
        print('false')
    elif len(letter_guessed) > 1:
        print('false')
    elif letter_guessed.lower() in old_letters_guessed or letter_guessed.upper() in old_letters_guessed:
        print("false")
    elif len(letter_guessed) == 1 and letter_guessed.isalpha and (letter_guessed.lower() not in old_letters_guessed or letter_guessed.upper() not in old_letters_guessed):
        print('true')
    else:
        print("error")
