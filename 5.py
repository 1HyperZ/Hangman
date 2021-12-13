def is_valid_input(letter_guessed):
    if not letter_guessed.isalpha():
        print('false')
    elif len(letter_guessed) > 1:
        print('false')
    elif len(letter_guessed) == 1 and letter_guessed.isalpha:
        print('true')


is_valid_input('app$')
