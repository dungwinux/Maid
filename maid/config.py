# libraries
import os
import configparser
from error import MaidError

confHeader = """# File generated by Maid - DO NOT EDIT
"""

# Default directory
appPath = os.getenv('APPDATA')
maidDir = os.fsencode(os.getcwd() + '\\maid\\')
maidConfDir = os.fsencode(appPath + '\\maid\\')
maidTempDir = os.fsencode(os.getenv('TEMP') + '\\maid\\')
maidPackDir = os.fsencode(os.fsdecode(maidDir) + 'pkg\\')
maidConfFile = os.fsencode(appPath + '\\maid\\maid.conf')


def ReadConf():
    """Read configuration in designated location"""

    global maidDir, maidConfDir, maidTempDir, maidPackDir

    print('[Verbose] Reading config file')
    # Try importing configuration, else maid will make one
    if os.path.isfile(maidConfFile):
        conf = configparser.ConfigParser()
        conf.read(maidConfFile)

        maidDir = os.fsencode(conf['options']['rootDir'])
        maidConfDir = os.fsencode(conf['options']['confDir'])
        maidTempDir = os.fsencode(conf['options']['tempDir'])
        maidPackDir = os.fsencode(conf['options']['packDir'])
    else:
        MakeConf()

    prepareDir()


def prepareDir():
    if not os.path.isdir(maidDir):
        os.makedirs(maidDir)
    if not os.path.isdir(maidConfDir):
        os.makedirs(maidConfDir)
    if not os.path.isdir(maidPackDir):
        os.makedirs(maidPackDir)
    if not os.path.isdir(maidTempDir):
        os.makedirs(maidTempDir)


def MakeConf():
    """Create new configuration in designated location"""

    global maidDir, maidConfDir, maidTempDir, maidPackDir

    # Maid config.maidDir
    print('[Verbose] Creating config file')
    if not os.path.isdir(maidConfDir):
        try:
            os.mkdir(maidConfDir)
        except os.error:
            raise MaidError(
                """Error : could not find Maid configuration directory.
An attempt to create it has failed. Check if you have permission to create
    """ + maidConfDir)

    try:
        os.chdir(maidConfDir)
    except os.error:
        raise MaidError(
            """Error : could not access Maid configuration directory.""")

    print(f"Config directory: {os.getcwd()}")

    # Config file
    config = configparser.ConfigParser()
    config['options'] = {
        'rootDir': os.fsdecode(maidDir),
        'confDir': os.fsdecode(maidConfDir),
        'tempDir': os.fsdecode(maidTempDir),
        'packDir': os.fsdecode(maidPackDir),
        'logFile': ''}
    try:
        with open(os.fsencode('maid.conf'), 'w') as configfile:
            configfile.write(confHeader)
            config.write(configfile)
    except OSError:
        raise MaidError("Error : could not access maid.conf")


def FirstTimeSetup():

    print("Seems like this is the first time Maid is run. \
    Preparing initial setup.")

    prepareDir()
    MakeConf()
    ReadConf()


ReadConf()

# Check for prepared directory
# If not, Maid will try to create `maid` file in order to mark folder

# if not os.path.isfile('maid'):
#     with open('maid', 'w+') as f:
#         FirstTimeSetup()

# os.chdir(maidConfDir)
