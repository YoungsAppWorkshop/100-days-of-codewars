#!/usr/bin/env python3

import unittest
from day42_simultaneous_equations import solve_eq


class Test(unittest.TestCase):

    def test_decompose(self):
        self.assertEqual(solve_eq([[4, -3, 1, -10], [2, 1, 3, 0], [-1, 2, -5, 17]]), [1, 4, -2])  # noqa
        self.assertEqual(solve_eq([[2, 1, 3, 10], [-3, -2, 7, 5], [3, 3, -4, 7]]), [-1, 6, 2])  # noqa
        self.assertEqual(solve_eq([[3, 2, 0, 7], [-4, 0, 3, -6], [0, -2, -6, -10]]), [3, -1, 2])  # noqa
        self.assertEqual(solve_eq([[4, 2, -5, -21], [2, -2, 1, 7], [4, 3, -1, -1]]), [1, 0, 5])  # noqa
        self.assertEqual(solve_eq([[1, 1, 1, 5], [2, 2, 3, 14], [2, -3, 2, -5]]), [-2, 3, 4])  # noqa


if __name__ == '__main__':
    unittest.main()
