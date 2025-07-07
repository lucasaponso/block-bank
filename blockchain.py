import hashlib
import time
from typing import List

class Block:
    def __init__(self, index: int, previous_hash: str, timestamp: float, data: str, hash: str):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash

    def to_dict(self):
        return self.__dict__

def calculate_hash(index, previous_hash, timestamp, data):
    value = f"{index}{previous_hash}{timestamp}{data}"
    return hashlib.sha256(value.encode()).hexdigest()

def create_genesis_block():
    return Block(0, "0", time.time(), "Genesis Block", calculate_hash(0, "0", time.time(), "Genesis Block"))

class Blockchain:
    def __init__(self):
        self.chain: List[Block] = [create_genesis_block()]

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, data: str):
        latest_block = self.get_latest_block()
        new_index = latest_block.index + 1
        new_timestamp = time.time()
        new_hash = calculate_hash(new_index, latest_block.hash, new_timestamp, data)
        new_block = Block(new_index, latest_block.hash, new_timestamp, data, new_hash)
        self.chain.append(new_block)
        return new_block

    def get_chain(self):
        return [block.to_dict() for block in self.chain]
