#!/usr/bin/env python3
"""
    Mexican Wave - 6 kyu

        In this simple Kata your task is to create a function that
        turns a string into a Mexican Wave.

        You will be passed a string and you must return that string
        in an array where an uppercase letter is a person standing up.

    Rules
        1. The input string will always be lower case but maybe empty.

        2. If the character in the string is whitespace then pass over it
            as if it was an empty seat.

    Examples
        wave("hello") => ["Hello", "hEllo", "heLlo", "helLo", "hellO"]

    https://www.codewars.com/kata/mexican-wave/train/python
"""


# My Solution
def wave(str):
    return [str[:i] + str[i].upper() + str[i + 1:]
            for i in range(len(str)) if str[i].isalpha()]


# Best Practice
# def wave(str):
#     return [str[:i] + str[i].upper() + str[i+1:] for i in range(len(str)) if str[i].isalpha()]  # noqa


if __name__ == '__main__':
    print(wave('hello'))
    print(wave(''))
    print(wave('two words'))
    print(wave(' gap '))
