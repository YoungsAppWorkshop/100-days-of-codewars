#!/usr/bin/env python3

import unittest
from day12_counting_duplicates import duplicate_count


class Test(unittest.TestCase):

    def test_thirt(self):
        self.assertEqual(duplicate_count("abcde"), 0)
        self.assertEqual(duplicate_count("abcdea"), 1)
        self.assertEqual(duplicate_count("indivisibility"), 1)


if __name__ == '__main__':
    unittest.main()
