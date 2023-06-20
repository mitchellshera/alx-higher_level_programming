#!/usr/bin/python3


import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    def test_constructor(self):
        s = Square(5, 2, 3, 1)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)
        self.assertEqual(s.id, 1)

    def test_size_validation(self):
        with self.assertRaises(ValueError):
            s = Square(-5, 2, 3)
        with self.assertRaises(ValueError):
            s = Square(0, 2, 3)
        with self.assertRaises(TypeError):
            s = Square("5", 2, 3)

    def test_x_validation(self):
        with self.assertRaises(ValueError):
            s = Square(5, -2, 3)
        with self.assertRaises(TypeError):
            s = Square(5, "2", 3)

    def test_y_validation(self):
        with self.assertRaises(ValueError):
            s = Square(5, 2, -3)
        with self.assertRaises(TypeError):
            s = Square(5, 2, "3")

    def test_area(self):
        s = Square(5)
        self.assertEqual(s.area(), 25)

    def test_display(self):
        s = Square(3)
        expected_output = "###\n###\n###\n"
        with self.assertLogs() as log:
            s.display()
        self.assertEqual(log.output, [expected_output])

    def test_update(self):
        s = Square(5, 2, 3, 1)
        s.update(2, 7, 4, 5)
        self.assertEqual(s.size, 7)
        self.assertEqual(s.x, 4)
        self.assertEqual(s.y, 5)
        self.assertEqual(s.id, 2)

    def test_update_kwargs(self):
        s = Square(5, 2, 3, 1)
        s.update(size=7, x=4, y=5)
        self.assertEqual(s.size, 7)
        self.assertEqual(s.x, 4)
        self.assertEqual(s.y, 5)

    def test_to_dictionary(self):
        s = Square(5, 2, 3, 1)
        expected_dict = {"id": 1, "size": 5, "x": 2, "y": 3}
        self.assertEqual(s.to_dictionary(), expected_dict)


if __name__ == '__main__':
    unittest.main()
