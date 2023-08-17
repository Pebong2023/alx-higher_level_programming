#!/usr/bin/python3
def multiply_list_elements(my_list=[], factor=1):
    """
    Multiply elements in a list by a specified factor using map and a lambda function.
    """
    multiplied_list = list(map(lambda x: x * factor, my_list))
    return (multiplied_list)
