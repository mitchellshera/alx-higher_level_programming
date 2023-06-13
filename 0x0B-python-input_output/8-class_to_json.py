#!/usr/bin/python3
"""DEfines a python class-to-JSON function"""


def class_to_json(obj):
    """Converts an object to a JSON-serializable dictionary representation."""
    json_dict = {}

    # Iterate through all attributes of the object
    for attr, value in obj.__dict__.items():
        # Check if the value is a list, dictionary, string, integer, or boolean
        if isinstance(value, (list, dict, str, int, bool)):
            json_dict[attr] = value

    return json_dict
