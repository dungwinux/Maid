# Maid
Guide for Maid

Running `maid.py -h` will provide a list of options available :
```
[Verbose] Reading config file
usage: maid [-h] [--version] [--force] <command> ...

Maid - Package Manager

optional arguments:
  -h, --help  show this help message and exit
  --version   show program's version number and exit
  --force

command:
  <command>   sub-command help
    add       Add package
    rem       Remove package
    que       Query package
    cle       Clear temporary package downloads

Example: TBA
```

### Basic instructions
###### All commands used here is ran with Administrator privilege.
#### Adding Packages
```
maid add https://github.com/minhducsun2002/just-another-newtab-archive/master.zip
```
```
[Verbose] Reading config file
Starting download from https://github.com/minhducsun2002/just-another-newtab/archive/master.zip

Downloaded just-another-newtab-master.zip
Extracting to C:\Program Files (No Installation)\maid\maid\pkg\just-another-newtab...
```
