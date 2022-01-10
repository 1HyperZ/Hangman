def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    if len(letter_guessed) > 1 or not letter_guessed.isalpha() or letter_guessed in old_letters_guessed:
        print("X")
        print(" -> ".join((sorted(old_letters_guessed))))
        return False
    else:
        old_letters.append(letter_guessed)
        return True



old_letters = ['a', 'p', 'c', 'f', 's', 'd']
print(try_update_letter_guessed('d', old_letters))

