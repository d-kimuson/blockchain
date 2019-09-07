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

    def add_transaction(self, amount: int, sender: str, receiver: str) -> None:
        self.unconfirmed_transactions.append({
            'sender': sender,
            'receiver': receiver,
            'amount': amount
        })

    def add_transactions(self, transactions: list) -> None:
        for transaction in transactions:
            diff = set(transaction.keys()) - set(['sender',
                                                  'receiver',
                                                  'amount'])
            assert diff == set(), f'Index error, {diff}.'
        for transaction in transactions:
            self.add_transaction(
                sender=transaction['sender'],
                receiver=transaction['receiver'],
                amount=transaction['amount']
            )

    def pop_transactions(self) -> list:
        _ = self.unconfirmed_transactions
        self.unconfirmed_transactions = []
        return _

    def create_block(self) -> None:
        previous = self.chain[-1]
        new_block = Block(self.pop_transactions(), previous.hash)
        self.proof_of_work(new_block)
        self.chain.append(new_block)

    def proof_of_work(self, block: Block) -> None:
        block.nonce = 0
        while self.valid_proof(block):
            block.nonce += 1
        block.set_hash()

    def valid_proof(self, block: Block) -> bool:
        return block.proof[:self.difficulty] != "0" * self.difficulty