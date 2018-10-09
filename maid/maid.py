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
        prog='maid', description='Maid - Package Manager')
    parser.add_argument('--version', action='version',
                        version='%(prog)s Pre-Alpha')
    subparsers = parser.add_subparsers(
        help='sub-command help',
        title='command',
        required=True,
        metavar='<command>')

    add_parse = subparsers.add_parser('add', help='Add package')
    add_parse.add_argument('url', type=str, help='Url to package', metavar='<url>')
    # add_parse.set_defaults(func=core.get)

    rem_parse = subparsers.add_parser('rem', help='Remove package')
    rem_parse.add_argument('pkg_name', type=str, help='Package name', metavar='<pkg_name>')
    # rem_parse.set_defaults(func=core.)

    # args = parser.parse_args()