#!/usr/bin/env python3
"""
    Find heavy ball
            - level: novice - 7 kyu
            - lever: conqueror - 6 kyu

        There are 8 balls numbered from 0 to 7.
        Seven of them have the same weight. One is heavier.
        Your task is to find it's number.

        Your function findBall will receive single argument - scales object.

        The scales object contains an internally stored array of 8 elements
        (indexes 0-7), each having the same value except one, which is greater.

        It also has a public method named getWeight(left, right) which takes
        two arrays of indexes and returns -1, 0, or 1 based on the accumulation
        of the values found at the indexes passed are heavier, equal, or
        lighter.

    getWeight returns:

        -1 if left pan is heavier

        1 if right pan is heavier

        0 if both pans weight the same

    Examples of scales.getWeight() usage:

        scales.getWeight([3], [7])
            returns -1 if ball 3 is heavier than ball 7,
            1 if ball 7 is heavier,
            or 0 i these balls have the same weight.

        scales.getWeight([3, 4], [5, 2])
            returns -1 if weight of balls 3 and 4 is heavier than
            weight of balls 5 and 2 etc.

    So where's the catch, you may ask. Well - the scales is very old.
    You can use it only 4 TIMES before the scale breaks.

    level - novice: https://www.codewars.com/kata/544047f0cf362503e000036e
    lever - conqueror: http://www.codewars.com/kata/find-heavy-ball-level-conqueror/train/python  # noqa
"""


# My Solution
def find_ball(scales):
    # call scales.get_weight() at most 4 TIMES
    # return indexOfHeavierBall

    first = 0
    last = 8

    while first < last:
        i = (first + last) / 2
        left = range(first, i)
        right = range(i, last)
        w = scales.get_weight(left, right)

        print(left, right, w)

        if w == -1:
            last = i
        elif w == 1:
            first = i

        if len(left) == 1:
            return left[0] if w == -1 else right[0]


# Best Practice
# def find_ball(scales):
#     balls = range(8)
#     while len(balls) > 1:
#         left, right = balls[:len(balls) / 2], balls[len(balls) / 2:]
#         balls = right if scales.get_weight(left, right) > 0 else left
#     return balls[0]


# if __name__ == '__main__':
#     main()
