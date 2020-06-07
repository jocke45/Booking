# https://beautifultable.readthedocs.io/

from argparse import ArgumentParser
from beautifultable import BeautifulTable
import yaml
import datetime

# Variables

parser = ArgumentParser(
    prog='Booking', usage='%(prog)s [-help] [--list] [--list STORE_NAME] ', description='A program for listing and booking the stores in the lab')
parser.add_argument("-l", "--list", nargs="?", default='not_specified', type=str,
                    help="List the whole booking table or only for a store")
parser.add_argument("-v", "--verbose", action="store_true",
                    help="increase output verbosity")
parser.add_argument

args = parser.parse_args()

# Convert input to upper case if it exists
try:
    store = args.list.upper()
except AttributeError as identifier:
    store = False


# Functions
def createTable(dict, full):
    """This function creates a table of the booking schedule for 
    one store or all stores and prints it"""
    table = BeautifulTable()
    table.column_headers = ["Store", "Booker", "Environment",
                            "Store name", "Platform", "Start date", "End date"]
    if full:
        for store in dict:
            table.append_row([*dict[store].values()])
    else:
        table.append_row([*dict.values()])
    print(table)
    return


with open(r'./table.yaml') as file:
    # The FullLoader parameter handles the conversion from YAML
    # scalar values to Python the dictionary format
    global Store_list
    Store_list = yaml.full_load(file)

if args.verbose:
    print('')
    print(args)
    print('')
    print('args.list is of type: ' + str(type(args.list)))
    print('')
    print('Store list is of type: ' + str(type(Store_list)))
    print('')
    print('Stores available:')
    for store in Store_list:
        print(Store_list[store])
    print('')
    print('Specified store is: ' + str(store))
    print('')


if args.list != 'not_specified':
    if not store:
        createTable(Store_list, 1)
    else:
        if store in Store_list:
            createTable(Store_list[store], 0)
        else:
            print('No store matching that name was found.')
