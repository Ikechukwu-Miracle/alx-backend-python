#!/usr/bin/env python3
"""Unittest module that is parameterized"""
import Unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAcessNestedMap(Unittest.Testcase):
    """Class for testing the nested map"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])

    def test_access_nested_map(self, nested_map, path, expected_result):
        """Test method that for expected results"""

        self.assertEqual(access_nested_map(nested_map, path), expected_result)
