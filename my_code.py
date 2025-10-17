# TO CHECK IF THE CODE IS RUNNING IN A VIRTUAL ENVIRONMENT OR NOT

import sys

def is_virtual():
    return sys.prefix != sys.base_prefix

if is_virtual():
    print('Virtual environment')
else:
    print('Not virtual environment')

"""
Explanation:
sys.prefix: Points to the prefix of the Python installation currently in use.
sys.base_prefix: Points to the prefix of the base Python installation.
is_virtual(): Returns True if the script is running inside a virtual environment (i.e., sys.prefix is different from sys.base_prefix).
"""

