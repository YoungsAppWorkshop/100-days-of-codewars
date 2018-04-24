#!/usr/bin/env python3

import unittest
from day23_scramblies import scramble


class Test(unittest.TestCase):

    def test_alphabet_war(self):
        self.assertEqual(scramble('rkqodlw', 'world'),  True)
        self.assertEqual(scramble('cedewaraaossoqqyt', 'codewars'), True)
        self.assertEqual(scramble('katas', 'steak'), False)
        self.assertEqual(scramble('scriptjava', 'javascript'), True)
        self.assertEqual(scramble('scriptingjava', 'javascript'), True)


if __name__ == '__main__':
    unittest.main()
