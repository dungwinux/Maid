import os
import shutil
from config import maidDir, maidPackDir


def bin_search(pkg_name):
    """Search binaries and executables then hard-link to bin/ folder"""

    print("""Searching for binaries & executables ...""")

    src = os.path.join(os.fsdecode(maidPackDir), pkg_name) + '\\'
    maidBinDir = os.path.join(os.fsdecode(maidDir), 'bin')

    for path, dirs, files in os.walk(src):
        for file in files:
            if os.path.splitext(file)[-1] in ['.exe', '.reg', '.bat']:
                binary = os.path.join(path, file)
                print("Found:", binary)
                os.link(binary, os.path.join(maidBinDir, file))
                print("\t->", os.path.join(maidBinDir, file))


def link_rem(pkg_name):
    """Search hard-link of binaries and executables then delete"""

    print("""Searching for binaries & executables ...""")

    src = os.path.join(os.fsdecode(maidPackDir), pkg_name) + '\\'
    maidBinDir = os.path.join(os.fsdecode(maidDir), 'bin')

    for path, dirs, files in os.walk(src):
        for file in files:
            if os.path.splitext(file)[-1] in ['.exe', '.reg', '.bat']:
                link = os.path.join(maidBinDir, file)
                print(link)
                if os.path.isfile(link):
                    print("Unlink:", link)
                    os.remove(link)