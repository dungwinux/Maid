# Libraries
import zipfile
import os
import wget
from urllib.parse import urlunparse

# Modules
import pkgman
from config import maidDir, maidTempDir

# def add(package):
# TODO: Add function


def get(url):
    """Retrieve package with specified url"""

    os.chdir(maidTempDir)
    filename = wget.download(url)
    print(f'\nDownloaded {filename}')

    os.chdir(maidDir)



# def query(package, pkg_list):
# TODO: Query function

# def rem(package)
# TODO: Remove function

# get('https://github.com/taptapking/2049/releases/download/5.3/2048.5.3.x86.exe')
