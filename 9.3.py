def choose_word(file_path, index):
    with open(file_path, 'r') as words_file:
        words = words_file.read()
    words = words.split()
    length_of_words = len(words)
    while index > length_of_words:
        index -= length_of_words
    word = words[index - 1]
    sorted_words = sorted(list(set(words)), key=words.index)
    length_of_sorted_words = len(sorted_words)
    return (length_of_sorted_words, word.lower())


print(choose_word(r"C:\Users\omerz\Desktop\New folder (2)\words.txt", 15))