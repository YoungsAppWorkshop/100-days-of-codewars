#!/usr/bin/env python3

import unittest
from day16_dashatize_it import dashatize


class Test(unittest.TestCase):

    def test_dashatize_it(self):
        self.assertEqual(dashatize(274), "2-7-4")
        self.assertEqual(dashatize(5311), "5-3-1-1")
        self.assertEqual(dashatize(86320), "86-3-20")
        self.assertEqual(dashatize(974302), "9-7-4-3-02")
        self.assertEqual(dashatize(None), "None")
        self.assertEqual(dashatize(0), "0")
        self.assertEqual(dashatize(-1), "1")
        self.assertEqual(dashatize(-28369), "28-3-6-9")


if __name__ == '__main__':
    unittest.main()
