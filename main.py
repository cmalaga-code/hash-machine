from fastapi import FastAPI
from model import Data
from utility import sha256

app = FastAPI()


@app.get("/")
@app.post("/")
async def index():
    return {"message": "Please use /hash"}


@app.post("/hash")
async def hash(data: Data):
    item = data.item
    algorithm = data.algorithm
    salt = data.salt
    salt_value = data.salt_value
    if algorithm == "SHA2":
        if salt:
            return {"result": sha256(item, True, salt_value)}
        return {"result": sha256(item, False, salt_value)}
