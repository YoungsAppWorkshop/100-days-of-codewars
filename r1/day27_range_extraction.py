#!/usr/bin/env python3
"""
Range Extraction

    A format for expressing an ordered list of integers is to use
    a comma separated list of either individual integers or a range
    of integers denoted by the starting integer separated from the
    end integer in the range by a dash, '-'.

    The range includes all integers in the interval including both
    endpoints. It is not considered a range unless it spans at least
    3 numbers. For example ("12, 13, 15-17")

    Complete the solution so that it takes a list of integers in
    increasing order and returns a correctly formatted string in the
    range format.

    Example:

        solution([-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20])  # noqa
        # returns "-6,-3-1,3-5,7-11,14,15,17-20"


    https://www.codewars.com/kata/range-extraction
"""


# My Solution
def solution(numbers):
    pprev, prev = False, False
    output = ''
    for index, num in enumerate(numbers):
        try:
            next = numbers[index] + 1 == numbers[index + 1]
        except IndexError:
            next = None
        if next is True:
            if prev is False:
                output += str(numbers[index])
        else:
            if pprev is False and prev is True:
                output += ','
            elif pprev is True and prev is True:
                output += '-'
            output += str(numbers[index])
            if next is False:
                output += ','
        pprev = prev
        prev = next
    return output


# Best Practice
# def func(args):
#     pass

lst = [-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]

if __name__ == '__main__':
    print(solution(lst))
