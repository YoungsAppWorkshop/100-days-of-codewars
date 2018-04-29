#!/usr/bin/env python3
"""
Pyramid Slide Down

    Pyramids are amazing! Both in architectural and mathematical sense.
    If you have a computer, you can mess with pyramids even if you are
    not in Egypt at the time. For example, let's consider the following
    problem.

    Imagine that you have a plane pyramid built of numbers, like this one
    here:

           /3/
          \7\ 4
         2 \4\ 6
        8 5 \9\ 3

    Here comes the task...

    Let's say that the 'slide down' is a sum of consecutive numbers from
    the top to the bottom of the pyramid. As you can see, the longest
    'slide down' is 3 + 7 + 4 + 9 = 23

    Your task is to write a function longestSlideDown
    (in ruby: longest_slide_down) that takes a pyramid representation as
    argument and returns its' longest 'slide down'.

    For example,

        longestSlideDown([[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]])
        # => 23

    By the way... My tests include some extraordinarily high pyramides
    so as you can guess, brute-force method is a bad idea unless you have
    a few centuries to waste. You must come up with something more clever
    than that.

    http://www.codewars.com/kata/pyramid-slide-down
"""


# My Solution
def longest_slide_down(pyramid):
    if len(pyramid) <= 1:
        return pyramid[0][0]
    else:
        lst0 = pyramid[-2]
        lst1 = pyramid[-1]
        for i in range(len(lst0)):
            lst0[i] += lst1[i] if lst1[i] > lst1[i + 1] else lst1[i + 1]
        lst2 = pyramid[:-2]
        lst2.append(lst0)

        return longest_slide_down(lst2)


# Best Practice
# def longest_slide_down(p):
#     res = p.pop()
#     while p:
#         tmp = p.pop()
#         res = [tmp[i] + max(res[i],res[i+1])  for i in range(len(tmp))]
#     return res.pop()


# longest_slide_down = lambda l:reduce(lambda x,y:[max([x[i],x[i+1]])+y[i] for i in range(len(y))],l[::-1])[0]  # noqa


if __name__ == '__main__':
    lst = [[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]
    # lst = [[3], [7, 4], [2, 4, 6]]
    # lst = [[3], [7, 4]]
    print(longest_slide_down(lst))
