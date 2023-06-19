#!/usr/bin/python3


class Base:
    """Base class for managing id attribute in all future classes."""

    __nb_objects = 0  # Private class attribute to track the number of objects created

    def __init__(self, id=None):
        """
        Initialize a Base object.

        Args:
            id (int): Optional. ID value to assign to the instance.

        If `id` is provided, assign it to the public instance attribute `id`.
        Otherwise, increment the `__nb_objects` attribute and assign the new value to `id`.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
