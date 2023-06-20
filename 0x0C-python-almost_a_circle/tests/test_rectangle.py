#!/usr/bin/python3


import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test_constructor(self):
        r = Rectangle(10, 20, 5, 7, 1)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 20)
        self.assertEqual(r.x, 5)
        self.assertEqual(r.y, 7)
        self.assertEqual(r.id, 1)

    def test_width_validation(self):
        with self.assertRaises(ValueError):
            r = Rectangle(-10, 20, 5, 7)
        with self.assertRaises(ValueError):
            r = Rectangle(0, 20, 5, 7)
        with self.assertRaises(TypeError):
            r = Rectangle("10", 20, 5, 7)

    def test_height_validation(self):
        with self.assertRaises(ValueError):
            r = Rectangle(10, -20, 5, 7)
        with self.assertRaises(ValueError):
            r = Rectangle(10, 0, 5, 7)
        with self.assertRaises(TypeError):
            r = Rectangle(10, "20", 5, 7)

    def test_x_validation(self):
        with self.assertRaises(ValueError):
            r = Rectangle(10, 20, -5, 7)
        with self.assertRaises(TypeError):
            r = Rectangle(10, 20, "5", 7)

    def test_y_validation(self):
        with self.assertRaises(ValueError):
            r = Rectangle(10, 20, 5, -7)
        with self.assertRaises(TypeError):
            r = Rectangle(10, 20, 5, "7")

    def test_area(self):
        r = Rectangle(10, 20)
        self.assertEqual(r.area(), 200)

    def test_display(self):
        r = Rectangle(3, 2)
        expected_output = "###\n###\n"
        with self.assertLogs() as log:
            r.display()
        self.assertEqual(log.output, [expected_output])

    def test_update(self):
        r = Rectangle(10, 20, 5, 7, 1)
        r.update(2, 15, 25, 10, 12)
        self.assertEqual(r.width, 15)
        self.assertEqual(r.height, 25)
        self.assertEqual(r.x, 10)
        self.assertEqual(r.y, 12)
        self.assertEqual(r.id, 2)

    def test_update_kwargs(self):
        r = Rectangle(10, 20, 5, 7, 1)
        r.update(width=15, height=25, x=10, y=12)
        self.assertEqual(r.width, 15)
        self.assertEqual(r.height, 25)
        self.assertEqual(r.x, 10)
        self.assertEqual(r.y, 12)

    def test_to_dictionary(self):
        r = Rectangle(10, 20, 5, 7, 1)
        expected_dict = {"id": 1, "width": 10, "height": 20, "x": 5, "y": 7}
        self.assertEqual(r.to_dictionary(), expected_dict)


if __name__ == '__main__':
    unittest.main()
