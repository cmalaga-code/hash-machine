"""
utility code for main.py
"""

import hashlib
import time

def sha256(input: str, salt: bool = False):
    """
    hash input with the respective algorithm and return the value. if salt is true then return add. 
    """
    if salt:
        if input.salt_value:
            salted_data = input.item + input.salt_value
        else:
            salted_data = input.item + str(int(time.time()))
        return hashlib.sha256(salted_data.encode("utf-8")).hexdigest()
    return hashlib.sha256(input.item.encode("utf-8")).hexdigest()
