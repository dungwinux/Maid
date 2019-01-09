from setuptools import setup, find_packages

with open("README.md", "r") as readline:
    long_description = readline.read()

setup(
    name="maid",
    version="0.1.12",
    author="Nguyễn Tuấn Dũng",
    author_email="ntddebugger@gmail.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dungwinux/Maid",
    packages=['maid'],
    install_requires=['wget', 'patool', 'pywin32', 'winshell'],
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
