from block import Block


class Blockchain:
    def __init__(self, difficulty=4):
        self.chain = []
        self.unconfirmed_transactions = []
        self.difficulty = difficulty
        self.genesis_block()

    def genesis_block(self) -> None:
        genesis_block = Block([], "0")
        self.proof_of_work(genesis_block)
        self.chain.append(genesis_block)

    def proof_of_work(self, block: Block) -> None:
        block.nonce = 0
        while self.valid_proof(block):
            block.nonce += 1
        block.set_hash()

    def valid_proof(self, block: Block) -> bool:
        return block.proof[:self.difficulty] != "0" * self.difficulty