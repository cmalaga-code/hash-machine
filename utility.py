"""
utility code for main.py
"""

import hashlib
import time


def sha256(item: str, salt: bool, salt_value: str | None):
    """
    hash item with the respective algorithm and return the value. if salt is true then return add.
    """
    if salt:
        if salt_value:
            salted_data = item + salt_value
        else:
            salted_data = item + str(int(time.time()))
        return hashlib.sha256(salted_data.encode("utf-8")).hexdigest()
    return hashlib.sha256(item.encode("utf-8")).hexdigest()
