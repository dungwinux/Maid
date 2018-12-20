"""
patoolib uses importlib and pyinstaller doesn't find it
"""


hiddenimports = [
    'patoolib.programs',
    'patoolib.programs.*'
]
