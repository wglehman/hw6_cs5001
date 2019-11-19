def unpack():
    try:
        file = open('wordlist.txt', 'r')

        word_list = []

        for word in file:
            word_list = eval(word)

        file.close()

        return word_list

    except FileNotFoundError:
        print('file not found')
        return


def repack(letters_drawn):
    word_list = unpack()

    for val in letters_drawn:
        word_list.remove(val)

    try:
        file_write = open('wordlist_write.txt', 'w')

        file_write.write(str(word_list))

        file_write.close()

        return word_list

    except FileNotFoundError:
        print('file not found')
        return
