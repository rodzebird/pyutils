"""
The whichpython module encapsulate the sys.version_info call
to write more elegant conditional code when switching operations
depending on the Python version used by the developer.

E.g.: Instead of doing `if sys.version_info < (3, 0): #python2 code`
      you can do `if PY2: #python2 code`
"""

import sys


def version():
    """Return the version of the currently used Python binary."""
    return sys.version_info


"""Constant set to True if the Python version is Python 2.X"""
PY2 = version() < (3, 0)

"""Constant set to True if the Python version is Python 2.3"""
PY3 = not PY2

"""Constant set to `bytes` if the current Python version is Python3, else `unicode`"""
ENCODER = bytes if PY3 else unicode
