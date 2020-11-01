import unittest
from unittest.mock import patch

import src.example_5_module_2


class TestEx5M2Option1AndOption2(unittest.TestCase):
    def test_foo(self):
        """
        how to call >> option 1: context manager
        """
        # Replace a function with a MagicMock.
        with patch('src.example_5_module_2.db_write', return_value=5):
            x = src.example_5_module_2.foo()
            self.assertEqual(x, 5)
        
        # Use the original function itself.
        y = src.example_5_module_2.foo()
        self.assertEqual(y, 1)
    
    @patch('src.example_5_module_2.db_write', return_value=55)
    def test_foo_2(self, mock_db_write):
        """
        how to call >> option 2: function decorator
        """
        x = src.example_5_module_2.foo()
        self.assertEqual(x, 55)


@patch('src.example_5_module_2.db_write', return_value=555)
class TestEx5M2Option3(unittest.TestCase):
    """
    how to call >> option 3: class decorator
    """
    def test_foo_1(self, mock_db_write):
        x = src.example_5_module_2.foo()
        self.assertEqual(x, 555)
    
    def test_foo_2(self, mock_db_write):
        x = src.example_5_module_2.foo() * 10
        self.assertEqual(x, 5550)

