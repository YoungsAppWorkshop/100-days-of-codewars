#!/usr/bin/env python3

import unittest
from day15_is_it_IPv4_address import ipv4_address


class Test(unittest.TestCase):

    def test_ipv4_address(self):
        self.assertEqual(ipv4_address(""), False)
        self.assertEqual(ipv4_address("127.0.0.1"), True)
        self.assertEqual(ipv4_address("0.0.0.0"), True)
        self.assertEqual(ipv4_address("255.255.255.255"), True)
        self.assertEqual(ipv4_address("10.20.30.40"), True)
        self.assertEqual(ipv4_address("10.256.30.40"), False)
        self.assertEqual(ipv4_address("10.20.030.40"), False)
        self.assertEqual(ipv4_address("127.0.1"), False)
        self.assertEqual(ipv4_address("127.0.0.0.1"), False)
        self.assertEqual(ipv4_address("..255.255"), False)
        self.assertEqual(ipv4_address("127.0.0.1\n"), False)
        self.assertEqual(ipv4_address("\n127.0.0.1"), False)
        self.assertEqual(ipv4_address(" 127.0.0.1"), False)
        self.assertEqual(ipv4_address("127.0.0.1 "), False)
        self.assertEqual(ipv4_address(" 127.0.0.1 "), False)


if __name__ == '__main__':
    unittest.main()
