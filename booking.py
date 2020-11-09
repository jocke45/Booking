import beautifultable
import click
import os
import pymongo
from handle_db import update_store, find_all_stores, find_store

# TODO
# Add beautifultable prints
# Read data from mongoDB
# Use dicts instead of list where possible

####################
# Helper functions #
####################


def arg_handler(args):
    """Give the user a chance to input missing args"""
    # convert the input tuple to a list
    store_list = list(args)
    # all args are provided, return the original list
    if len(store_list) > 2:
        return store_list
    click.echo('Missing arguments, please enter the following')
    # Otherwise get the args needed from the user
    if len(store_list) < 1:
        store_list.append(click.prompt("Store name"))
    if len(store_list) < 2:
        store_list.append(click.prompt("Your name"))
    if len(store_list) < 3:
        store_list.append(click.prompt("Comment"))
    return store_list

# This might be a decorator later


def verbose(func):
    """Does nothing yet"""
    # TODO print all the things
    return

############
# Commands #
############


@click.group()
def main():
    print('I main')
    pass


@main.command()
@click.argument('book_store', nargs=-1)
def book(book_store):
    """Book a store."""
    book_list = arg_handler(book_store)
    result = update_store(book_list)
    if not result:
        click.echo('A store by that name was not found')
    else:
        click.echo(
            f'Booking store {book_list[0]} to {book_list[1]} with comment {book_list[2]}')


@main.command()
@click.argument('change_store', nargs=-1)
def change(change_store):
    """Change the booking of a store."""
    change_list = arg_handler(change_store)
    result = update_store(change_list)
    if not result:
        click.echo('A store by that name was not found')
    else:
        click.echo(
            f'Changing booking of store {change_list[0]} to {change_list[1]} with comment {change_list[2]}')


@main.command()
@click.argument('drop_store', nargs=-1)
def drop(drop_store):
    """Drop a booking of a store.
    This deletes all info about a unit"""
    if not drop_store:
        drop_store = click.prompt('Store')
    click.echo(
        f'You are about to delete any booking or comment one store {drop_store[0]}.')
    if click.prompt('Proceed? \n[Y/n]').casefold() in {'y', 'yes'}:
        click.echo(f'Removed booking of store {drop_store[0]}')


@main.command()
@click.argument('list_store', nargs=-1)
def show(list_store):
    """List all or just one stores booking information."""
    if not list_store:
        click.echo('List all command passed')
        click.echo(find_all_stores())
    else:
        click.echo(f'List store {list_store[0]} command passed')
        result = find_store(list_store[0])
        if not result[0]:
            click.echo('Did not find a store with the specified name')
        else:
            click.echo(result)


@main.command()
@click.argument('a')
def test(a):
    print(f'in test {a}')


if __name__ == "__main__":
    main()
