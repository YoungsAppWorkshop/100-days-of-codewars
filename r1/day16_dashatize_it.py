#!/usr/bin/env python3
"""
Dashatize it

    Given a number, return a string with dash'-'marks before and
    after each odd integer, but do not begin or end the string
    with a dash mark.

    Ex:

        dashatize(274) -> '2-7-4'
        dashatize(6815) -> '68-1-5'

    https://www.codewars.com/kata/dashatize-it
"""


# My Solution
def dashatize(args):
    try:
        lst = [x for x in str(abs(args))]
    except Exception:
        return "None"
    else:
        str1 = ''
        for index in range(len(lst) - 1):
            if int(lst[index]) % 2 == 1:
                str1 += lst[index] + '-'
            elif int(lst[index + 1]) % 2 == 1:
                str1 += lst[index] + '-'
            else:
                str1 += lst[index]
        str1 += lst[-1]
        return str1


# Best Practice
# def dashatize(num):
#     try:
#         return ''.join(['-' + i + '-' if int(i) % 2 else i
#                         for i in str(abs(num))]).replace('--', '-').strip('-')  # noqa
#     except Exception:
#         return 'None'


if __name__ == '__main__':
    print(dashatize(274))
    print(dashatize(6815))
    print(dashatize(None))
    print(dashatize(-28369))
