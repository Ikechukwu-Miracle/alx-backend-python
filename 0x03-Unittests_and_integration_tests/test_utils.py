#!/usr/bin/env python3
"""Unittest module that is parameterized"""
import unittest
from typing import Dict, Tuple, Union
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map, get_json



class TestAccessNestedMap(unittest.Testcase):
    """Class for testing the nested map"""
    # unittest does not support test decorators,
    # only tests created with @parameterized.expand will be executed

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])

    def test_access_nested_map(
            self,
            nested_map: Dict,
            path: Tuple[str],
            expected: Union[Dict, int],
            ) -> None:
        """Test method that for expected results"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])

    def test_access_nested_map_exception(
            self,
            nested_map: Dict,
            path: Tuple[str],
            exception: Exception
            ) -> None:
        """Test case for access_nested_map exceptions"""
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(str(context.exception), exception)

    
class TestGetJson(unittest.TestCase):
    """Class for testing utils.get_json method"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])

    def test_get_json(
            self,
            test_url: str,
            test_payload: Dict,
            ) -> None:
        """Test case for get_json output"""
        params = {'json.return_value': test_payload}
        with patch("requests.get", return_value=Mock(**params)) as getReq:
            self.assertEqual(get_json(test_url), test_payload)
            getReq.assert_called_once_with(test_url)
