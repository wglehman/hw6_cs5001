"""
    will lehman
    cs5001-02
    fall 2019
    11/21/2019
    hw6

    scrabble_points.py
"""


def bag_of_letters(num_letters):
    '''
        function: bag of letters
              in: number of letters (dict with letter key and # val)
             out: list of those letters repeated
            does: "unpacks" the bag and creates a list based on their frequency
    '''
    # initializes letters list
    letters = []

    # unpacks dict adding the correct frequency of letter to new string
    for k, v in num_letters.items():
        letters += [k] * v

    # returns string to other function
    return letters


def get_word_value(word, value):
    '''
        function: get word value
              in: word (string),
                  value (dict)
             out: points for that word based on the value dict
            does: checks to see how many points a string is worth
    '''
    # init points
    points = 0

    # splits up word, if matched in value dict, adds the key to the points
    for char in word.upper():
        if value.get(char) is not None:
            points += value.get(char)

    return points
