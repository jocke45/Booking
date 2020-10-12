from argparse import ArgumentParser
from beautifultable import BeautifulTable
import yaml

# TODO
# Change command that changes platform/comment/environment
# Fix so that argument cleaning is handled in function
# Use actual database (PosgresSQL)

# TESTING
# Sub command for list, e.g. listing all "db" envs or how many units Joakim has booked

# Define what arguments are valid and their help message
parser = ArgumentParser(
    prog='Booking', usage='%(prog)s [command] <options>', description='A program for listing and booking units')
parser.add_argument("-b", "--book", nargs=5, type=str,
                    help="Book a specified unit to a name")
parser.add_argument("-c", "--change", nargs="+", default='not_specified', type=str,
                    help="Change the values in the booking table for a unit")
parser.add_argument("-d", "--drop", nargs=1, type=str,
                    help="Drop a booking of a specified unit. This deletes all info about a unit")
parser.add_argument("-l", "--list", nargs="?", default='not_specified', type=str,
                    help="List the whole booking table or only for a unit")
parser.add_argument("-v", "--verbose", action="store_true",
                    help="increase output verbosity")
parser.add_argument

args = parser.parse_args()

# Variables
in_file = './table.yaml'
out_file = './unit_file.yaml'
# Convert input to upper case if it exists
# Book input
try:
    book_unit = args.book[0].upper()
except TypeError as identifier:
    book_unit = False
# Drop input
try:
    drop_unit = args.drop[0].upper()
except TypeError as identifier:
    drop_unit = False
# List input
try:
    list_unit = args.list.upper()
except AttributeError as identifier:
    list_unit = False


# Functions
# Create table function
def create_table(dict, full):
    """This function creates a table of the booking schedule for
    one unit or all units and prints it"""
    table = BeautifulTable(maxwidth=100)
    table.set_style(BeautifulTable.STYLE_BOX)
    table.column_headers = ["unit", "Booker", "Environment",
                            "unit name", "Platform", "Comment", "Start date", "End date"]
    if full:
        for unit in dict:
            table.append_row([*dict[unit].values()])
    else:
        table.append_row([*dict.values()])
    print(table)
    return


# Book command
def book_command(book_args, book_unit_list, unit):
    if not unit:
        print('Please specify the unit that you want to book.')
    else:
        if unit in book_unit_list:
            if (book_unit_list[unit]['Booker'] not in (None, 'Free', '', ' ')) and \
                    (book_unit_list[unit]['Booker'] != book_args.book[1]):
                print('Warning: unit already booked to',
                      book_unit_list[unit]['Booker'])
            print('Changing booking of unit', unit)
            book_unit_list[unit]['Booker'] = book_args.book[1]
            book_unit_list[unit]['Comment'] = book_args.book[2]
            book_unit_list[unit]['StartDate'] = book_args.book[3]
            book_unit_list[unit]['EndDate'] = book_args.book[4]
            write_booking(out_file, book_unit_list)
            create_table(book_unit_list[unit], 0)
        else:
            print('No unit matching that name was found.')


# Change command
def change_command(change_args, change_unit_list):
    unit = change_args[0].upper()
    if unit in change_unit_list:
        for i in change_unit_list[unit]:
            if i in ('name', 'booker'):
                print(change_unit_list[unit]['Booker'])
    else:
        print('No unit matching that name was found.')


# Drop command
def drop_command(drop_unit_list, unit):
    if not unit:
        print('Please specify the unit that should be cleared.')
    else:
        if unit in drop_unit_list:
            print('Clearing booking of unit ', unit)
            drop_unit_list[unit]['Booker'] = ' '
            drop_unit_list[unit]['Comment'] = ' '
            drop_unit_list[unit]['StartDate'] = ' '
            drop_unit_list[unit]['EndDate'] = ' '
            write_booking(out_file, drop_unit_list)
            create_table(drop_unit_list[unit], 0)
        else:
            print('No unit matching that name was found.')


# List command
def list_command(list_unit_list, unit):
    if not unit:
        create_table(list_unit_list, 1)
    else:
        if unit in list_unit_list:
            create_table(list_unit_list[unit], 0)
        else:
            print('No unit matching that name was found.')


# Verbose command
def verbose_command(verbose_args, verbose_unit_list, verbose_list_unit, verbose_book_unit):
    print('')
    print('in file:', in_file, 'and out file:', out_file)
    print('')
    print(verbose_args)
    print('')
    print('args.list is of type: ', type(verbose_args.list))
    print('')
    print('args.book is of type: ', type(verbose_args.book))
    print('')
    print('args.drop is of type: ', type(verbose_args.drop))
    print('')
    print('unit list is of type: ', type(verbose_unit_list))
    print('')
    print('units available:')
    for unit in verbose_unit_list:
        print(verbose_unit_list[unit])
    print('')
    print('Specified list_unit is: ', verbose_list_unit)
    print('')
    print('Specified book_unit is:', verbose_book_unit)
    print('')


# Write booking schedule to file
def write_booking(write_out_file, write_unit_list):
    with open(write_out_file, 'w') as write_file:
        yaml.dump(write_unit_list, write_file, sort_keys=False)


with open(in_file) as file:
    # The FullLoader parameter handles the conversion from YAML
    # scalar values to Python the dictionary format
    global unit_list
    unit_list = yaml.full_load(file)

# Handling of commands
# Verbose command
# Placing this first as this should be done first to not make other passed argument output hard to read
if args.verbose:
    verbose_command(args, unit_list, list_unit, book_unit)

# Book command
if args.book:
    book_command(args, unit_list, book_unit)

# Drop command
if args.change != 'not_specified':
    change_command(args.change, unit_list)

# Drop command
if args.drop:
    drop_command(unit_list, drop_unit)

# List command
if args.list != 'not_specified':
    list_command(unit_list, list_unit)
