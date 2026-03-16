import unittest
from unittest.mock import patch

from constants import *
from sorter import sorter


class MyTestCase(unittest.TestCase):
    @patch('sorter.input')
    def test_length_edge_case(self, mock_input):
        # mock the inputs
        mock_input.side_effect = side_effect=['150', '1', '1', '1']
        result = sorter()
        self.assertEqual(result, SPECIAL)
        self.assertEqual(mock_input.call_count, 4)


    @patch('sorter.input')
    def test_width_edge_case(self, mock_input):
        # mock the inputs
        mock_input.side_effect = side_effect=['1', '150', '1', '1']
        result = sorter()
        self.assertEqual(result, SPECIAL)
        self.assertEqual(mock_input.call_count, 4)


    @patch('sorter.input')
    def test_height_edge_case(self, mock_input):
        # mock the inputs
        mock_input.side_effect = side_effect=['1', '1', '150', '1']
        result = sorter()
        self.assertEqual(result, SPECIAL)
        self.assertEqual(mock_input.call_count, 4)


    @patch('sorter.input')
    def test_total_dim_edge_case(self, mock_input):
        # mock the inputs
        mock_input.side_effect = side_effect=['100', '100', '100', '1']
        result = sorter()
        self.assertEqual(result, SPECIAL)
        self.assertEqual(mock_input.call_count, 4)


    @patch('sorter.input')
    def test_standard_case(self, mock_input):
        # mock the inputs
        mock_input.side_effect = side_effect=['100', '100', '99', '1']
        result = sorter()
        self.assertEqual(result, STANDARD)
        self.assertEqual(mock_input.call_count, 4)


    @patch('sorter.input')
    def test_standard_case_validate_input(self, mock_input):
        # mock the inputs
        mock_input.side_effect = side_effect=['0', '100', '100', '99', '1']
        result = sorter()
        self.assertEqual(result, STANDARD)
        # extra call due to invalid input
        self.assertEqual(mock_input.call_count, 5)


    @patch('sorter.input')
    def test_mass_edge_case(self, mock_input):
        # mock the inputs
        mock_input.side_effect = side_effect=['1', '1', '1', '20']
        result = sorter()
        self.assertEqual(result, SPECIAL)
        self.assertEqual(mock_input.call_count, 4)


    @patch('sorter.input')
    def test_rejected_case(self, mock_input):
        # mock the inputs
        mock_input.side_effect = side_effect=['1', '1', '150', '20']
        result = sorter()
        self.assertEqual(result, REJECTED)
        self.assertEqual(mock_input.call_count, 4)


if __name__ == '__main__':
    unittest.main()
