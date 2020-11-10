import unittest
from click.testing import CliRunner
from booking import arg_handler, book, list

test_tuple_full = ('a', 'b', 'c')
test_tuple_missing_one = ('a', 'b')
test_tuple_missing_two = ('a')
test_tuple_missing_three = ()
store = 'a'


class TestBooking(unittest.TestCase):
    """Nothing here will work right now as the code has undergone major changes"""

    def test_arg_handler_full(self):
        """Test the arg_handler function when all args are given"""
        self.assertEqual(arg_handler(test_tuple_full), [
                         'a', 'b', 'c'], 'should be [a, b, c]')

    def test_book_full(self):
        """Test the book command with all args provided"""
        runner = CliRunner()
        result = runner.invoke(book, [test_tuple_full])
        self.assertEqual(result.exit_code, 0, 'Should be zero')
        self.assertEqual(
            result.output, f'Booking store {test_tuple_full[0]} to {test_tuple_full[1]} with comment {test_tuple_full[2]}\n')

    def test_book_missing_one(self):
        """Test the book command with one arg missing"""
        runner = CliRunner()
        result = runner.invoke(book, [test_tuple_missing_one], input='c')
        self.assertEqual(result.exit_code, 0, 'Should be zero')
        # assertIn to avoid having to deal asserting the input prompt and such
        self.assertIn(
            f'Booking store {test_tuple_full[0]} to {test_tuple_full[1]} with comment {test_tuple_full[2]}\n', result.output)

    def test_book_missing_two(self):
        """Test the book command with two args missing"""
        runner = CliRunner()
        result = runner.invoke(book, [test_tuple_missing_two], input="b\nc")
        self.assertEqual(result.exit_code, 0, 'Should be zero')
        # assertIn to avoid having to deal asserting the input prompt and such
        self.assertIn(
            f'Booking store {test_tuple_full[0]} to {test_tuple_full[1]} with comment {test_tuple_full[2]}\n', result.output)

    def test_book_missing_three(self):
        """Test the book command with two args missing"""
        runner = CliRunner()
        result = runner.invoke(
            book, [test_tuple_missing_three], input="a\nb\nc")
        self.assertEqual(result.exit_code, 0, 'Should be zero')
        # assertIn to avoid having to deal asserting the input prompt and such
        self.assertIn(
            f'Booking store {test_tuple_full[0]} to {test_tuple_full[1]} with comment {test_tuple_full[2]}\n', result.output)

    def test_list_empty(self):
        """Test the list command without specifying a store"""
        runner = CliRunner()
        result = runner.invoke(list, [])
        assert result.exit_code == 0
        assert result.output == 'List all command passed\n'

    def test_list_specified(self):
        """Test the list command without specifying a store"""
        runner = CliRunner()
        result = runner.invoke(list, [store])
        assert result.exit_code == 0
        assert result.output == f'List store {store} command passed\n'

    def test_create_table(self):
        #dict = {'Store:': 'book_list[0].upper()', 'name': 'book_list[1]',
                                                  'comment': 'book_list[2]', "new": 'ny sak'}

        #create_table([dicta])
        pass


if __name__ == "__main__":
    unittest.main()
