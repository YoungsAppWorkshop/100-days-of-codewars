#!/usr/bin/env python3

import unittest
from day21_tank_truck import tankvol


class Test(unittest.TestCase):

    def test_tankvol(self):
        self.assertEqual(tankvol(5, 7, 3848), 2940)
        self.assertEqual(tankvol(2, 7, 3848), 907)


if __name__ == '__main__':
    unittest.main()
