from setuptools import setup

version = {}

with open("maid/version.py") as fp:
    exec(fp.read(), version)

with open("README.md", "r") as readline:
    long_description = readline.read()

setup(
    name="maid",
    version=version['__version__'],
    description="A package manager written in Python 3.7",
    author="Nguyễn Tuấn Dũng",
    author_email="ntddebugger@gmail.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dungwinux/Maid",
    packages=['maid'],
    install_requires=[
        'wget>=3.2',
        'patool>=1.12',
        'pywin32>=224',
        'winshell>=0.6'
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Operating System :: Microsoft :: Windows :: Windows 7",
        "Operating System :: Microsoft :: Windows :: Windows 8",
        "Operating System :: Microsoft :: Windows :: Windows 8.1",
        "Operating System :: Microsoft :: Windows :: Windows 10",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: Microsoft :: Windows"
    ],
)
