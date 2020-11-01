import unittest
from unittest.mock import patch

import src.example_3_module_2


class TestEx3M2(unittest.TestCase):
    @patch('src.example_3_module_2.db_write', return_value=3)
    def test_foo(self, mock_db_write):
        x = src.example_3_module_2.foo()
        self.assertEqual(x, 3)

