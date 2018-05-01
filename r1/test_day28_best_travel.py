#!/usr/bin/env python3

import unittest
from day29_best_travel import choose_best_sum


class Test(unittest.TestCase):

    def test_choose_best_sum(self):
        xs = [100, 76, 56, 44, 89, 73, 68, 56, 64, 123, 2333, 144, 50, 132, 123, 34, 89]  # noqa
        self.assertEqual(choose_best_sum(230, 4, xs), 230)
        self.assertEqual(choose_best_sum(430, 5, xs), 430)
        self.assertEqual(choose_best_sum(430, 8, xs), None)


if __name__ == '__main__':
    unittest.main()
