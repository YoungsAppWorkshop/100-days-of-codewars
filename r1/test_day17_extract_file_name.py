#!/usr/bin/env python3

import unittest
from day17_extract_file_name import extract_file_name


class Test(unittest.TestCase):

    def test_extract_file_name(self):
        self.assertEqual(extract_file_name("1231231223123131_FILE_NAME.EXTENSION.OTHEREXTENSION"), "FILE_NAME.EXTENSION")  # noqa
        self.assertEqual(extract_file_name("1_FILE_NAME.EXTENSION.OTHEREXTENSIONadasdassdassds34"), "FILE_NAME.EXTENSION")  # noqa
        self.assertEqual(extract_file_name("05448615793675593_d_zSivbWpDpD-eiBX_.kt2.L2_2Lo4G4T6N_S2eF2B"), "FILE_NAME.EXTENSION")  # noqa


if __name__ == '__main__':
    unittest.main()
