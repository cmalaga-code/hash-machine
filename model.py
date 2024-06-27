"""
pydantic models to validate data.
"""

from pydantic import BaseModel
from enum import Enum


class Algorithm(str, Enum):
    md5 = "MD5"
    sha1 = "SHA1"
    sha256 = "SHA256"
    sha384 = "SHA384"
    sha512 = "SHA512"


class Data(BaseModel):
    item: str
    algorithm: Algorithm
    salt: bool | None = False
    salt_value: str | None = None
