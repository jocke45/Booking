from beautifultable import BeautifulTable
import click
from handle_db import empty_unit, find_all_units, find_unit, update_unit


####################
# Helper functions #
####################


def arg_handler(args):
    """
    Take the user input and return it as a dictionary
    Give the user a chance to input missing args, if any
    """
    unit_list = {}
    # all args are provided, return the original list
    if 3 < len(args):
        unit_list['_id'] = args[0]
        unit_list['booker'] = args[1]
        unit_list['comment'] = " ".join(args[2:-1])
        unit_list['date'] = args[-1]
        return unit_list
    # Otherwise get the args needed from the user
    click.echo('Missing arguments, please enter the following')
    # Define the keys for the dict
    unit_list_keys = ['_id', 'booker', 'comment', 'date']
    unit_list = dict(zip(unit_list_keys, args))
    if len(args) < 1:
        unit_list['_id'] = click.prompt("Unit name")
    if len(args) < 2:
        unit_list['booker'] = click.prompt("Your name")
    if len(args) < 3:
        unit_list['comment'] = click.prompt("Comment")
    if len(args) < 4:
        unit_list['date'] = click.prompt("Date")
    return unit_list


def create_table(schedule_list):
    """Create a BeatifulTable from the provided schedule list"""
    table = BeautifulTable()
    table.set_style(BeautifulTable.STYLE_BOX)
    # Dynamically create the column header
    # If the dictionaries in schedule_list does not have the same
    # keys it will look dumb, but that's on you then
    # Also, show header '_id' as 'Unit' instead
    table.columns.header = [
        'Unit' if key == '_id' else key.capitalize() for key in schedule_list[0]]
    for i in schedule_list:
        table.rows.append(i.values())
    return table


############
# Commands #
############


@ click.group()
def main():
    pass


@ main.command()
@ click.argument('book_unit', nargs=-1)
def book(book_unit):
    """Book a unit."""
    book_list = arg_handler(book_unit)
    result = update_unit(book_list)
    if not result:
        click.echo('A unit by that name was not found')
    else:
        click.echo(create_table([book_list]))


@ main.command()
@ click.argument('change_unit', nargs=-1)
def change(change_unit):
    """Change the booking of a unit. This does that same thing as 'book'"""
    book(change_unit)


@ main.command()
@ click.argument('drop_unit', nargs=-1)
def drop(drop_unit):
    """Drop a booking of a unit.
    This deletes all info about a unit"""
    if not drop_unit:
        drop_unit = click.prompt('Unit')
    click.echo(
        f'You are about to delete any booking or comment on unit {drop_unit[0]}.')
    if click.prompt('Proceed? \n[Y/n]').casefold() in {'y', 'yes'}:
        if empty_unit(drop_unit[0]):
            click.echo(f'Removed booking of unit {drop_unit[0]}')
        else:
            click.echo('Did not find a unit with the specified name')


@ main.command()
@ click.argument('show_unit', nargs=-1)
def show(show_unit):
    """Show booking information of one or all units"""
    if not show_unit:
        result = find_all_units()
        click.echo(create_table(result))
    else:
        result = find_unit(show_unit[0])
        if not result[0]:
            click.echo('Did not find a unit with the specified name')
        else:
            click.echo(create_table(result))


if __name__ == "__main__":
    main()
