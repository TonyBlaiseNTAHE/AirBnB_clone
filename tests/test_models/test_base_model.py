#!/usr/bin/python3
"""
importing unittest module
"""

import unittest
from datetime import datetime
from uuid import uuid4
from time import sleep
from models.base_model import BaseModel


class BaseModelTest(unittest.TestCase):
    """testing class for all the BaseModel methods
    """
    def test_init(self):
        """ testing init method"""
        obj = BaseModel()

        self.assertIsInstance(obj, BaseModel)
        self.assertIsInstance(obj.id, str)
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)

    def test_save(self):
        """ test save method"""
        obj = BaseModel()
        sleep(1)

        now = datetime.now().replace(microsecond=0)
        obj.save()
        self.assertEqual(obj.updated_at.replace(microsecond=0), now)

    def test_dict(self):
        """ test to_dict method"""
        obj = BaseModel()
        obj.name = "mercedes"
        obj.number = 360

        my_obj = obj.to_dict()
        self.assertIsInstance(my_obj, dict)

        obj_id = my_obj['id']
        updated_at = my_obj['updated_at']
        created_at = my_obj['created_at']
        cls_name = my_obj['__class__']
        name = my_obj['name']
        number = my_obj['number']

        self.assertIsInstance(obj_id, str)
        self.assertIsInstance(updated_at, str)
        self.assertIsInstance(created_at, str)
        self.assertIsInstance(number, int)
        self.assertIsInstance(cls_name, str)


if __name__ == '__main__':
    unittest.main()
