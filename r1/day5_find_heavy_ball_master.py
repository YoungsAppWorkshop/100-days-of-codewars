#!/usr/bin/env python3
"""
    Find heavy ball
            - level: novice - 7 kyu
            - lever: conqueror - 6 kyu
            - lever: master - 5 kyu

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
    You can use it only TWICE before the scale breaks.

    level - novice: https://www.codewars.com/kata/544047f0cf362503e000036e
    lever - conqueror: http://www.codewars.com/kata/find-heavy-ball-level-conqueror/train/python  # noqa
    lever - master: http://www.codewars.com/kata/find-heavy-ball-level-master/train/python  # noqa
"""


# My Solution
def find_ball(scales):
    group1, group2, group3 = [0, 1, 2], [3, 4, 5], [6, 7]
    first_scale = scales.get_weight(group1, group2)

    if first_scale == -1:
        # group1 is heavier
        second_scale = scales.get_weight(group1[0:1], group1[1:2])
        if second_scale == -1:
            return group1[0]
        elif second_scale == 1:
            return group1[1]
        else:
            return group1[2]
    elif first_scale == 1:
        # group2 is heavier
        second_scale = scales.get_weight(group2[0:1], group2[1:2])
        if second_scale == -1:
            return group2[0]
        elif second_scale == 1:
            return group2[1]
        else:
            return group2[2]
    else:
        # both pans weight the same
        second_scale = scales.get_weight(group3[0:1], group3[1:2])
        if second_scale == -1:
            return group3[0]
        elif second_scale == 1:
            return group3[1]
        else:
            return group3[2]


# Best Practice
# def find_ball(scales):
#     part = [[None, 0, 1], [2, 3, 4], [5, 6, 7]]
#     res1 = scales.get_weight(part[-1], part[1])
#     res2 = scales.get_weight([part[res1][-1]], [part[res1][1]])
#     return part[res1][res2]


# if __name__ == '__main__':
#     main()
