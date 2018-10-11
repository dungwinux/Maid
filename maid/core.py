# Libraries
import zipfile
import os
import wget
import shutil
import re
from urllib.parse import urlunparse, urlparse

# Dev libraries
import fire

# Modules
import pkgman
from config import maidConfDir, maidDir, maidPackDir, maidTempDir, appPath


# def add(package):
# TODO: Add function

def get(url):
    """Retrieve package with specified url"""

    link = urlparse(url)
    url = link.geturl()
    print(f'Starting download from {url}')

    # Change directory to Temp folder
    if not os.path.isdir(maidTempDir):
        os.mkdir(maidTempDir)
    os.chdir(maidTempDir)

    # Download package using wget
    filename = wget.download(url)
    print(f'\nDownloaded {filename}')
    # pkgname = input(f'Package name (default is {filename}): ')
    # if not pkgname:
    #     pkgname = filename

    # Remove extension from filename
    pkgname = os.path.splitext(filename)[0]
    # Try removing version number from filename
    name_break = pkgname.split('-')
    # TODO: Compare with downloaded package

    if len(name_break) > 1:
        name_break.pop()
    pkgname = '-'.join(name_break)

    # Extract package to maidPkgDir
    extractPath = os.fsdecode(maidPackDir) + pkgname
    print(f'Extracting to {extractPath}...')
    if not os.path.isdir(extractPath):
        os.makedirs(extractPath)
    if zipfile.is_zipfile(filename):
        zipfile.ZipFile(filename).extractall(path=extractPath)
    else:
        print('Not zip archive file. Treating downloaded file as extracted package.')
        shutil.copy2(filename, extractPath)

    os.chdir(maidDir)

# Example
# get('https://github.com/taptapking/2049/releases/download/5.3/2048.5.3.x86.exe')


# def query(package, pkg_list):
# TODO: Query function

def rem(package):
    """Remove package"""

    cwd = os.getcwd()
    os.chdir(maidPackDir)
    print('Removing:', package)
    path = package + '\\'
    if os.path.isdir(path):
        shutil.rmtree(path)
    else:
        print('Invalid Package')


def query(pkg_search):
    """Query list of package"""

    pkg_list = list(os.listdir(maidPackDir))
    pkg_list = map(os.fsdecode, pkg_list)
    # filter() pkg_list with regex
    regex = re.compile(str(pkg_search))
    pkg_list = list(filter(regex.search, pkg_list))

    print('Number of matching package(s):', len(pkg_list))
    for pkg in pkg_list:
        print(pkg)


def clear():
    """Clear temp folder"""

    print('Clearing temporary package download...')
    if os.path.exists(maidTempDir):
        shutil.rmtree(maidTempDir)

    if not os.path.exists(maidTempDir):
        os.makedirs(maidTempDir)


# Dev interface
if __name__ == '__main__':
    fire.Fire()
