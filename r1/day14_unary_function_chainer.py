#!/usr/bin/env python3
"""
Unary function chainer

    Your task is to write a higher order function for chaining together
    a list of unary functions. In other words, it should return a function
    that does a left fold on the given functions.

        chained([a,b,c,d])(input)

    Should yield the same result as

        d(c(b(a(input))))

    https://www.codewars.com/kata/unary-function-chainer
"""


def f1(x): return x * 2


def f2(x): return x + 2


def f3(x): return x**2


# My Solution
def chained(functions):
    def inner_func(arg):
        if len(functions) > 0:
            return chained(functions[1:])(functions[0](arg))
        return arg
    return inner_func


# Other Solution
# def chained(functions):
#     def f(x):
#         for function in functions:
#             x = function(x)
#         return x
#     return f


if __name__ == '__main__':
    print(chained([f1, f2, f3])(0))
