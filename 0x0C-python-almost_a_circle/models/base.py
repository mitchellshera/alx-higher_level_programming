#!/usr/bin/python3
"""
This module contains the "Base" class
"""


import json
import csv
import turtle


class Base:
    """A base class"""
    
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize a Base object.

        Args:
            id (int): Optional. ID value to assign to the instance.

        If `id` is not None, assign it to the public instance attribute `id`.
        Otherwise, increment `__nb_objects` and assign the new value to the public instance attribute `id`.
        """
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Convert a list of dictionaries to a JSON string.

        Args:
            list_dictionaries (list): List of dictionaries to convert.

        Returns:
            str: JSON string representation of the list of dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Save the JSON string representation of a list of objects to a file.

        Args:
            list_objs (list): List of instances to save.

        The filename is based on the class name.
        The JSON string representation of `list_objs` is written to the file.
        """
        filename = cls.__name__ + ".json"
        json_string = "[]"
        if list_objs is not None:
            json_string = cls.to_json_string([obj.to_dictionary() for obj in list_objs])
        with open(filename, "w") as file:
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """
        Convert a JSON string representation to a list of dictionaries.

        Args:
            json_string (str): JSON string representation.

        Returns:
            list: List of dictionaries represented by the JSON string.
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Create an instance with attributes set based on a dictionary.

        Args:
            **dictionary: Double pointer to a dictionary.

        Returns:
            object: Instance of the class with attributes set based on the dictionary.

        To assign the attributes, a "dummy" instance is created first.
        The `update` method is called on the "dummy" instance with the dictionary as `**kwargs`.
        This assigns the attributes using the `update` method's logic.
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        Load a list of instances from a JSON file.

        Returns:
            list: List of instances.

        The filename is based on the class name.
        If the file doesn't exist, an empty list is returned.
        Otherwise, the JSON string representation is loaded from the file.
        The list of dictionaries is converted back to instances using the `create` method.
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as file:
                json_string = file.read()
        except FileNotFoundError:
            return []
        dictionaries = cls.from_json_string(json_string)
        instances = [cls.create(**dictionary) for dictionary in dictionaries]
        return instances
    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Save the CSV representation of a list of objects to a file.

        Args:
            list_objs (list): List of instances to save.

        The filename is based on the class name.
        The CSV representation of `list_objs` is written to the file.
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            for obj in list_objs:
                writer.writerow(obj.to_csv_row())

    @classmethod
    def load_from_file_csv(cls):
        """
        Load a list of instances from a CSV file.

        Returns:
            list: List of instances.

        The filename is based on the class name.
        If the file doesn't exist, an empty list is returned.
        Otherwise, the CSV data is loaded from the file.
        The list of instances is created based on the CSV data.
        """
        filename = cls.__name__ + ".csv"
        instances = []
        try:
            with open(filename, "r", newline="") as file:
                reader = csv.reader(file)
                for row in reader:
                    instance = cls.create_from_csv_row(row)
                    instances.append(instance)
        except FileNotFoundError:
            pass
        return instances

    def to_csv_row(self):
        """
        Convert the instance to a CSV row.

        Returns:
            list: CSV row representing the instance.

        This method should be implemented in the subclasses to define the CSV row format.
        """
        raise NotImplementedError("Subclasses must implement to_csv_row method.")

    @classmethod
    def create_from_csv_row(cls, row):
        """
        Create an instance with attributes set based on a CSV row.

        Args:
            row (list): CSV row representing the instance.

        Returns:
            object: Instance of the class with attributes set based on the CSV row.

        This method should be implemented in the subclasses to create instances from CSV rows.
        """
        raise NotImplementedError("Subclasses must implement create_from_csv_row method.")

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw all the Rectangles and Squares using Turtle graphics."""
        turtle.setup(width=800, height=600)
        screen = turtle.Screen()
        screen.title("Drawing Rectangles and Squares")
        screen.bgcolor("white")

        def draw_shape(shape):
            """Draw a shape (Rectangle or Square) using turtle graphics."""
            turtle.penup()
            turtle.goto(shape.x, shape.y)
            turtle.pendown()
            turtle.fillcolor(shape.color)  # Customize the color as desired
            turtle.begin_fill()
            for _ in range(4):
                turtle.forward(shape.width)
                turtle.left(90)
            turtle.end_fill()

        for rectangle in list_rectangles:
            draw_shape(rectangle)

        for square in list_squares:
            draw_shape(square)

        turtle.done()