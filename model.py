"""
pydantic models to validate data.
"""

from pydantic import BaseModel

class Data(BaseModel):
    item: str
    algorithm: str | None = "SHA2"
    salt: bool | None = False
    salt_value: str | None = None
