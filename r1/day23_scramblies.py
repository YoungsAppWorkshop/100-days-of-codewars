#!/usr/bin/env python3
"""
Scramblies

    Complete the function scramble(str1, str2) that returns true
    if a portion of str1 characters can be rearranged to match str2,
    otherwise returns false.

    Notes:
        Only lower case letters will be used (a-z).
        No punctuation or digits will be included.
        Performance needs to be considered

    Examples:
        scramble('rkqodlw', 'world') ==> True
        scramble('cedewaraaossoqqyt', 'codewars') ==> True
        scramble('katas', 'steak') ==> False

    http://www.codewars.com/kata/scramblies
"""


# My Solution
def scramble(s1, s2):
    dict = {}
    for l in s1:
        if dict.get(l):
            dict[l] += 1
        else:
            dict[l] = 1
    for l in s2:
        if dict.get(l):
            dict[l] -= 1
        else:
            return False
    return True


# Best Practice
# from collections import Counter
# def scramble(s1,s2):
#     # Counter basically creates a dictionary of counts and letters
#     # Using set subtraction, we know that if anything is left over,
#     # something exists in s2 that doesn't exist in s1
#     return len(Counter(s2)- Counter(s1)) == 0


# def scramble(s1,s2):
#     for c in set(s2):
#         if s1.count(c) < s2.count(c):
#             return False
#     return True


if __name__ == '__main__':
    print(scramble('rkqodlw', 'world'))
    print(scramble('cedewaraaossoqqyt', 'codewars'))
    print(scramble('katas', 'steak'))
