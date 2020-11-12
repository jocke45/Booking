import unittest
from click.testing import CliRunner
from booking import arg_handler
from handle_db import add_unit, delete_unit, empty_unit, find_all_units, find_unit, update_unit

test_list_full = ['a', 'b', 'c', 'd']
test_unit = 'a'
test_unit_data = {'_id': 'a', 'booker': 'b', 'comment': 'c', 'date': 'd'}
test_find_unit_correct_result = {'_id': 'A',
                                 'booker': 'b', 'comment': 'c', 'date': 'd'}
arg_handler_correct_result = {'_id': 'a',
                              'booker': 'b', 'comment': 'c', 'date': 'd'}


class TestBooking(unittest.TestCase):
    """Testing all code of the booking CLI
    Unfortunately it is very ugly to assert output of beautifultable
    so we test the functions that give output to beautifultable
    and then test one print of a table"""

    def test_a(self):
        """Test the arg_handler function when all args are given"""
        self.assertEqual(arg_handler(test_list_full),
                         arg_handler_correct_result)

    def test_b(self):
        """Test add_unit"""
        self.assertEqual(add_unit(test_unit_data), 'A')

    def test_c(self):
        """Test empty_unit"""
        self.assertEqual(empty_unit(test_unit), 1)

    def test_d(self):
        """Test update_unit"""
        self.assertEqual(update_unit(test_unit_data), 1)

    def test_e(self):
        """Test find_unit"""
        self.assertEqual(find_unit(test_unit), [test_find_unit_correct_result])

    def test_z(self):
        """Test delete_unit"""
        self.assertEqual(delete_unit(test_unit), 1)


if __name__ == "__main__":
    # Make sure the test data is not already there
    delete_unit(test_unit_data['_id'])
    # Test time!
    unittest.main()
