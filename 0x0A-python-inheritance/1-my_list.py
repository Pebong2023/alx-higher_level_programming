#!/usr/bin/python3

"""
A class MyList that inherits from the list class.
"""

class MyList(list):
    """
    Inherits from the list class.
    """
    
    def print_sorted(self):
        """
        Prints the list, but sorted in ascending order.
        """
        print(sorted(self))
