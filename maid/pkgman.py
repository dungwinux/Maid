# Libraries
import json
import os
from urllib.parse import urlparse


class pkg:
    def __init__(self, name, bin_url, sha1, is_local=False):
        self.name = str(name)
        self.bin_url = urlparse(bin_url)
        self.sha1 = str(sha1)
        self.is_local = bool(is_local)

    def toJSON(self):
        """Convert package to json"""
        return json.dumps(self, default=lambda o: o.__dict__,
                          indent=4)

    @staticmethod
    def is_pkg(p_json):
        """Check if given object is package"""
        if type(p_json) is dict:
            if not all(key in p_json for key in ('name', 'bin_url', 'sha1')):
                return False
        return True

    @classmethod
    def fromJSON(cls, p_json):
        """Create new package from json"""
        if pkg.is_pkg(p_json):
            dmp = json.loads(p_json)
        return cls(dmp['name'], dmp['bin_url'], dmp['sha1'])
        # TODO: is_local


class pkg_list:
    def __init__(self, filename):
        self.data = []
        data = json.load(filename)
        if type(data) is list:
            for p in data:
                if pkg.is_pkg(p):
                    self.data.append(pkg.fromJSON(p))

    def add(self, package: pkg):
        """Append package"""
        self.data.append(pkg)

    def rem(self, package: pkg):
        """Remove package"""
        self.data.remove(pkg)

    # TODO: Low-level API

# Example
# print(pkg('2049', 'https://www.example.com/', 'sha1').toJSON())
