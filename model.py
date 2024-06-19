"""
pydantic models to validate data.
"""

from pydantic import BaseModel
from enum import Enum


class Algorithm(str, Enum):
    sha256 = "SHA2"


class Data(BaseModel):
    item: str
    algorithm: Algorithm
    salt: bool | None = False
    salt_value: str | None = None
