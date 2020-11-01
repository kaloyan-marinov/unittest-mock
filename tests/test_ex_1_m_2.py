import unittest
from unittest.mock import patch

from src.example_1_module_1 import get_fixed_number, CHARACTER
from src.example_1_module_2 import build_str_of_random_length


class TestEx1M2(unittest.TestCase):
    @patch('src.example_1_module_2.randint', side_effect=get_fixed_number)
    def test_build_str_of_random_length(self, mock_randint):
        random_str = build_str_of_random_length(CHARACTER)

        expected_length = get_fixed_number()
        expected_str = expected_length * CHARACTER
        self.assertEqual(random_str, expected_str)

