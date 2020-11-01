import unittest
from unittest.mock import patch

import src.example_2_module_1


class TestEx2M1(unittest.TestCase):
    @patch('src.example_2_module_1.db_write', return_value=2)
    def test_foo(self, mock_db_write):
        x = src.example_2_module_1.foo()
        self.assertEqual(x, 2)

