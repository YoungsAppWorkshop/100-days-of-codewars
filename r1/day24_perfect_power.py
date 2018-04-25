#!/usr/bin/env python3
"""
What's a Perfect Power anyway?

    A perfect power is a classification of positive integers:

    In mathematics, a perfect power is a positive integer that can be
    expressed as an integer power of another positive integer.

    More formally, n is a perfect power if there exist natural numbers
    m > 1, and k > 1 such that m^k = n.

    Your task is to check wheter a given integer is a perfect power.
    If it is a perfect power, return a pair m and k with mk = n as a proof.
    Otherwise return Nothing, Nil, null, NULL, None.

    Note: For a perfect power, there might be several pairs.

    For example 81 = 3^4 = 9^2, so (3,4) and (9,2) are valid solutions.
    However, the tests take care of this, so if a number is a perfect power,
    return any pair that proves it.

    Examples:
        isPP(4) => [2,2]
        isPP(9) => [3,2]
        isPP(5) => None

    https://www.codewars.com/kata/whats-a-perfect-power-anyway
"""
import math


# My Solution
def isPP(n):
    for m in range(2, int(math.sqrt(n)) + 1):
        k = 2
        while m**k <= n:
            if m**k == n:
                return [m, k]
            k += 1
    return None


# Best Practice
# from math import log, sqrt
# def isPP(n):
#     for b in range(2, int(sqrt(n)) + 1):
#         e = int(round(log(n, b)))
#         if b ** e == n:
#             return [b, e]
#     return None


if __name__ == '__main__':
    print(isPP(4))
    print(isPP(9))
    print(isPP(5))
