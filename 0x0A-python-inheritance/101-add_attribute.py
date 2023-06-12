#!/usr/bin/python3


def add_attribute(obj, attribute, value):
    """
    Adds a new attribute to an object if it's possible.
    Raises a TypeError if the object can't have a new attribute.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    obj.__setattr__(attribute, value)
