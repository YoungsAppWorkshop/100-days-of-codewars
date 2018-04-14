#!/usr/bin/env python3
"""
    Moves in squared strings (II) - 6 kyu

        You are given a string of n lines, each substring being
        n characters long: For example:

            s = "abcd\nefgh\nijkl\nmnop"

        We will study some transformations of this square of strings.


    Clock rotation 180 degrees: rot
        rot(s) => "ponm\nlkji\nhgfe\ndcba"

    selfie_and_rot(s) (or selfieAndRot or selfie-and-rot)

        It is initial string + string obtained by clock rotation 180 degrees
        with dots interspersed in order (hopefully) to better show the rotation
        when printed.

        |rotation        |selfie_and_rot
        |abcd --> ponm   |abcd --> abcd....
        |efgh     lkji   |efgh     efgh....
        |ijkl     hgfe   |ijkl     ijkl....
        |mnop     dcba   |mnop     mnop....
                                   ....ponm
                                   ....lkji
                                   ....hgfe
                                   ....dcba

    #Task:

        Write these two functions rotand selfie_and_rot and high-order function
        oper(fct, s) where fct is the function of one variable f to apply to
        the string s (fct will be one of rot, selfie_and_rot)

    https://www.codewars.com/kata/moves-in-squared-strings-ii
"""


# My Solution
def rot(strng):
    return strng[::-1]


def selfie_and_rot(strng):
    selfie = '\n'.join([x + '.' * len(x) for x in strng.split('\n')])
    and_rot = rot(selfie)
    return '{}\n{}'.format(selfie, and_rot)


def oper(fct, s):
    return fct(s)


# Best Practice
# def rot(string):
#     return string[::-1]
#
# def selfie_and_rot(string):
#     s_dot = '\n'.join([ s+'.'*len(s) for s in string.split('\n') ])
#     return s_dot+'\n'+rot(s_dot)
#
# def oper(fct, s):
#     return fct(s)


if __name__ == '__main__':
    print(oper(rot, "abcd\nefgh\nijkl\nmnop"))
    print()
    print(oper(selfie_and_rot, "abcd\nefgh\nijkl\nmnop"))
