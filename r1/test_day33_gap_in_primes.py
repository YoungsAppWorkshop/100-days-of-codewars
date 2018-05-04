#!/usr/bin/env python3

import unittest
from day33_gap_in_primes import gap


class Test(unittest.TestCase):

    def test_gap(self):
        self.assertEqual(gap(2, 100, 110), [101, 103])
        self.assertEqual(gap(4, 100, 110), [103, 107])
        self.assertEqual(gap(6, 100, 110), None)
        self.assertEqual(gap(8, 300, 400), [359, 367])
        self.assertEqual(gap(10, 300, 400), [337, 347])


if __name__ == '__main__':
    unittest.main()
