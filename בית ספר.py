import random

HANGMAN_ASCII_ART = r'''Welcome to the game Hangman.                       
    _    _
   | |  | |
   | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
   |  __  |/ _' | '_ \ / _' | '_ ' _ \ / _' | '_ \
   | |  | | (_| | | | | (_| | | | | | | (_| | | | |
   |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                        __/ |
                       |___/ '''

MAX_TRIES = 6







#print('Mission 1.4.1')


print(HANGMAN_ASCII_ART)

print("Max tries: ", MAX_TRIES)

word = input('Please enter a word: ')
word_length = len(word)
print('_' * word_length)

the_letter = input('Guess a letter: ',)
if not the_letter.isalpha():
    print('E2')
elif len(the_letter) > 1:
    print('E1')
elif the_letter.isalpha():
    print(the_letter.lower())



#print('Mission 1.4.2')




print('''x-------x''')



print('''x-------x
    |
    |
    |
    |
    |''')



print('''x-------x
    |       |
    |       0
    |
    |
    |
''')

print('''x-------x
    |       |
    |       0
    |       |
    |
    |''')

print(r''' x-------x
    |       |
    |       0
    |      /|\
    |
    |''')

print(r''' x-------x
    |       |
    |       0
    |      /|\
    |      /
    |''')

print(r''' x-------x
    |       |
    |       0
    |      /|\
    |      / \
    |''')





