import json
import os
import fire
from urllib.parse import urlparse


class pkg:
    def __init__(self, name, ver, bin_url, sha1=""):
        self.name = str(name)
        self.ver = str(ver)
        self.bin_url = urlparse(bin_url)
        self.sha1 = str(sha1)

    def gen(self, override=False):
        print('Generating package')
        if not os.path.isdir(self.name):
            os.mkdir(self.name)
        with (open(f'{self.name}\\task', 'w')) as pkg:
            json.dump({'name': self.name,
                       'ver': self.ver,
                       'bin_url': self.bin_url,
                       'sha1': self.sha1},
                      pkg)

    @classmethod
    def read(folder):
        print('Reading package')
        if not os.path.isdir(str(folder)):
            with (open(f'{str(folder)}\\task', 'r')) as pkg:
                db = json.load(pkg)
            if str(db['name']) == str(folder):
                return db

# Example
# t = pkg('2048', '5.2.4',
#         'https://github.com/taptapking/2048/releases/download/5.2.4/2048.5.2.4.x86.exe')
# t.gen()
