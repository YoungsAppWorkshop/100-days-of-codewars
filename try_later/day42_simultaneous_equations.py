#!/usr/bin/env python3
"""
Simultaneous Equations - Three Variables

    We have 3 equations with 3 unknowns x, y, and z and we are to solve for
    these unknowns.

    Equations 4x -3y +z = -10, 2x +y +3z = 0, and -x +2y -5z = 17 will be
    passed in as an array of [[4, -3, 1, -10], [2, 1, 3, 0], [-1, 2, -5, 17]]
    and the result should be returned as an array like [1, 4, -2]
    (i.e. [x, y, z]).

    Note: In C++ do not use new or malloc to allocate memory for the returned
    variable as allocated memory will not be freed in the Test Cases. Setting
    the variable as static will do.

    https://www.codewars.com/kata/59280c056d6c5a74ca000149/train/python
"""
import numpy as np


# My Solution
def solve_eq(eq):
    A = np.array([vector[:3] for vector in eq])
    b = np.array([vector[-1] for vector in eq])
    return [int(x) for x in np.linalg.solve(A, b)]


# Best Practice
# def func(args):
#     pass


if __name__ == '__main__':
    print(solve_eq([[4, -3, 1, -10], [2, 1, 3, 0], [-1, 2, -5, 17]]))
    print(solve_eq([[2, 1, 3, 10], [-3, -2, 7, 5], [3, 3, -4, 7]]))
