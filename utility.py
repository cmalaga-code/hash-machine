"""
utility code for main.py
"""

import hashlib
import time


def hasher(algorithm: str, item: str, salt: bool, salt_value: str | None):
    """
    hash item with the respective algorithm and return the value. if salt is true then return add.
    """
    if salt:
        if salt_value:
            salted_data = item + salt_value
        else:
            salted_data = item + str(int(time.time()))

        match algorithm:
            case "MD5":
                return hashlib.md5(salted_data.encode("utf-8")).hexdigest()
            case "SHA1":
                return hashlib.sha1(salted_data.encode("utf-8")).hexdigest()
            case "SHA256":
                return hashlib.sha256(salted_data.encode("utf-8")).hexdigest()
            case "SHA384":
                return hashlib.sha384(salted_data.encode("utf-8")).hexdigest()
            case "SHA512":
                return hashlib.sha512(salted_data.encode("utf-8")).hexdigest()

    match algorithm:
        case "MD5":
            return hashlib.md5(item.encode("utf-8")).hexdigest()
        case "SHA1":
            return hashlib.sha1(item.encode("utf-8")).hexdigest()
        case "SHA256":
            return hashlib.sha256(item.encode("utf-8")).hexdigest()
        case "SHA384":
            return hashlib.sha384(item.encode("utf-8")).hexdigest()
        case "SHA512":
            return hashlib.sha512(item.encode("utf-8")).hexdigest()
