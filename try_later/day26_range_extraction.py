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


    https://www.codewars.com/kata/51ba717bb08c1cd60f00002f/train/python
"""


# My Solution
def solution(numbers):
    dict = {numbers[i]: numbers[i + 1] == numbers[i] + 1 for i in range(len(numbers) - 1)}
    print(dict)
    # pprev, prev = False, False
    # str = ''
    # for index, num in enumerate(numbers):
    #     try:
    #         next = numbers[index] + 1 == numbers[index + 1]
    #     except IndexError:
    #         next = False
    #     print("Index: {} Number: {} pprev: {} prev: {} next: {}".format(
    #         index, numbers[index], pprev, prev, next
    #     ))
    #     if prev is False and next is False:
    #         str += str(numbers[index]) + ','
    #     elif prev is False and next is True:
    #         str += str(numbers[index])
    #     pprev = prev
    #     prev = next
    return numbers


# Best Practice
# def func(args):
#     pass

lst = [-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]

if __name__ == '__main__':
    print(solution(lst))
