from argparse import ArgumentParser
from beautifultable import BeautifulTable
import yaml
import datetime

# TODO
# Change command that changes platform/comment/environment
# Fix so that argument cleaning is handled in function
# TESTING
# Sub command for list, e.g. listing all "db" envs or how many stores Joakim has booked


parser = ArgumentParser(
    prog='Booking', usage='%(prog)s [command] <options>', description='A program for listing and booking the stores in the lab')
parser.add_argument("-b", "--book", nargs=5, type=str,
                    help="Book a specified store to a name")
parser.add_argument("-c", "--change", nargs="+", default='not_specified', type=str,
                    help="Change the values in the booking table for a store")
parser.add_argument("-d", "--drop", nargs=1, type=str,
                    help="Drop a booking of a specified store. This deletes all info about a store")
parser.add_argument("-l", "--list", nargs="?", default='not_specified', type=str,
                    help="List the whole booking table or only for a store")
parser.add_argument("-v", "--verbose", action="store_true",
                    help="increase output verbosity")
parser.add_argument

args = parser.parse_args()

# Variables
in_file = './table.yaml'
out_file = './store_file.yaml'
# Convert input to upper case if it exists
# Book input
try:
    book_store = args.book[0].upper()
except TypeError as identifier:
    book_store = False
# Drop input
try:
    drop_store = args.drop[0].upper()
except TypeError as identifier:
    drop_store = False
# List input
try:
    list_store = args.list.upper()
except AttributeError as identifier:
    list_store = False


# Functions
# Create table function
def createTable(dict, full):
    """This function creates a table of the booking schedule for
    one store or all stores and prints it"""
    table = BeautifulTable(max_width=100)
    table.set_style(BeautifulTable.STYLE_BOX)
    table.column_headers = ["Store", "Booker", "Environment",
                            "Store name", "Platform", "Comment", "Start date", "End date"]
    if full:
        for store in dict:
            table.append_row([*dict[store].values()])
    else:
        table.append_row([*dict.values()])
    print(table)
    return


# Book command
def bookCommand(args, Store_list, store):
    if not store:
        print('Please specify the store that you want to book.')
    else:
        if store in Store_list:
            if((Store_list[store]['Booker'] not in (None, 'Free', '', ' ')) and (Store_list[store]['Booker'] != args.book[1])):
                print('Warning: Store already booked to',
                      Store_list[store]['Booker'])
            print('Changing booking of store', store)
            Store_list[store]['Booker'] = args.book[1]
            Store_list[store]['Comment'] = args.book[2]
            Store_list[store]['StartDate'] = args.book[3]
            Store_list[store]['EndDate'] = args.book[4]
            writeBooking(out_file, Store_list)
            createTable(Store_list[store], 0)
        else:
            print('No store matching that name was found.')


# Change command
def changeCommand(args, Store_list):
    store = args[0].upper()
    if store in Store_list:
        for i in Store_list[store]:
            if(i in ('name', 'booker')):
                print(Store_list[store]['Booker'])
    else:
        print('No store matching that name was found.')


# Drop command
def dropCommand(Store_list, store):
    if not store:
        print('Please specify the store that should be cleared.')
    else:
        if store in Store_list:
            print('Clearing booking of store ', store)
            Store_list[store]['Booker'] = ' '
            Store_list[store]['Comment'] = ' '
            Store_list[store]['StartDate'] = ' '
            Store_list[store]['EndDate'] = ' '
            writeBooking(out_file, Store_list)
            createTable(Store_list[store], 0)
        else:
            print('No store matching that name was found.')


# List command
def listCommand(Store_list, store):
    if not store:
        createTable(Store_list, 1)
    else:
        if store in Store_list:
            createTable(Store_list[store], 0)
        else:
            print('No store matching that name was found.')


# Verbose command
def verboseCommand(args, Store_list, list_store, book_store):
    print('')
    print('in file:', in_file, 'and out file:', out_file)
    print('')
    print(args)
    print('')
    print('args.list is of type: ', type(args.list))
    print('')
    print('args.book is of type: ', type(args.book))
    print('')
    print('args.drop is of type: ', type(args.drop))
    print('')
    print('Store list is of type: ', type(Store_list))
    print('')
    print('Stores available:')
    for store in Store_list:
        print(Store_list[store])
    print('')
    print('Specified list_store is: ', list_store)
    print('')
    print('Specified book_store is:', book_store)
    print('')


# Write booking schedule to file
def writeBooking(out_file, Store_list):
    with open(out_file, 'w') as file:
        yaml.dump(Store_list, file, sort_keys=False)


with open(in_file) as file:
    # The FullLoader parameter handles the conversion from YAML
    # scalar values to Python the dictionary format
    global Store_list
    Store_list = yaml.full_load(file)

# Handling of commands
# Verbose command
# Placing this first as this should be done first to not make other passed argument output hard to read
if args.verbose:
    verboseCommand(args, Store_list, list_store, book_store)

# Book command
if args.book:
    bookCommand(args, Store_list, book_store)

# Drop command
if args.change != 'not_specified':
    changeCommand(args.change, Store_list)

# Drop command
if args.drop:
    dropCommand(Store_list, drop_store)

# List command
if args.list != 'not_specified':
    listCommand(Store_list, list_store)
