#!/usr/bin/python3

"""
Class MyInt that inherits from int.
"""

class MyInt(int):
    """
    Class MyInt that inherits from int.
    """
    def __eq__(self, other):
        """
        Override the equality operator (==).
        """
        return int(str(self)) != other

    def __ne__(self, other):
        """
        Override the inequality operator (!=).
        """
        return int(str(self)) == other
