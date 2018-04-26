#!/usr/bin/env python3

import unittest
from day25_valid_braces import validBraces


class Test(unittest.TestCase):

    def test_valid_braces(self):
        self.assertEqual(validBraces("(){}[]"), True)
        self.assertEqual(validBraces("([{}])"), True)
        self.assertEqual(validBraces("(}"), False)
        self.assertEqual(validBraces("[(])"), False)
        self.assertEqual(validBraces("[({})](]"), False)


if __name__ == '__main__':
    unittest.main()
