# Libraries
import os
import argparse
import configparser
import shutil

# Modules
import core
from config import *

# Global variable


def FirstTimeSetup():

    print("Running First-Time-Setup")

    cwd = os.getcwd()

    # TaskList file
    # taskList = configparser.ConfigParser()
    # taskList['list'] = {
    #     'GitPkg': 'False'}
    # with open(os.fsencode('list.conf'), 'w') as taskfile:
    #     taskfile.write(confHeader)
    #     taskList.write(taskfile)

    # Pkg maidDir
    os.chdir(maidDir)
    if not os.path.isdir(maidDir):
        os.mkdir(maidDir)

    if not os.path.isdir('list/'):
        os.mkdir('list/')
    if not os.path.isdir('pkg/'):
        os.mkdir('pkg/')

    os.chdir(cwd)


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


# Try creating global configuration
if not ReadConf():
    MakeConf()

os.chdir(maidConfDir)

# Check for prepared directory
# If not, Maid will try to create `maid` file in order to mark folder

if not os.path.isfile('maid'):
    with open('maid', 'w+') as f:
        FirstTimeSetup()

print('Maid root directory:', os.fsdecode(maidDir))
print('Maid config directory:', os.fsdecode(maidConfDir))
print('Maid temp directory:', os.fsdecode(maidTempDir))
