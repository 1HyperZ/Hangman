def check_win(secret_word, old_letters_guessed):
    aviv = 0
    for x in secret_word:
        if x not in old_letters_guessed:
            aviv = 1
        else:
            pass

    if aviv == 1:
        return "False"
    else:
        return "True"

secret_word = "yes"
old_letters_guessed = ['d', 'g', 'e', 'i', 's', 'k', 'y']
print(check_win(secret_word, old_letters_guessed))