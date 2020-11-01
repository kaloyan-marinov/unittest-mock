"""
This module illustrates how to handle a situation, where a lot of things need to be
mocked.

Furthermore, 2 approaches to handling that situation are demonstrated.
Those approaches are identical in functionality.
The first approach does not follow the "Don't repeat yourself" principle as closely as
the second approach.
So the second approach is preferable over the first one.
"""

import unittest
from unittest.mock import patch

from src.example_6_module_2 import introduce_as_str, introduce_as_json


@patch('src.example_6_module_2.name', return_value='N')
@patch('src.example_6_module_2.birthday', return_value='B')
@patch('src.example_6_module_2.address', return_value='A')
class TestEx6M2Option4Approach1(unittest.TestCase):
    def test_introduce_as_str(self, mock_address, mock_birthday, mock_name):
        s = introduce_as_str()
        self.assertEqual(s, 'Hello, my name is N. I was born on B. My address is A.')
    
    def test_introduce_as_json(self, mock_address, mock_birthday, mock_name):
        d = introduce_as_json()
        self.assertEqual(d, {'name': 'N', 'birthday': 'B', 'address': 'A'})


class TestEx6M2Option4Approach2(unittest.TestCase):
    """
    how to call >> option 4: manual start/stop
    """
    def setUp(self):
        mock_name = patch('src.example_6_module_2.name', return_value='N').start()
        mock_birthday = patch(
            'src.example_6_module_2.birthday', return_value='B'
        ).start()
        mock_address = patch('src.example_6_module_2.address', return_value='A').start()

        # https://docs.python.org/3/library/unittest.mock-examples.html emphasizes
        # you must ensure that the patching is “undone” by calling stop.
        # This can be fiddlier than you might think, because if an exception is raised
        # in the `setUp`, then `tearDown` is not called.
        # `unittest.TestCase.addCleanup()` makes this easier:
        self.addCleanup(patch.stopall)
        # https://docs.python.org/3/library/unittest.html says
        # If `setUp()` fails, meaning that `tearDown()` is not called,
        # then any cleanup functions added will still be called.
    
    def test_introduce_as_str(self):
        s = introduce_as_str()
        self.assertEqual(s, 'Hello, my name is N. I was born on B. My address is A.')
    
    def test_introduce_as_json(self):
        d = introduce_as_json()
        self.assertEqual(d, {'name': 'N', 'birthday': 'B', 'address': 'A'})

