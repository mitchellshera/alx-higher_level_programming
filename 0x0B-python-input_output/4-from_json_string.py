#!/usr/bin/python3
""" Defines a JSON-to-object function """
import json


def from_json_string(my_str):
    """
    Convert a JSON string to its corresponding Python object.

    Args:
        my_str: The JSON string to be converted.

    Returns:
        The Python object represented by the JSON string.
    """
    return json.loads(my_str)
