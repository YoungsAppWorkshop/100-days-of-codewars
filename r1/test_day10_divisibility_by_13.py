#!/usr/bin/env python3

import unittest
from day10_divisibility_by_13 import thirt


class Test(unittest.TestCase):

    def test_thirt(self):
        self.assertEqual(thirt(8529), 79)
        self.assertEqual(thirt(85299258), 31)
        self.assertEqual(thirt(5634), 57)
        self.assertEqual(thirt(1111111111), 71)
        self.assertEqual(thirt(987654321), 30)


if __name__ == '__main__':
    unittest.main()
