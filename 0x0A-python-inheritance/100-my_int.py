#!/usr/bin/python3


class MyInt(int):
    """
    A custom integer class that inherits from the built-in int class.
    The == and != operators are inverted.
    """

    def __eq__(self, other):
        """
        Override the == operator.
        Returns True if the values are not equal; otherwise, False.
        """
        return int(self) != int(other)

    def __ne__(self, other):
        """
        Override the != operator.
        Returns True if the values are equal; otherwise, False.
        """
        return int(self) == int(other)
