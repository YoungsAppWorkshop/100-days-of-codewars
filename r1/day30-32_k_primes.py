#!/usr/bin/env python3
"""
k-Primes

    A natural number is called k-prime if it has exactly k prime factors,
    counted with multiplicity.

    A natural number is thus prime if and only if it is 1-prime.

Examples:
    k = 2 -> 4, 6, 9, 10, 14, 15, 21, 22, …
    k = 3 -> 8, 12, 18, 20, 27, 28, 30, …
    k = 5 -> 32, 48, 72, 80, 108, 112, …

#Task:

    Write function count_Kprimes (or countKprimes or count-K-primes or kPrimes)
    which given parameters k, start, end (or nd) returns an array
    (or a list or a string depending on the language - see "Solution" and
    "Sample Tests") of the k-primes between start (inclusive) and end
    (inclusive).

#Example:

    countKprimes(5, 500, 600) --> [500, 520, 552, 567, 588, 592, 594]


for all languages except Bash shell

    Given positive integers s and a, b, c where a is 1-prime, b 3-prime,
    c 7-prime find the number of solutions of a + b + c = s.
    Call this function puzzle(s).

Examples:

    puzzle(138) --> 1 ([2 + 8 + 128] is solution)
    puzzle(143) --> 2 ([3 + 12 + 128, 7 + 8 + 128] are solutions)

    https://www.codewars.com/kata/5726f813c8dcebf5ed000a6b/train/python
"""
from math import sqrt


# My Solution
def count_prime_factors(n):
    if n < 2:
        return 0
    count = 0
    while n % 2 == 0:
        n = n // 2
        count += 1
    for i in range(3, int(sqrt(n)) + 1, 2):
        while n % i == 0:
            n = n // i
            count += 1
    if n > 2:
        count += 1
    return count


def count_Kprimes(k, start, end):
    k_primes = []
    for i in range(start, end + 1):
        if count_prime_factors(i) == k:
            k_primes.append(i)
    return k_primes


def puzzle(s):
    answer = 0
    primes_7 = count_Kprimes(7, 128, s)
    for prime_7 in primes_7:
        primes_3 = count_Kprimes(3, 8, s - prime_7)
        for prime_3 in primes_3:
            primes_1 = count_Kprimes(1, 2, s - prime_7 - prime_3)
            for prime_1 in primes_1:
                if prime_1 + prime_3 + prime_7 == s:
                    answer += 1
    return answer


# Best Practice
# def func(args):
#     pass


if __name__ == '__main__':
    print(count_Kprimes(2, 0, 100))
