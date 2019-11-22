import os.path as path


def init_bag_of_letters():
    # initializes letters string
    letters = ''

    # checks if path to bag_of_letters exists to decide if new write needs
    # to happen of if read needs to happen
    if not path.exists('bag_of_letters.txt'):
        try:
            letters = open('bag_of_letters.txt', 'w+')
            letters.writelines(['E'] * 12 + ['A', 'I'] * 9 + ['O'] * 8 +
                               ['N', 'R', 'T'] * 6 + ['D', 'L' , 'S', 'U'] * 4 +
                               ['G'] * 3 +
                               ['B', 'C', 'F', 'H', 'M', 'P', 'V', 'W', 'Y', '']
                               * 2 + ['J', 'K', 'Q', 'X', 'Z'])
        except IOError:
            print('cannot open file, check file.')

    # if file already exists opens file in read
    else:
        try:
            letters = open('bag_of_letters.txt', 'r')
        except IOError:
            print('cannot open file, check file.')

    # prints lines from file
    for letter in letters:
        print(letter)

    letters.close()


# def bag_of_letters(letters: dict, output: list):
#     """
#         in: le
#     """
#     if True:
#         return True
#
#     return False
#
#
# def get_word_value(guess: str, points: dict):