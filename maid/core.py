# Libraries
import zipfile
import os
import wget
import shutil
from urllib.parse import urlunparse, urlparse
# Dev libraries
import fire

# Modules
import pkgman
from config import maidDir, maidTempDir, maidPackDir

# def add(package):
# TODO: Add function


def get(url):
    """Retrieve package with specified url"""

    link = urlparse(url)
    url = link.geturl()
    print(f'Starting download from {url}')
    os.chdir(maidTempDir)
    filename = wget.download(url)
    print(f'\nDownloaded {filename}')
    # pkgname = input(f'Package name (default is {filename}): ')
    # if not pkgname:
    #     pkgname = filename
    pkgname = os.path.splitext(filename)[0]
    extractPath = os.fsdecode(maidPackDir) + pkgname
    print(f'Extracting to {extractPath}...')
    if not os.path.isdir(extractPath):
        os.makedirs(extractPath)
    if zipfile.is_zipfile(filename):
        zipfile.ZipFile(filename).extractall(path=extractPath)
    else:
        print('Not zip archive file. Casting downloaded file as extracted package.')
        shutil.copy2(filename, extractPath)

    os.chdir(maidDir)

# Example
# get('https://github.com/taptapking/2049/releases/download/5.3/2048.5.3.x86.exe')


# def query(package, pkg_list):
# TODO: Query function

# def rem(package)
# TODO: Remove function

# Dev interface
if __name__ == '__main__':
    fire.Fire()