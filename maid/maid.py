# Libraries
import os
import argparse
import configparser
import shutil

# Modules
import core
# from config import maidConfDir, maidDir, maidPackDir, maidTempDir, appPath

# Global variable


parser = argparse.ArgumentParser(
    prog='Maid', description='Maid - Package Manager')
parser.add_argument('--version', action='version',
                    version='%(prog)s Pre-Alpha')
subparsers = parser.add_subparsers(
    help='sub-command help',
    title='command',
    required=True,
    metavar='<command>')
subparsers.add_parser('add', help='Add package')
subparsers.add_parser('rem', help='Remove package')

args = parser.parse_args()
