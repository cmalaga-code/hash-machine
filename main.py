from fastapi import FastAPI
from model import Data
from utility import hasher
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=["POST"],
    allow_headers=["Content-Type"],
)

@app.get("/")
@app.post("/")
async def index():
    """
    Please use /hash {POST}.
    """
    return {"message": "Please use /hash"}


@app.post("/hash")
async def hash(data: Data):
    """
    Hashes string item sent by client and returns json containing result according to available algorithm chosen by client.
    """
    item = data.item
    algorithm = data.algorithm
    salt = data.salt
    salt_value = data.salt_value

    if salt:
        return {"result": hasher(algorithm, item, True, salt_value)}
    return {"result": hasher(algorithm, item, False, salt_value)}
