#!/usr/bin/env python3

import unittest
from day18_fibonacci_and_friends import Xbonacci


class Test(unittest.TestCase):

    def test_Xbonacci(self):
        self.assertEqual(Xbonacci([0, 1], 10), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])  # noqa
        self.assertEqual(Xbonacci([1, 1], 10), [1, 1, 2, 3, 5, 8, 13, 21, 34, 55])  # noqa
        self.assertEqual(Xbonacci([0, 0, 0, 0, 1], 10), [0, 0, 0, 0, 1, 1, 2, 4, 8, 16])  # noqa
        self.assertEqual(Xbonacci([1, 0, 0, 0, 0, 0, 1], 10), [1, 0, 0, 0, 0, 0, 1, 2, 3, 6])  # noqa
        self.assertEqual(Xbonacci([1, 0, 0, 0, 0, 0, 0, 0, 0, 0], 20), [
                         1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 2, 4, 8, 16, 32, 64, 128, 256])  # noqa


if __name__ == '__main__':
    unittest.main()
