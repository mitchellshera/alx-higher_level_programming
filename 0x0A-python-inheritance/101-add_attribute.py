#!/usr/bin/python3


def add_attribute(obj, name, value):
    """
    Adds a new attribute to an object if it's possible.
    Raises a TypeError if the object can't have a new attribute.
    """
    if hasattr(obj, "__dict__") or \
       (hasattr(obj, "__slots__") and name in obj.__slots__):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
