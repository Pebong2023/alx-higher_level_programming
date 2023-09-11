#!/usr/bin/python3

"""
Adds a new attribute to an object if it's possible.
"""

def add_attribute(obj, attribute, value):
    """
    Adds a new attribute to an object.

    Args:
        obj (object): The object to which the attribute will be added.
        attribute (str): The name of the attribute.
        value (any): The value to set for the attribute.

    Raises:
        TypeError: If the object doesn't have a dictionary (__dict__) or has slots (__slots__).
    """
    if '__dict__' not in dir(obj) and not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    if '__slots__' in dir(obj) or hasattr(obj, '__slots__'):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, attribute, value)
