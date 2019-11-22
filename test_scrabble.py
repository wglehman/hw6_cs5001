'''
    CS5001
    Fall 2019
    Test suite -- testing two scrabble functions
'''

from scrabble_points import bag_of_letters
from scrabble_points import get_word_value

def test_make_bag(input_freq, expected):
    ''' Function test_make_bag
        Input: a dictionary (input to the function), a list of strings
                (expected output)
        Returns: True if expected == actual, false otherwise
    '''
    print('Testing', input_freq, 'expecting', expected)
    actual = bag_of_letters(input_freq)
    if actual == expected:
        print('...SUCCESS!\n')
        return True
    else:
        print('...FAIL :(\n')
        return False

def test_word_value(word, values, expected):
    ''' Function test_word_value
        Input: a word (string), letter-to-value mapping (dictionary),
                and the word's expected value (int)
        Returns: True if expected == actual, false otherwise
    '''
    print('Testing', word, 'expecting', expected)
    actual = get_word_value(word, values)
    if actual == expected:
        print('...SUCCESS!\n')
        return True
    else:
        print('...FAIL :(\n')
        return False


def run_bag_tests():
    ''' Function run_bag_tests
        Input: nothing
        Returns: an int, number of tests that failed.
        Does: repeatedly calls test_make_bag on varied inputs,
              and validates that result is what we expected.
    '''
    num_failed = 0
    if not test_make_bag({'A':1}, ['A']):
        num_failed += 1
    if not test_make_bag({}, []):
        num_failed += 1
    if not test_make_bag({'A':2}, ['A', 'A']):
        num_failed += 1
    if not test_make_bag({'A':1, 'Z':3}, ['A', 'Z', 'Z', 'Z']):
        num_failed += 1
    if not test_make_bag({'B':1, 'M':2, 'P':3}, ['B', 'M', 'M', 'P', 'P', 'P']):
        num_failed += 1
    if not test_make_bag({'Z':1, 'Y':1, 'X':1}, ['Z', 'Y', 'X']):
        num_failed += 1

    return num_failed

def run_word_tests():
     ''' Function run_word_tests
         Input: nothing
         Returns: an int, number of tests that failed.
         Does: repeatedly calls test_word_value on varied inputs,
              and validates that result is what we expected.
    '''
     num_failed = 0
     if not test_word_value('A', {'A':1}, 1):
         num_failed += 1
     if not test_word_value('A', {'B':1}, 0):
         num_failed += 1
     if not test_word_value('a', {'A':1}, 1):
         num_failed += 1
     if not test_word_value('7', {'A':1}, 0):
         num_failed += 1
     if not test_word_value('BAT', {'A':1, 'B':2, 'T':2}, 5):
         num_failed += 1
     if not test_word_value('AIQY', {'A':1, 'B':2, 'I':1, 'Q':10, 'Y':4}, 16):
         num_failed += 1
     return num_failed


def main():
    print('Beginning test suite. Testing bag_of_letters first...')
    fails = run_bag_tests()
    if fails > 0:
        print('Something went wrong, pls go back and fix.')

    print('Testing word values...')
    fails += run_word_tests()
    if fails > 0:
        print('Something went wrong, pls go back and fix.')

    if fails == 0:
        print('ALL TESTS PASSED!!')

main()




        
