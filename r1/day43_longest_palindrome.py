#!/usr/bin/env python3
"""
Longest Palindrome

    Find the length of the longest substring in the given string s that is the
    same in reverse.

    As an example, if the input was “I like racecars that go fast”, the
    substring (racecar) length would be 7.

    If the length of the input string is 0, the return value must be 0.

    Example:
        "a" -> 1
        "aab" -> 2
        "abcde" -> 1
        "zzbaabcd" -> 4
        "" -> 0

    https://www.codewars.com/kata/
"""


def is_palindrome(s):
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


# My Solution
def longest_palindrome(s):
    length = len(s)
    while length > 0:
        left = 0
        right = left + length
        while right <= len(s):
            if is_palindrome(s[left:right]):
                return length
            left += 1
            right += 1
        length -= 1
    return length


# Best Practice
# def func(args):
#     pass


if __name__ == '__main__':
    print(longest_palindrome("abcdefghba"))
    print(longest_palindrome(""))
