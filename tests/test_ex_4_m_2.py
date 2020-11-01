import unittest
from unittest.mock import patch

import src.example_4_module_2


class TestEx4M2(unittest.TestCase):
    @patch('src.example_4_module_1.db_write', return_value=4)  # NB: different from the imported module!
    def test_foo(self, mock_db_write):
        x = src.example_4_module_2.foo()
        self.assertEqual(x, 4)

