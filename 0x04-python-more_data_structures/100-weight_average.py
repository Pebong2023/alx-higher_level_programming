#!/usr/bin/python3

def weight_average(my_list=[]):
    """
    Calculate the weighted average of a list of tuples.
    """
    if not my_list:
        return 0

    total_num = sum([x * y for x, y in my_list])
    total_den = sum([y for _, y in my_list])

    return (total_num / total_den)
