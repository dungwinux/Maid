def addPath(arg):
    os.environ["PATH"] += ';' + arg;
def removePath(arg):
    # WARNING : Use this carefully. In case PATH cannot be found, the system will be SERIOUSLY
    # broken, as finding fundamental utilities fails.
    os.environ["PATH"].replace(arg, '')
