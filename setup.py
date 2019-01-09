import setuptools

with open("README.md", "r") as readline:
    long_description = readline.read()

setuptools.setup(
    name="Maid",
    version="0.0.0",
    author="dungwinux, minhducsun2002",
    author_email="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dungwinux/Maid",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: Microsoft :: Windows"
    ],
)
