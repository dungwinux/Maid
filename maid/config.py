#libraries
import os

appPath = os.getenv('APPDATA')
maidDir = os.fsencode(os.getcwd() + '\\maid\\')
maidConfDir = os.fsencode(appPath + '\\maid\\')
maidTempDir = os.fsencode(os.getenv('TEMP') + '\\maid\\')