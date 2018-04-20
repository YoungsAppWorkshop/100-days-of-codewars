#!/usr/bin/env python3
"""
Detect Pangram

    A pangram is a sentence that contains every single letter
    of the alphabet at least once.

    For example, the sentence "The quick brown fox jumps over the lazy dog"
    is a pangram, because it uses the letters A-Z at least once
    (case is irrelevant).

    Given a string, detect whether or not it is a pangram.
    Return True if it is, False if not.
    Ignore numbers and punctuation.

    https://www.codewars.com/kata/detect-pangram
"""
import re


# My Solution
def is_pangram(s):
    return True if len(set("".join(re.findall("[a-zA-Z]+", s)).lower())) == 26 else False  # noqa


# Best Practice
# import string
# def is_pangram(s):
#     return set(string.lowercase) <= set(s.lower())


if __name__ == '__main__':
    pangram = "The quick, brown fox jumps over the lazy dog!"
    print(is_pangram(pangram))
