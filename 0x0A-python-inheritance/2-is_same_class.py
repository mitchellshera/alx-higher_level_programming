#!/usr/bin/python3

def is_same_class(obj, a_class):
    """
    Check if the object is exactly an instance of the specified class.

    Args:
        obj: The object to be checked.
        a_class: The specified class.

    Returns:
        True if the object is exactly an instance of the specified class;
        otherwise, False.
    """
    return type(obj) is a_class
