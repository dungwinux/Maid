# Libraries
import wget
import requests
import zipfile
import os

# Modules
import pkgman
import config

# def add(package):
# TODO: Add function


def get(package):
    """Retrieve package with specified url"""

    os.chdir(config.maidTempDir)
    filename = wget.download(package.bin_url)
    print(f'Downloaded {filename}')


# def query(package, pkg_list):
# TODO: Query function

# def rem(package)
# TODO: Remove function
