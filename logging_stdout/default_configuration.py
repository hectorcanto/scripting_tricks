"""
Modify the default configuration adding a configuration.py file.
The code will read the default configuration and overwrite some values with configuration.py. If it does not
exists, it will go on silently. This will prevent errors from missing parameters

In general, do not add it to the repository.
Later on you may have several configuration depending on the environment - development, test, production ...
"""

import logging

GENERAL_LOG_LEVEL = logging.INFO

try:
    from configuration import *
except ImportError:
    pass
