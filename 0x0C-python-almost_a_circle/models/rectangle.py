#!/usr/bin/python3


from models.base import Base


class Rectangle(Base):
    """Rectangle class that inherits from Base."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize a Rectangle object.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
            x (int): Optional. x-coordinate of the rectangle's position.
            y (int): Optional. y-coordinate of the rectangle's position.
            id (int): Optional. ID value to assign to the instance.

        Calls the super class with `id` to utilize the logic of the `__init__` method in the Base class.
        Assigns the provided arguments `width`, `height`, `x`, and `y` to the corresponding attributes.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter for the width attribute."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for the width attribute."""
        if not isinstance(value, int):
            raise TypeError("width must be an interger.")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter for the height attribute."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for the height attribute."""
        if not isinstance(value, int):
            raise TypeError("height must be an interger.")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter for the x attribute."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for the x attribute."""
        if not isinstance(value, int):
            raise TypeError("x must be an interger.")
        if value <= 0:
            raise ValueError("x must be > 0")
        self.__x = value

    @property
    def y(self):
        """Getter for the y attribute."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for the y attribute."""
        if not isinstance(value, int):
            raise TypeError("y must be an interger.")
        if value <= 0:
            raise ValueError("y must be > 0")
        self.__y = value

    def area(self):
        """calculates the area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """print a display of the rectangle"""
        print(("\n" * self.__y) +
              "\n".join(((" " * self.__x) + ("#" * self.__width))
                        for i in range(self.__height)))
    def __str__(self):
        """
        Return a string representation of the Rectangle.

        Returns:
            str: String representation of the Rectangle instance.
        """
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """
        Update the attributes of the Rectangle.

        Args:
            *args: Variable length argument list for no-keyword arguments.
            **kwargs: Variable length keyworded argument list for key-value arguments.

        If *args exists and is not empty, the attributes are assigned based on the no-keyword arguments in the following order:
        1st argument -> id attribute
        2nd argument -> width attribute
        3rd argument -> height attribute
        4th argument -> x attribute
        5th argument -> y attribute

        If **kwargs exists, the attributes are assigned based on the key-value arguments in any order.
        Each key represents an attribute of the Rectangle instance.
        """
        if args:
            attributes = ['id', 'width', 'height', 'x', 'y']
            for i, arg in enumerate(args):
                setattr(self, attributes[i], arg)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
        
    def to_dictionary(self):
        """dictionary representation of a Rectangle"""
        d = {}
        d["id"] = self.id
        d["width"] = self.width
        d["height"] = self.height
        d["x"] = self.x
        d["y"] = self.y
        return d