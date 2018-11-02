# Libraries
import json
import os
from urllib.parse import urlparse

# NOTE: These code are originally created for handling packages with core.py,
# The following code are expected to be used in future, so don't change it


class pkg:
    def __init__(self, name, up_url, sha1):
        # - name: Package name
        # - up_url: Upstream url, None if local package is added
        # - sha1: Package's SHA1
        self.name = str(name)
        # NOTE: Need a better way to handle url
        self.up_url = urlparse(up_url).geturl()
        self.sha1 = str(sha1)

    def toJSON(self):
        """Convert package to json"""
        return json.dumps(self, default=lambda o: o.__dict__,
                          indent=4)

    @staticmethod
    def is_pkg(p_json):
        """Check if given json (not file), is package"""

        if type(p_json) is dict:
            if not all(key in p_json for key in ('name', 'up_url', 'sha1')):
                return False
        return True

    @classmethod
    def fromJSON(cls, filename):
        """Read package from json file"""
        with open(filename) as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                return None
        if pkg.is_pkg(data):
            return cls(data['name'], data['up_url'], data['sha1'])


class pkg_list:
    """List of package. This class is for import/export function"""

    def __init__(self):
        self.data = list()

    def add(self, package: pkg):
        """Append package"""
        self.data.append(pkg)

    def rem(self, package: pkg):
        """Remove package"""
        self.data.remove(pkg)
