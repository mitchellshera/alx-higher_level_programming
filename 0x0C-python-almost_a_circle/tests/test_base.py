#!/usr/bin/python3


import unittest
import json
import os
from models.base import Base


class TestBase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.file_name = "Base.json"

    def setUp(self):
        if os.path.exists(self.file_name):
            os.remove(self.file_name)

    def tearDown(self):
        if os.path.exists(self.file_name):
            os.remove(self.file_name)

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
            Base("10")


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

    def test_save_to_file_empty_list(self):
        Base.save_to_file([])
        self.assertTrue(os.path.exists(self.file_name))
        with open(self.file_name, "r") as file:
            json_data = file.read()
            self.assertEqual(json_data, "[]")

    def test_save_to_file_non_empty_list(self):
        b1 = Base()
        b2 = Base(10)
        Base.save_to_file([b1, b2])
        self.assertTrue(os.path.exists(self.file_name))
        with open(self.file_name, "r") as file:
            json_data = file.read()
            expected_json = '[{"id": 1}, {"id": 10}]'
            self.assertEqual(json_data, expected_json)

    def test_load_from_file_non_existing_file(self):
        obj_list = Base.load_from_file()
        self.assertEqual(obj_list, [])

    def test_load_from_file_existing_file(self):
        b1 = Base()
        b2 = Base(10)
        Base.save_to_file([b1, b2])

        obj_list = Base.load_from_file()
        self.assertEqual(len(obj_list), 2)
        self.assertEqual(obj_list[0].id, 1)
        self.assertEqual(obj_list[1].id, 10)

    def test_load_from_file_invalid_json(self):
        with open(self.file_name, "w") as file:
            file.write("Invalid JSON")

        obj_list = Base.load_from_file()
        self.assertEqual(obj_list, [])

    def test_create(self):
        dictionary = {'id': 1, 'width': 5, 'height': 3, 'x': 2, 'y': 3}
        b = Base.create(**dictionary)
        self.assertEqual(b.id, 1)
        self.assertEqual(b.width, 5)
        self.assertEqual(b.height, 3)
        self.assertEqual(b.x, 2)
        self.assertEqual(b.y, 3)

    def test_create_from_csv_row(self):
        row = ['1', '5', '3', '2', '3']
        b = Base.create_from_csv_row(row)
        self.assertEqual(b.id, 1)
        self.assertEqual(b.width, 5)
        self.assertEqual(b.height, 3)
        self.assertEqual(b.x, 2)
        self.assertEqual(b.y, 3)

    def test_save_to_file_csv_empty_list(self):
        Base.save_to_file_csv([])
        self.assertTrue(os.path.exists("Base.csv"))
        with open("Base.csv", "r") as file:
            csv_data = file.read()
            self.assertEqual(csv_data, "")

    def test_save_to_file_csv_non_empty_list(self):
        b1 = Base()
        b2 = Base(10)
        Base.save_to_file_csv([b1, b2])
        self.assertTrue(os.path.exists("Base.csv"))
        with open("Base.csv", "r") as file:
            csv_data = file.read()
            expected_csv = "1,0,0,0,0\n10,0,0,0,0\n"
            self.assertEqual(csv_data, expected_csv)


if __name__ == '__main__':
    unittest.main()
