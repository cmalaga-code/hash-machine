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
    if data.algorithm == "SHA2":
        if data.salt:
            return {"result": sha256(data, True)}
        return {"result": sha256(data)}



