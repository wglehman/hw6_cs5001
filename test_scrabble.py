import random
import wordlist

LENGTH = 7
POINTS = {1: ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R'],
          2: ['D', 'G'],
          3: ['B', 'C', 'M', 'P'],
          4: ['F', 'H', 'V', 'W', 'Y'],
          5: ['K'],
          8: ['J', 'X'],
          10: ['Q', 'Z']}


def draw():
    word_list = wordlist.unpack()

    letters = []

    idx = random.sample(range(0, len(word_list) - 1), LENGTH)

    for i in idx:
        letters += [word_list[i]]

    print(letters)

    wordlist.repack(letters)

    return letters


def play(letters):
    for letter in letters:
        print(letter + '', end='')

    total_points = []

    word = input('\nWhat\'s your word? ')

    for char in word:
        if char in letters:
            total_points += [k for k, v in POINTS.items() if char in v]
        else:
            print(char, 'not in the drawn letters. you lose.')
            return []

    print(sum(total_points))
    return [word, sum(total_points)]


def print_words(words):
    total_points = []

    for i in range(1, len(words), 2):
        total_points += [words[i]]

    print('You have a total of', sum(total_points), 'points so far!')

    for i in range(0, len(words), 2):
        print(words[i], '--', words[i + 1], 'points')


def menu():
    choice = ''
    letters = []
    words = []

    while choice != 'Q':
        choice = input('D: Draw from bag\n'
                       'W: Make a word\n'
                       'P: Print words made so far\n'
                       'Q: QUIT\n').upper()

        if choice == 'D':
            letters = draw()

        elif choice == 'W':
            words += play(letters)

        elif choice == 'P':
            print_words(words)


menu()
