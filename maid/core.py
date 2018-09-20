# Libraries
import requests
import zipfile
import os
from urllib.parse import urlunparse

# Modules
import pkgman
import config

# def add(package):
# TODO: Add function


def download(url, name=""):
    filename = name if name else url.split('/')[-1]
    with requests.get(url, stream=True) as r:
        with open(filename, 'wb') as f:
            for chk in r.iter_content(chunk_size=1024):
                if chk:
                    f.write(chk)
    return filename


def get(package):
    """Retrieve package with specified url"""

    cwd = os.getcwd()
    os.chdir(config.maidTempDir)
    filename = download(urlunparse(package.bin_url))
    print(f'Downloaded {filename}')
    os.chdir(cwd)

# def query(package, pkg_list):
# TODO: Query function

# def rem(package)
# TODO: Remove function


t = pkgman.pkg('2048', '5.2.4',
               'https://github.com/taptapking/2049/releases/download/5.3/2048.5.3.x86.exe')

get(t)
# download('https://github.com/taptapking/2049/releases/download/5.3/2048.5.3.x86.exe')
