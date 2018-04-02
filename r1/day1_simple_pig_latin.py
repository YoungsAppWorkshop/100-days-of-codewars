#!/usr/bin/env python3
"""
    Simple Pig Latin - 5 kyu
        Move the first letter of each word to the end of it,
        then add "ay" to the end of the word.
        Leave punctuation marks untouched.

    https://www.codewars.com/kata/520b9d2ad5c005041100000f/train/python
"""


# My Solution
def pig_it(text):
    char = None
    str = ''
    for letter in text:
        if letter.isalpha():
            if char is None:
                char = letter
            else:
                str += letter
        else:
            if char is None:
                str += letter
            else:
                str += char + 'ay' + letter
                char = None
        print('letter: {} \tis_alpha: {}'.format(letter, letter.isalpha()))
    if char is not None:
        str += char + 'ay'
    return str


# Best Practice
# import re
# def pig_it(text):
#     return re.sub(r'([a-z])([a-z]*)', r'\2\1ay', text, flags=re.I)


def main():
    str = 'Pig latin is cool'
    str = 'AZ az !,'
    str = 'Start small, but will succeed!!'
    # str = 'This is my string'
    print(pig_it(str))


if __name__ == '__main__':
    main()
