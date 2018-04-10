#!/usr/bin/env python3
"""
    Tortoise racing - 6 kyu

        Two tortoises named A and B must run a race.

        A starts with an average speed of 720 feet per hour.
        Young B knows she runs faster than A, and furthermore
        has not finished her cabbage.

        When she starts, at last, she can see that A has a 70 feet lead
        but B's speed is 850 feet per hour. How long will it take B to catch A?

        More generally: given two speeds v1 (A's speed, integer > 0) and
        v2 (B's speed, integer > 0) and a lead g (integer > 0)

        how long will it take B to catch A?

        The result will be an array [hour, min, sec] which is the time
        needed in hours, minutes and seconds
        (don't worry for fractions of second).

        If v1 >= v2 then return nil, nothing, null, None
        or {-1, -1, -1} for C++, C, Go, Nim, [] for Kotlin.

    Examples
        race(720, 850, 70) => [0, 32, 18]
        race(80, 91, 37)   => [3, 21, 49]

    http://www.codewars.com/kata/55e2adece53b4cdcb900006c/train/python
"""


# My Solution
def race(v1, v2, g):
    if v2 > v1:
        division = g / (v2 - v1)
        return [int(division), int(division * 60 % 60), int(division * 3600 % 60)]  # noqa


# Best Practice
# def race(v1, v2, g):
#     if v1>v2: return None
#     res = g*3600/(v2-v1)
#     return [res/3600,res%3600/60,res%60]

if __name__ == '__main__':
    print(race(720, 850, 70))
    print(race(80, 91, 37))
    print(race(80, 100, 40))
    print(race(80, 80, 40))
