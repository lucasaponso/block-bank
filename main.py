from fastapi import FastAPI
from blockchain import Blockchain
from pydantic import BaseModel

app = FastAPI()

blockchain = Blockchain()

class BlockData(BaseModel):
    data: str

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI Blockchain!"}

@app.get("/chain")
def get_chain():
    return {"length": len(blockchain.chain), "chain": blockchain.get_chain()}

@app.post("/mine")
def mine_block(block_data: BlockData):
    new_block = blockchain.add_block(block_data.data)
    return {"message": "Block added", "block": new_block.to_dict()}
