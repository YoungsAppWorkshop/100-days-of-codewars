#!/usr/bin/env python3
"""
Extract file name

    You have to extract a portion of the file name as follows:

    Assume it will start with date represented as long number
    Followed by an underscore
    Youll have then a filename with an extension
    it will always have an extra extension at the end

    Inputs:
        1231231223123131_FILE_NAME.EXTENSION.OTHEREXTENSION
        1_This_is_an_otherExample.mpg.OTHEREXTENSIONadasdassdassds34
        1231231223123131_myFile.tar.gz2

    Outputs:
        FILE_NAME.EXTENSION
        This_is_an_otherExample.mpg
        myFile.tar

    The recommend way to solve it is using RegEx and specifically groups.

    https://www.codewars.com/kata/extract-file-name
"""
import re


# My Solution
def extract_file_name(dirty_file_name):
    match = re.match(r'\d+_([\w-]+)\.([\w-]+)\.\w*', dirty_file_name)
    return match.group(1) + '.' + match.group(2)


# Best Practice
# def extract_file_name(dirty_file_name):
#     return re.match(r'\d+_(.+?\..+?)\.', dirty_file_name).group(1)


if __name__ == '__main__':
    print(extract_file_name("123123122131_FILE_NAME.EXTENSION.OTHEREXTENSION"))
    print(extract_file_name("1_FILE_NAME.EXTENSION.OTHEREXTENSIONadasdassds4"))
    print(extract_file_name("05448615793675593_d_zSivbWpDpD-eiBX_.kt2.L2_2Lo4G4T6N_S2eF2B"))  # noqa
