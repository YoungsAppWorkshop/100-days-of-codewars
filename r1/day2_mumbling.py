#!/usr/bin/env python3
"""
    Mumbling - 7 kyu
        This time no story, no theory.
        The parameter of accum is a string which includes only
        letters from a..z and A..Z.
        The examples below show you how to write function accum:

        accum("abcd")    # "A-Bb-Ccc-Dddd"
        accum("RqaEzty") # "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
        accum("cwAt")    # "C-Ww-Aaa-Tttt"

    https://www.codewars.com/kata/5667e8f4e3f572a8f2000039/train/python
"""


# My Solution
def accum(s):
    str = ''
    for index, letter in enumerate(s):
        str += letter.upper() + letter.lower() * index + '-'
    return str[:-1]


# Best Practice
# def accum(s):
#     return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s))


if __name__ == '__main__':
    print(accum("abcd"))
