#!/usr/bin/env python3
"""
    Kebabize - 6 kyu

        Modify the kebabize function so that it converts
        a camel case string into a kebab case.

        the returned string should only contain lowercase letters

    Examples
        kebabize('camelsHaveThreeHumps') // camels-have-three-humps
        kebabize('camelsHave3Humps') // camels-have-humps

    https://www.codewars.com/kata/57f8ff867a28db569e000c4a/train/python
"""
import re


# My Solution
def kebabize(string):
    string = ''.join([i for i in string if not i.isdigit()])
    try:
        string = string[0].upper() + string[1:]
    except IndexError:
        pass
    return ('-'.join(re.findall('[A-Z][a-z]*', string))).lower()


# Best Practice
# def kebabize(s):
#     return ''.join(c if c.islower() else '-' + c.lower() for c in s if c.isalpha()).strip('-')  # noqa


if __name__ == '__main__':
    print(kebabize('myCamelCasedString'))
