#!/usr/bin/env python3

import unittest
from day22_alphabet_war import alphabet_war


class Test(unittest.TestCase):

    def test_alphabet_war(self):
        self.assertEqual(alphabet_war("z"), "Right side wins!")
        self.assertEqual(alphabet_war("****"), "Let's fight again!")
        self.assertEqual(alphabet_war("z*dq*mw*pb*s"), "Let's fight again!")
        self.assertEqual(alphabet_war("zdqmwpbs"), "Let's fight again!")
        self.assertEqual(alphabet_war("zz*zzs"), "Right side wins!")
        self.assertEqual(alphabet_war("sz**z**zs"), "Left side wins!")
        self.assertEqual(alphabet_war("z*z*z*zs"), "Left side wins!")
        self.assertEqual(alphabet_war("*wwwwww*z*"), "Left side wins!")
        self.assertEqual(alphabet_war("w****z"), "Let's fight again!")
        self.assertEqual(alphabet_war("mb**qwwp**dm"), "Let's fight again!")


if __name__ == '__main__':
    unittest.main()
