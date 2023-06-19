#!/usr/bin/python3


from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize a Square object.

        Args:
            size (int): Size of the square.
            x (int): Optional. x-coordinate of the square's position.
            y (int): Optional. y-coordinate of the square's position.
            id (int): Optional. ID value to assign to the instance.

        Calls the super class with `id`, `x`, `y`, `width`, and `height` to utilize the logic of the `__init__` method in the Rectangle class.
        The width and height attributes are assigned the value of `size`.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for the size attribute."""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for the size attribute."""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Update the attributes of the Square.

        Args:
            *args: Variable length argument list for no-keyword arguments.
            **kwargs: Variable length keyworded argument list for key-value arguments.

        If *args exists and is not empty, the attributes are assigned based on the no-keyword arguments in the following order:
        1st argument -> id attribute
        2nd argument -> size attribute
        3rd argument -> x attribute
        4th argument -> y attribute

        If **kwargs exists, the attributes are assigned based on the key-value arguments in any order.
        Each key represents an attribute of the Square instance.
        """
        if args:
            attributes = ['id', 'size', 'x', 'y']
            for i, arg in enumerate(args):
                setattr(self, attributes[i], arg)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Return the dictionary representation of the Square.

        Returns:
            dict: Dictionary representation of the Square instance.
        """
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }

    def __str__(self):
        """
        Return a string representation of the Square.

        Returns:
            str: String representation of the Square instance.
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
