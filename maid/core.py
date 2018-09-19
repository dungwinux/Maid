import wget
import requests
import os
import zipfile
import pkgman

# def add(package):
# TODO: Add function

def get(package):
    """Retrieve package with specified url"""

    filename = wget.download(package.bin_url)
    print(f'Downloaded {filename}')


# def query(package, pkg_list):
# TODO: Query function

# def rem(package)
# TODO: Remove function  