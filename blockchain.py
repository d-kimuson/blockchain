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

    def validate_block(self, block: Block) -> bool:
        if block.hash != block.generate_hash():
            print(f"[Fail to validate] hash changed.")
            print(f"Hash {block.generate_hash()} changed from {block.hash}.")
            return False
        if self.valid_proof(block):
            print(f"[Fail to validate] Proof Of Work does not hold up.")
            return False
        return True

    def validate_chain(self) -> bool:
        if not self.validate_block(self.chain[0]):
            return False

        for i in range(1, len(self.chain)):
            current = self.chain[i]
            if not self.validate_block(current):
                return False
            if current.previous_hash != self.chain[i-1].hash:
                print(f"[Fail to validate] Hash does not connect.")
                print("{} is not equals to {}".format(
                    current.previous_hash,
                    self.chain[i-1].hash
                    ))
                return False
        return True

    def print_blocks(self) -> None:
        for i in range(len(self.chain)):
            current_block = self.chain[i]
            print(f"# Block {i} {current_block}")
            current_block.print_contents()

    @property
    def ledger(self):
        transactions = []
        for block in self.chain:
            transactions.extend(block.transactions)
        return transactions

    @property
    def wallets(self):
        return Wallets(self.ledger)


class Wallets(dict):
    def __init__(self, ledger: list) -> None:
        super().__init__()

        for column in ledger:
            sender = column['sender']
            receiver = column['receiver']
            if sender not in self.keys():
                self[sender] = 0
            if receiver not in self.keys():
                self[receiver] = 0
            self[sender] += int(column['amount'])
            self[receiver] -= int(column['amount'])