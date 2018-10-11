# Libraries
import os
import argparse
import configparser
import shutil
import urllib
import fire

# Modules
import core

# Argument parsing

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog='maid',
        description='Maid - Package Manager',
        epilog='Example: TBA')
    parser.add_argument(
        '--version',
        action='version',
        version='%(prog)s Pre-Alpha')
    parser.add_argument(
        '--force',
        action='store_true'
    )
    subparsers = parser.add_subparsers(
        help='sub-command help',
        title='command',
        required=True,
        metavar='<command>')

    add_parse = subparsers.add_parser('add', help='Add package')
    add_parse.add_argument(
        'package',
        type=str,
        help='Url to package',
        metavar='<url>')
    # nargs='+'
    add_parse.set_defaults(func=core.get)

    rem_parse = subparsers.add_parser('rem', help='Remove package')
    rem_parse.add_argument(
        'package',
        type=str,
        help='Package name',
        metavar='<pkg_name>')
    # nargs='+'
    rem_parse.set_defaults(func=core.rem)

    que_parse = subparsers.add_parser('que', help='Query package')
    que_parse.add_argument(
        'package',
        type=str,
        help='Package name',
        metavar='<pkg_name>',
        nargs='?')
    que_parse.set_defaults(func=core.query, package='.*?')

    cle_parse = subparsers.add_parser(
        'cle', help='Clear temporary package downloads')
    cle_parse.set_defaults(func=core.clear)

    args = parser.parse_args()
    if 'package' in args:
        args.func(args.package)
    else:
        args.func()
