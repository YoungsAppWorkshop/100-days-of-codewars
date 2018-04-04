#!/usr/bin/env python3
"""
    Highest and Lowest - 7 kyu
        In this little assignment you are given a string of space separated
        numbers, and have to return the highest and lowest number.

    Notes:

        - All numbers are valid Int32, no need to validate them.
        - There will always be at least one number in the input string.
        - Output string must be two numbers separated by a single space, and
            highest number is first.

    Examples:
        high_and_low("1 2 3 4 5")  # return "5 1"
        high_and_low("1 2 -3 4 5") # return "5 -3"
        high_and_low("1 9 3 4 -5") # return "9 -5"

    https://www.codewars.com/kata/554b4ac871d6813a03000035/train/python
"""


# My Solution
def high_and_low(numbers):
    numbers = [int(x) for x in numbers.split(' ')]
    return '{} {}'.format(max(numbers), min(numbers))


# Best Practice
# def high_and_low(numbers): #z.
#     nn = [int(s) for s in numbers.split(" ")]
#     return "%i %i" % (max(nn),min(nn))


if __name__ == '__main__':
    print(high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"))
