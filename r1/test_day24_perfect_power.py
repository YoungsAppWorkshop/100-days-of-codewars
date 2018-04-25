#!/usr/bin/env python3

import unittest
from day24_perfect_power import isPP


class Test(unittest.TestCase):

    def test_perfect_power(self):
        self.assertEqual(isPP(4), [2, 2])
        self.assertEqual(isPP(9), [3, 2])
        self.assertEqual(isPP(5), None)


if __name__ == '__main__':
    unittest.main()
