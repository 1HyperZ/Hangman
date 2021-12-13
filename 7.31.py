def show_hidden_word(secret_word, old_letters_guessed):
    for x in secret_word:
        if x not in old_letters_guessed:
            print("_", end=" ")
        else:
            print(x, end=" ")


secret_word = "mammals"
old_letters_guessed = ['s', 'p', 'j', 'i', 'm', 'k']
print(show_hidden_word(secret_word, old_letters_guessed))
