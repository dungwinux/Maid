# Maid

A package manager, written in Python 3.7, for Windows.

Status: **Alpha**

[![Build status](https://ci.appveyor.com/api/projects/status/isl3y0bxqk8kr2ls?svg=true)](https://ci.appveyor.com/project/dungwinux/maid)

## Installation

### Via `pip`

```sh
pip install maid
```

> Currently, Maid is depends on `pip` to update. In the future, Maid will be able to do self-update.

### Download pre-built binary

-   See: [Releases](https://github.com/dungwinux/Maid/releases)

> Note: Pre-built binary requires Microsoft Visual C++ 2017 Redistributable, which Windows 10 comes with by default. For older version of Windows, please search online for download links.

### Run source code

-   `git clone` this repository.
-   `python -r requirements.txt` to install all dependencies
-   Invoke `python -m maid -h`.
