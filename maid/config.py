# libraries
import os
import configparser

# Modules
from error import MaidError

confHeader = """# File generated by Maid - DO NOT EDIT
"""


# Static directory
appPath = os.getenv('APPDATA')
maidConfFile = os.fsencode(appPath + '\\maid\\maid.conf')


# Default directory
maidDir = os.fsencode(os.path.join(os.getcwd(), '\\maid\\'))
maidConfDir = os.fsencode(os.path.join(appPath, '\\maid\\'))
maidTempDir = os.fsencode(os.path.join(os.getenv('TEMP'), '\\maid\\'))
maidPackDir = os.fsencode(os.path.join(os.fsdecode(maidDir), 'pkg\\'))
maidBinDir = os.fsencode(os.path.join(os.fsdecode(maidDir), 'bin\\'))


def ReadConf():
    """Read configuration in designated location"""

    global maidDir, maidConfDir, maidTempDir, maidPackDir, maidBinDir

    print('[Verbose] Try reading config file')
    # Try importing configuration, else maid will make one
    if os.path.isfile(maidConfFile):
        conf = configparser.ConfigParser()
        conf.read(maidConfFile)

        try:
            # TODO: Sanitize string path
            maidDir = os.fsencode(conf['options']['rootDir'])
            maidConfDir = os.fsencode(conf['options']['confDir'])
            maidTempDir = os.fsencode(conf['options']['tempDir'])
            maidPackDir = os.fsencode(conf['options']['packDir'])
            maidBinDir = os.fsencode(conf['options']['binDir'])
        except KeyError:
            # Run MakeConf if there's at least one broken path
            MakeConf()
    else:
        # Run FirstTimeSetup if maidConfFile is not available
        FirstTimeSetup()

    prepareDir()


def prepareDir():
    """Prepare directories before serving"""

    os.makedirs(maidDir, exist_ok=True)
    os.makedirs(maidConfDir, exist_ok=True)
    os.makedirs(maidPackDir, exist_ok=True)
    os.makedirs(maidTempDir, exist_ok=True)
    os.makedirs(maidBinDir, exist_ok=True)

    # TODO: Make MAID_BIN_DIR persistent in PATH
    # Add MAID_DIR variable to PATH so that PATH is clean
    # if '%MAID_BIN_DIR%' not in (os.getenv('PATH')):
    #     print("MAID_BIN_DIR not found in PATH. Adding to PATH ...")
    #     os.putenv('PATH', os.getenv('PATH').join('%MAID_BIN_DIR%'))

    # Set MAID_BIN_DIR to maidBinDir
    # print('Setting MAID_BIN_DIR value ...')
    # os.putenv('MAID_BIN_DIR', os.fsdecode(maidBinDir))


def MakeConf():
    """Create new configuration in designated location"""

    global maidDir, maidConfDir, maidTempDir, maidPackDir, maidBinDir

    # Maid config.maidDir
    print('[Verbose] Creating config file')
    if not os.path.isdir(maidConfDir):
        try:
            os.mkdir(maidConfDir)
        except os.error:
            raise MaidError(
                """Error : could not find Maid configuration directory.
An attempt to create it has failed. Check if you have permission to create"""
                + maidConfDir)

    try:
        os.chdir(maidConfDir)
    except os.error:
        raise MaidError(
            """Error : could not access Maid configuration directory.""")

    print("Config directory:", os.getcwd())

    # Config setting
    config = configparser.ConfigParser()
    config['options'] = {
        'rootDir': os.fsdecode(maidDir),
        'confDir': os.fsdecode(maidConfDir),
        'tempDir': os.fsdecode(maidTempDir),
        'packDir': os.fsdecode(maidPackDir),
        'binDir': os.fsdecode(maidBinDir),
        'logFile': ''}
    # TODO: write logfile
    try:
        # Write Config to maidConfFile
        with open(os.fsencode(maidConfFile), 'w') as configfile:
            configfile.write(confHeader)
            config.write(configfile)
    except OSError:
        raise MaidError("Error : could not access maid.conf")


def FirstTimeSetup():
    """Set of commands to run when Maid is run for the first time"""

    print("Seems like this is the first time Maid is run. \
    Preparing initial setup.")

    prepareDir()
    MakeConf()
    ReadConf()


# Check for maid.conf file
# If there's none, run FirstTimeSetup

ReadConf()
