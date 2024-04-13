#!/usr/bin/env python3
"""Unittest module that is parameterized"""
import Unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAcessNestedMap(Unittest.Testcase):
    """Class for testing the nested map"""
    # unittest does not support test decorators,
    # only tests created with @parameterized.expand will be executed

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])

    def test_access_nested_map(self, map, path, expected_result):
        """Test method that for expected results"""

        actual_output = access_nested_map(map, path)
        self.assertEqual(actual_output, expected_output)
