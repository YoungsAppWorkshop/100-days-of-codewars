#!/usr/bin/env python3

import unittest
from day43_longest_palindrome import longest_palindrome


class Test(unittest.TestCase):
    def test_longest_palindrome(self):
        self.assertEqual(longest_palindrome("a"), 1)
        self.assertEqual(longest_palindrome("aa"), 2)
        self.assertEqual(longest_palindrome("baa"), 2)
        self.assertEqual(longest_palindrome("aab"), 2)
        self.assertEqual(longest_palindrome("abcdefghba"), 1)
        self.assertEqual(longest_palindrome("baablkj12345432133d"), 9)


if __name__ == '__main__':
    unittest.main()
