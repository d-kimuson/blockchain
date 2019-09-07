import json
from time import time
from hashlib import sha256

class Block:
    def __init__(self, transactions: list, previous_hash: str) -> None:
        self.time = time()
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce = 0
        self.set_hash()

    def set_hash(self) -> None:
        self.hash = self.generate_hash()

    def generate_hash(self) -> str:
        block_hash = sha256(self.block_header.encode())
        return block_hash.hexdigest()

    @property
    def block_header(self) -> str:
        return json.dumps({
            'time_stamp': self.time,
            'transactions': self.transactions,
            'previous_hash': self.previous_hash,
            'nonce': self.nonce,
        }, sort_keys=True)

    @property
    def proof(self) -> str:
        return self.generate_hash()

    def print_contents(self) -> None:
        print("time:", datetime.fromtimestamp(self.time))
        print("nonce:", self.nonce)
        print("transactions:", self.transactions)
        print("current hash:", self.generate_hash())
        print("previous hash:", self.previous_hash)