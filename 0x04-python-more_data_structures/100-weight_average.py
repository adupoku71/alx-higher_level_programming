#!/usr/bin/python3


def weight_average(my_list=[]):

    if not my_list:
        return 0

    nums = 0
    denoms = 0
    for x, y in my_list:
        nums += (x * y)
        denoms += y

    return nums / denoms
