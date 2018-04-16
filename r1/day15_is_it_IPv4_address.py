#!/usr/bin/env python3
"""
Regexp Basics - is it IPv4 address?

    Implement String#ipv4_address?,
    which should return true if given object is an IPv4 address
    - four numbers (0-255) separated by dots.

    It should only accept addresses in canonical representation,
    so no leading 0s, spaces etc.

    https://www.codewars.com/kata/regexp-basics-is-it-ipv4-address
"""
import re


# My Solution
def ipv4_address(address):
    ip = '([1-9]?[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])'
    return True if re.fullmatch("^(" + ip + "\.){3}" + ip + "$", address)\
        else False


# Best Practice
# from re import compile, match
# REGEX = compile(r'((\d|[1-9]\d|1\d\d|2[0-4]\d|25[0-5])\.){4}$')
# def ipv4_address(address):
#     # refactored thanks to @leonoverweel on CodeWars
#     return bool(match(REGEX, address + '.'))


if __name__ == '__main__':
    print(ipv4_address(""))
    print(ipv4_address("127.0.0.1"))
    print(ipv4_address("0.0.0.0"))
    print(ipv4_address("255.255.255.255"))
    print(ipv4_address("10.20.30.40"))
    print(ipv4_address("10.256.30.40"))
    print(ipv4_address("10.20.030.40"))
    print(ipv4_address("127.0.1"))
    print(ipv4_address("127.0.0.0.1"))
    print(ipv4_address("..255.255"))
    print(ipv4_address("127.0.0.1\n"))
    print(ipv4_address("\n127.0.0.1"))
    print(ipv4_address(" 127.0.0.1"))
    print(ipv4_address("127.0.0.1 "))
    print(ipv4_address(" 127.0.0.1 "))
