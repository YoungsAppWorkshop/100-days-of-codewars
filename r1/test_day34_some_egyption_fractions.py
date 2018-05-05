#!/usr/bin/env python3

import unittest
from day34_some_egyption_fractions import decompose


class Test(unittest.TestCase):

    def test_decompose(self):
        self.assertEqual(decompose('0'), [])
        self.assertEqual(decompose('3/4'), ["1/2", "1/4"])
        self.assertEqual(decompose('4/5'), ["1/2", "1/4", "1/20"])
        self.assertEqual(decompose('0.66'), ["1/2", "1/7", "1/59", "1/5163", "1/53307975"])  # noqa
        self.assertEqual(decompose('75/3'), ["25"])


if __name__ == '__main__':
    unittest.main()
