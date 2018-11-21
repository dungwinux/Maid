import os
import shutil
from config import maidDir, maidPackDir, maidBinDir


def bin_walk(pkg_name, fun):
    src = os.path.join(os.fsdecode(maidPackDir), pkg_name) + '\\'
    for path, dirs, files in os.walk(src):
        if path[len(src) + 1:].count(os.sep) < 2:
            for file in files:
                if os.path.splitext(file)[-1] in ['.exe', '.reg', '.bat']:
                    fun(path, file)


def bin_search(pkg_name):
    """Search binaries and executables then hard-link to bin/ folder"""

    print("""Searching for binaries & executables ...""")
    bin_walk(pkg_name, linkBin)


def link_rem(pkg_name):
    """Search hard-link of binaries and executables then delete"""

    print("""Searching for binaries & executables ...""")
    bin_walk(pkg_name, unlinkBin)


def linkBin(path, file):
    binary = os.path.join(path, file)
    link = os.path.join(os.fsdecode(maidBinDir), file)
    print("Found:", binary)
    try:
        os.link(binary, link)
        print("\t->", link)
    except FileExistsError:
        print("Link is valid, can't re-link")


def unlinkBin(path, file):
    link = os.path.join(os.fsdecode(maidBinDir), file)
    print(link)
    if os.path.isfile(link):
        print("Unlink:", link)
        os.remove(link)
