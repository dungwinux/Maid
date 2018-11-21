# Libraries
import zipfile
import os
import wget
import shutil
import re
from urllib.parse import urlparse

# Modules
from run import bin_search, link_rem
from error import MaidError
from config import maidDir, maidPackDir, maidTempDir
# import pkgman


def add(path):
    """Add package to local storage"""
    # This function will try to:
    # read given package,
    # get its name and
    # try to extract it to maidPackDir

    # Get filename from package's path
    filepath = os.fsdecode(os.fsencode(path))
    print(f'[Verbose] filepath: {filepath}')
    if not os.path.isfile(filepath):
        raise MaidError("Invalid package")
    filename = os.path.basename(filepath)
    # Here we got:
    # - filepath: path to pacakges
    # - filename: name of package (by concat filepath)

    print(f"Reading {filename}")
    # Remove extension from filename to get downloaded package's name
    pkgname = str(os.path.splitext(filename)[0])
    pkgname = pkgname.split(' ')[0]

    # Split version number from filename
    regex = re.compile(r"[0-9]+(\.[0-9]+){1,3}")
    ver_lookup = regex.search(pkgname)

    # Check if version looking-up is successful
    if ver_lookup is None:
        # If version number is not found, set name to pkgname, ver to '0.0.0'
        ver = '0.0.0'
        name = pkgname
    else:
        # If version number is found, set name to pkgname that was sliced
        # version number
        v_begin, v_end = ver_lookup.span()
        # Slice package version
        ver = pkgname[v_begin:v_end]
        print(f'[Verbose] Package version detected: {ver}')
        name = pkgname[:v_begin - 1]
        name = name + pkgname[v_end:]
    # TODO: Compare package's version with installed package

    # TODO: Compare SHA1 with installed package

    # NOTE: After above step, we got some important variables from guessing
    # - pkgname: Name of downloaded package, this is where we guess from
    # - name: Name of program inside package
    # - ver: Version of program inside package
    # - sha1: (TODO) Sha1 of downloaded package

    # Get extract path by concatenating maidPackDir and name
    extractPath = os.fsdecode(maidPackDir) + name
    # Verbose
    print(f'Extracting to {extractPath} ...')

    # Extract package to maidPkgDir
    if not os.path.isdir(extractPath):
        os.makedirs(extractPath)
    # Checking for zip file
    if zipfile.is_zipfile(filepath):
        # If it is, Maid will extract its content to pkg folder in maidPackDir
        zipfile.ZipFile(filepath).extractall(path=extractPath)
    else:
        # Else, Maid will copy content to new folder in maidPackDir
        print('Not zip archive file. Treating downloaded file as raw.')
        shutil.copy2(filename, extractPath)

    bin_search(name)


def get(url):
    """Retrieve package with specified url"""
    # This function will try to:
    # download package from url,
    # put it in maidTempFolder and
    # call add API on it

    # Get formal url from given url string by parsing it
    # (Who know, someone might try to break the Maid)
    link = urlparse(url)
    url = link.geturl()
    print(f'Starting download from {url}')

    os.chdir(maidTempDir)

    # Download package using wget
    filename = wget.download(url)
    print(f'\nDownloaded {filename}')

    # Call add API on downloaded package
    add(os.fsdecode(maidTempDir) + filename)

    # UNUSED: Change current working directory to main directory
    os.chdir(maidDir)


def rem(package):
    """Remove package"""
    # This function will try to:
    # Search package name in maidPackDir and
    # delete it if matching result be found

    # Get current working directory, in order to revert back later
    cwd = os.getcwd()
    os.chdir(maidPackDir)
    print('Removing:', package)

    # TODO: Search for package

    # Get designated package path by concatenating given package name
    # WARNING: This should be held serious as it could be used to delete
    # system files
    path = package + '\\'
    if os.path.isdir(path):
        link_rem(package)
        shutil.rmtree(path)
    else:
        print('Invalid Package')

    # Return
    os.chdir(cwd)


def query(pkg_search):
    """Query list of package"""
    # This function will try to:
    # Search package name in maidPackDir and
    # return list of matching package(s)

    # Generate a list of package
    # NOTE: Will use a new way to handle instead of querying folders' name
    pkg_list = list(os.listdir(maidPackDir))
    # Formatting package name from binary -> string
    pkg_list = map(os.fsdecode, pkg_list)
    # Generate regex for searching
    regex = re.compile(str(pkg_search))
    # Search for matching package(s)
    pkg_list = list(filter(regex.search, pkg_list))

    print('Matching package(s):', len(pkg_list))
    # Print searching result
    for pkg in pkg_list:
        print(pkg)


def clear():
    """Clear temp folder"""
    # This function will try to:
    # Remove maidTempDir with all its contents and create new one

    # Expecting behavior: Empty the maidTempDir without issue

    print('Clearing temporary package download...')
    if os.path.exists(maidTempDir):
        shutil.rmtree(maidTempDir)

    if not os.path.exists(maidTempDir):
        os.makedirs(maidTempDir)


def import_pkg(path):
    """Import packages list"""
    # This function will try to:
    # read package list from path and if it is:
    #         url -> call get API
    # local files -> call add API

    # TODO: import package list from path and call proper function to handle


def export_pkg(path):
    """Export packages list"""
    # This function will try to:
    # read all available packages and
    # return a package list in path

    # TODO: Query a package list and export to path


# TODO: Integrate pkgman.py function to handle package or,
#       poorly handle package by hand
