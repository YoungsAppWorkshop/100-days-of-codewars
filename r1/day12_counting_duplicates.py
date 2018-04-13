#!/usr/bin/env python3
"""
    Counting Duplicates - 6 kyu

        Write a function that will return the count of distinct
        case-insensitive alphabetic characters and numeric digits
        that occur more than once in the input string.

        The input string can be assumed to contain only alphabets
        (both uppercase and lowercase) and numeric digits.

    Example
        "abcde" -> 0 # no characters repeats more than once
        "aabbcde" -> 2 # 'a' and 'b'
        "aabBcde" -> 2 # 'a' occurs twice and 'b' twice (bandB)
        "indivisibility" -> 1 # 'i' occurs six times
        "Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
        "aA11" -> 2 # 'a' and '1'
        "ABBA" -> 2 # 'A' and 'B' each occur twice

    https://www.codewars.com/kata/counting-duplicates
"""


# My Solution
def duplicate_count(text):
    dict, sum = {}, 0

    for letter in text:
        key = letter.lower()
        if dict.get(key):
            dict[key] += 1
        else:
            dict[key] = 1

    for key in dict:
        if dict[key] > 1:
            sum += 1
    return sum


# Best Practice
# def duplicate_count(s):
#   return len([c for c in set(s.lower()) if s.lower().count(c)>1])


if __name__ == '__main__':
    print(duplicate_count("abcde"))
    print(duplicate_count("aabbcde"))
    print(duplicate_count("aabBcde"))
    print(duplicate_count("indivisibility"))
    print(duplicate_count("Indivisibilities"))
    print(duplicate_count("aA11"))
    print(duplicate_count("ABBA"))
