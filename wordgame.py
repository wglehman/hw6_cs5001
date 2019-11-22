"""
    will lehman
    cs5001-02
    fall 2019
    11/21/2019
    hw6

    wordgame.py
"""

from scrabble_points import *
from wordlist import get_wordlist
import random


NUM_LETTERS = {'E': 12, 'A': 9, 'I': 9, 'O': 8, 'N': 6, 'R': 6, 'T': 6,
               'D': 4, 'L': 4, 'S': 4, 'U': 4, 'G': 3, 'B': 2, 'C': 2, 'F': 2,
               'H': 2, 'M': 2, 'P': 2, 'V': 2, 'W': 2, 'Y': 2, '':2, 'J': 1,
               'K': 1, 'Q': 1, 'X': 1, 'Z': 1}

POINTS = {1: ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R'],
          2: ['D', 'G'],
          3: ['B', 'C', 'M', 'P'],
          4: ['F', 'H', 'V', 'W', 'Y'],
          5: ['K'],
          8: ['J', 'X'],
          10: ['Q', 'Z']}


def play(letters, wordlist, games):
    '''
        function: play
              in: letters (string of 7 drawn letters),
                  wordlist (list of strings of possible words),
                  games (dict of words played with points won)
             out: nothing
            does: checks to see if word user inputs is valid (hasn't been
                  guessed already, the tiles are in play, and the word is
                  in the wordlist). sends to get_points if determined valid
                  to calculate point value. saves word and points to dict.
    '''
    # user input
    word = input('what\'s your word? ').upper()

    # checks if word in wordlist, if it isn't errors and returns
    if word not in wordlist:
        print('word invalid, no points gained.')
        return

    # checks letters for the number of blank tiles, saves int val for check
    num_blanks = len([char for char in letters if char == ''])

    # splits up word if the letters have a blank tile, skips the "missing"
    # tile, elif, errors and returns
    for char in word:
        if char not in letters and num_blanks != 0:
            num_blanks -= 1
        elif char not in letters and num_blanks == 0:
            print('the letter', char, 'isn\'t in play')
            return

    # checks to see if words played, if yes errors and returns
    if word in games.keys():
        print('you\'ve already played that')
        return

    # calls get points to get points
    points = get_points(word)

    # creates dict entry for word with point value
    games[word] = points


def get_points(word):
    '''
        function: get points
              in: word (string)
             out: points (integer)
            does: converts letters to their summed point value using constant
                  vals for point values. returns overall points
    '''
    # init points
    points = 0

    # unpack word, compare to vals in points dict add key from that dict
    # (point value) if theres a match
    for char in word:
        for k, v in POINTS.items():
            for letter in v:
                if letter == char:
                    points += k

    return points


def draw(bag):
    '''
        function: draw
              in: bag (list of strings)
             out: letters (list of strings)
            does: takes in a bag of letters and draws 7 random letters from the
                  bag using sample and indices. removes the letters after
                  choosing them.
    '''
    letters = []

    # makes a list of 7 random indices from 0 to the length of the bag - 1
    # (0 - index list)
    idx = random.sample(range(0, len(bag) - 1), 7)

    # adds letter at index i to the bag
    for i in idx:
        letters += [bag[i]]

    # removes letters based on value from the bag
    for letter in letters:
        bag.remove(letter)

    return letters


def main():
    # games dict saves all games for printing
    games = {}
    # the 7 letters drawn
    letters = []
    # the bag of letters, created based on the constant NUM_LETTERS
    bag = bag_of_letters(NUM_LETTERS)
    # wordlist call to import its unpacked list
    wordlist = get_wordlist()

    # choice init
    choice = ''
    # constantly asks user for input until Q or correct input, upper()s input
    while choice != 'Q':
        choice = input('D - draw 7 letters\n'
                       'W - make a word from the letters\n'
                       'P - print the words so far\n'
                       'Q - QUIT\n').upper()

        # D choice for draw, checks to see if the bag has 7 (enough for a draw)
        if choice == 'D' and len(bag) >= 7:
            letters = draw(bag)
            print('you drew', letters)

        # error message for if the bag has less than 7 tiles
        elif choice == 'D' and len(bag) < 7:
            print('less than 7 letters left in the bag. make another choice')

        # checks to see if letters have been drawn, if not error, if yes
        # calls the play func
        elif choice == 'W':
            if letters == []:
                choice = ''
                print('in order to make a word, you need to draw (D)\n'
                      'try again\n')
            else:
                play(letters, wordlist, games)

        # prints the sum of the values in games (all points)
        # then unpacks the dict to show each answer and point valus
        elif choice == 'P':
            print('you have a total of', sum(games.values()))
            for k, v in games.items():
                print(k, '--', v, 'POINTS')

        # if bag is empty or out of letters, prints and quits
        elif len(bag) == 0 or len(letters) == 0:
            print('you\'ve run out of tiles!')
            print('you have a total of', sum(games.values()))
            for k, v in games.items():
                print(k, '--', v, 'POINTS')
            quit()


main()
