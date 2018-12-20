# Libraries
import os
import shutil
import re
from wget import download
from urllib.parse import urlparse
from urllib.error import URLError
from patoolib import extract_archive, list_formats, programs
from patoolib.util import PatoolError
from tempfile import mkdtemp

# Modules
from run import bin_search, link_rem
from error import MaidError
from config import maidPackDir, maidTempDir
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
    regex = re.compile(r"(v|)[0-9]+(\.[0-9]+){1,3}")
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
    extractPath = os.path.join(os.fsdecode(maidPackDir), name)
    # Verbose
    print(f'Extracting to {extractPath} ...')

    # Extract package to maidPkgDir
    # if not os.path.isdir(extractPath):
    #     os.makedirs(extractPath)
    # Checking for zip file

    try:
        extract_archive(filepath, outdir=extractPath, interactive=False)
        print("Extraction completed.")
    except PatoolError as msg:
        print(f"Extractor error: {msg}")
        print('Treating downloaded file as raw.')
        shutil.copy2(filepath, extractPath)

    bin_search(name)


def get(package):
    """Retrieve package with specified url or local path"""
    # This function will try to:
    # download package from url,
    # put it in maidTempFolder and
    # call add API on it

    try:
        # Get formal url from given url string by parsing it
        # (Who know, someone might try to break the Maid)
        tmpdir = mkdtemp(dir=maidTempDir)
        link = urlparse(package)
        if (link.netloc == ""):
            raise ValueError("Invalid URL")
        url = link.geturl()

        # Download package using wget

        print(f"[Verbose] Starting download from {url}")

        downloadDir = tmpdir
        cwd = os.getcwd()
        os.chdir(downloadDir)
        filename = download(url)
        os.chdir(cwd)

        print()
        print(f'[Verbose] Downloaded {filename}')

        # If things work well, it will set pkgPath to downloaded file
        pkgPath = os.path.join(os.fsdecode(downloadDir), filename)

    except ValueError as msg:
        # If ValueError is caught, Maid think given string is local
        print(f"[Verbose] {msg}")
        print("Invalid URL. Treating given string as local package")
        pkgPath = package

    except URLError as msg:
        # If URLError is caught, it's either network fault or your fault
        print(f"[Verbose] {msg}")
        raise MaidError("Cannot get from given URL")

    add(pkgPath)

    # Call add API on downloaded package


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
