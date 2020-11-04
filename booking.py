# from beautifultable import BeautifulTable
import click

# TODO
# Rewrite to use click module


# Define what arguments are valid and their help message
@click.command()
@click.option('-b', '--book', help='Book a store')
def book(book):
    """Book a store"""
    click.echo(f'Book store {book}')


@click.option('-c', '--change', help='Change the values in the booking\
    table for a unit')
def change(change):
    """Change a booked store"""
    click.echo(f'Changing booking of store {change}')


@click.option('-d', '--drop', help='Drop a booking of a specified unit.\
    This deletes all info about a unit')
def drop(drop):
    """Drop a booking of a store"""
    click.echo(f'Dropping booking of store {drop}')


@click.option('-l', '--list', help='List the whole booking table or only\
    for a unit')
def list():
    """List all stores and their bookings"""
    click.echo('List command passed')


@click.option('-v', '--verbose', is_flag=True, help='Increase output verbosity for\
    debugging purposes.')
def verbose():
    """Does nothing yet"""
    click.echo('Verbose command passed')


if __name__ == "__main__":
    list()
