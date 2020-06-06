#https://beautifultable.readthedocs.io/

from argparse import ArgumentParser
import yaml

# Variables

parser = ArgumentParser(
    prog='PROG', usage='booking [options]', description='A program for listing and booking the stores in the lab')
parser.add_argument("-l", "--list", dest="storename", nargs='?',
                    help="List the whole booking table or only for a store")
parser.add_argument("-v", "--verbose", action="store_true",
                    help="increase output verbosity")

args = parser.parse_args()

# Convert input to upper case
store = args.storename.upper()

with open(r'./table.yaml') as file:
    # The FullLoader parameter handles the conversion from YAML
    # scalar values to Python the dictionary format
    global Store_list
    Store_list = yaml.full_load(file)

if args.verbose:
    print('Very verbose, such text, wow')
    print(args)
    print('args.storename is: ' + str(type(args.storename)))
    print(Store_list)
    print('Store list is: ' + str(type(Store_list)))


if not store:
    for item in Store_list:
        print(item)
else:
    if store in Store_list:
        print(Store_list[store])
