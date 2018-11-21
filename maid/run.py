import os
from config import maidPackDir, maidBinDir


def bin_walk(pkg_name, fun):
    """Recursively browse for executables from pkg_name directory"""

    print("""Searching for binaries & executables ...""")
    # Maximum traversal depth
    MAX_DEPTH = 2
    # Generate location to search
    src = os.path.join(os.fsdecode(maidPackDir), pkg_name) + '\\'
    # Use os.walk to browse recursively
    for path, dirs, files in os.walk(src):
        # Check for traversal depth
        if path[len(src) + 1:].count(os.sep) < MAX_DEPTH:
            # Browsing through file in directory
            for file in files:
                # Filter executables
                if os.path.splitext(file)[-1] in ['.exe', '.reg', '.bat']:
                    print("Found:", os.path.join(path, file))
                    fun(path, file)


def bin_search(pkg_name):
    """Search binaries and executables then hard-link to bin/ folder"""

    bin_walk(pkg_name, linkBin)


def link_rem(pkg_name):
    """Search hard-link of binaries and executables then delete"""

    bin_walk(pkg_name, unlinkBin)


def linkBin(path, file):
    # This is file that need to be linked
    binary = os.path.join(path, file)
    # This is where file will be linked to
    link = os.path.join(os.fsdecode(maidBinDir), file)
    try:
        # Try to link file in case no link with same name
        os.link(binary, link)
        print("\t->", link)
    except FileExistsError:
        # If link is available, inform user
        print("Link is valid, cannot re-link")


def unlinkBin(path, file):
    # This is where file will be unlinked
    link = os.path.join(os.fsdecode(maidBinDir), file)
    # Check if link is available in bin/ folder
    if os.path.isfile(link):
        # If yes, delete it
        print("Unlink:", link)
        os.remove(link)
    else:
        # Else, inform "Missing link"
        print("Missing link:", link)
