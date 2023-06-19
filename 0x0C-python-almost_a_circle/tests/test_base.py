#!/usr/bin/python3


import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    def test_constructor_without_id(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_constructor_with_id(self):
        b = Base(10)
        self.assertEqual(b.id, 10)

    def test_constructor_with_non_integer_id(self):
        with self.assertRaises(TypeError):
            b = Base("10")

    def test_to_json_string_empty_list(self):
        json_string = Base.to_json_string([])
        self.assertEqual(json_string, "[]")

    def test_to_json_string_non_empty_list(self):
        b1 = Base()
        b2 = Base(10)
        json_string = Base.to_json_string([b1.to_dictionary(), b2.to_dictionary()])
        expected_json = '[{"id": 1}, {"id": 10}]'
        self.assertEqual(json_string, expected_json)

    def test_from_json_string_empty_string(self):
        obj_list = Base.from_json_string("")
        self.assertEqual(obj_list, [])

    def test_from_json_string_non_empty_string(self):
        json_string = '[{"id": 1}, {"id": 10}]'
        obj_list = Base.from_json_string(json_string)
        self.assertEqual(len(obj_list), 2)
        self.assertEqual(obj_list[0].id, 1)
        self.assertEqual(obj_list[1].id, 10)

    def test_create(self):
        dictionary = {'id': 1, 'size': 5, 'x': 2, 'y': 3}
        b = Base.create(**dictionary)
        self.assertEqual(b.id, 1)
        self.assertEqual(b.size, 5)
        self.assertEqual(b.x, 2)
        self.assertEqual(b.y, 3)

    def test_load_from_file_non_existing_file(self):
        obj_list = Base.load_from_file()
        self.assertEqual(obj_list, [])

    def test_load_from_file_existing_file(self):
        # Assuming Rectangle is used as an example
        obj_list = Base.load_from_file()
        self.assertEqual(len(obj_list), 2)
        self.assertEqual(obj_list[0].id, 1)
        self.assertEqual(obj_list[1].id, 2)


if __name__ == '__main__':
    unittest.main()
