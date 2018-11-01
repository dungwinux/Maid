# Libraries
import os
import argparse
import configparser
import urllib

# Modules
import core

# Argument parsing

if __name__ == "__main__":
    # Declare Argument Parser
    parser = argparse.ArgumentParser(
        prog='maid',
        description='Maid - Package Manager',
        epilog='Program is still in Pre-Alpha. WIP')
    # --version argument
    parser.add_argument(
        '--version',
        action='version',
        version='%(prog)s Pre-Alpha')
    # TODO: --force argument
    # parser.add_argument(
    #     '--force',
    #     action='store_true'
    # )
    # Add subparser to main Parser
    subparsers = parser.add_subparsers(
        help="Maid's sub-command",
        title='command',
        required=True,
        metavar='<command>')

    # add sub-command
    add_parse = subparsers.add_parser(
        'add', help='Add package from local path')
    add_parse.add_argument(
        'package',
        type=str,
        help='Path to package',
        metavar='<path>')
    # nargs='+'
    add_parse.set_defaults(func=core.get)

    # get sub-command
    get_parse = subparsers.add_parser(
        'get', help='Get package from url')
    get_parse.add_argument(
        'package',
        type=str,
        help='Path to package',
        metavar='<url>')
    # nargs='+'
    add_parse.set_defaults(func=core.add)

    # rem sub-command
    rem_parse = subparsers.add_parser(
        'rem', help='Remove package from storage')
    rem_parse.add_argument(
        'package',
        type=str,
        help='Package name',
        metavar='<pkg_name>')
    # nargs='+'
    rem_parse.set_defaults(func=core.rem)

    # query sub-command
    que_parse = subparsers.add_parser(
        'que', help='Query package from storage')
    que_parse.add_argument(
        'package',
        type=str,
        help='Package name',
        metavar='<pkg_name>',
        nargs='?')
    que_parse.set_defaults(func=core.query, package='.*?')

    # clear sub-command
    cle_parse = subparsers.add_parser(
        'cle', help='Clear temporary package downloads')
    cle_parse.set_defaults(func=core.clear)

    # Call argument parser
    args = parser.parse_args()
    # Checking for argument
    # If no argument -> clear
    # else           -> other function
    if 'package' in args:
        args.func(args.package)
    else:
        args.func()
