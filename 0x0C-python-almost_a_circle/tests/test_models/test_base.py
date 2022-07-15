#!/usr/bin/python3
"""unit test for base class"""

import unittest
import json
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class Test_Base(unittest.TestCase):

    def test_id(self):
        """test if the id works properly"""
        a = Base()
        b = Base()
        c = Base(20)
        d = Base()
        self.assertEqual(a.id, 1)
        self.assertEqual(b.id, 2)
        self.assertEqual(c.id, 20)
        self.assertEqual(d.id, 3)

    def test_ToJsonString(self):
        """test if to_json_string works properly"""
        test = Base.to_json_string([])
        self.assertEqual(test, "[]")
        test = base.to_json_string(None)
        self.assertEqual(test, "[]")
        test2 = [{'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8}]
        test = Base.to_json_string(test2)
        self.assertEqual(test, json.dumps(test2))
        test = Base.to_json_string([{}])
        self.assertEqual(test, json.dumps([{}]))
        test = Base.to_json_string([None])
        self.assertEqual(test, json.dumps([None]))
        test = Base.to_json_string([{"a": None}])
        self.assertEqual(test, json.dumps([{"a": None}]))

    def test_fromJsonString(self):
        Base._Base__nb_objects = 0
        temp = Base.from_json_string(json.dumps([]))
        self.assertEqual(temp, [])
        temp = Base.from_json_string(None)
        self.assertEqual(temp, [])
        temp2 = [{'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8}]
        json_str = json.dumps(temp2)
        temp = Base.from_json_string(json_str)
        self.assertEqual(temp, json.loads(json_str))

if __name__ == "__main__":
    unittest.main()
