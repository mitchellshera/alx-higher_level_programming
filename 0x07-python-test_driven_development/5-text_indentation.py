#!/usr/bin/python3
"""Defines a text-indentation function."""


def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = ""
    chars_to_indent = [".", "?", ":"]
    prev_char = ""

    for char in text:
        if prev_char in chars_to_indent:
            if char == " ":
                continue
            else:
                result += "\n\n" + char
        else:
            result += char

        prev_char = char

    print(result)
