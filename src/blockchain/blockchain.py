from datetime import datetime
import hashlib
import json

class Block:
    def __init__(self, index, transactions, timestamp, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = json.dumps({
            "index": self.index,
            "timestamp": self.timestamp,
            "transactions": self.transactions,
            "previous_hash": self.previous_hash
        }, sort_keys=True).encode()
        
        return hashlib.sha256(block_string).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.difficulty = 4
        self.pending_transactions = []
        self.mining_reward = 10

    def create_genesis_block(self):
        return Block(0, [], datetime.now().timestamp(), "0")

    def get_latest_block(self):
        return self.chain[-1]

    def mine_pending_transactions(self, miner_address):
        block = Block(
            len(self.chain),
            self.pending_transactions + [{"from": "network", "to": miner_address, "amount": self.mining_reward}],
            datetime.now().timestamp(),
            self.get_latest_block().hash
        )
        
        self.chain.append(block)
        self.pending_transactions = []

    def add_transaction(self, sender, recipient, amount):
        self.pending_transactions.append({
            "from": sender,
            "to": recipient,
            "amount": amount
        })

    def get_balance(self, address):
        balance = 0
        
        for block in self.chain:
            for transaction in block.transactions:
                if transaction["from"] == address:
                    balance -= transaction["amount"]
                if transaction["to"] == address:
                    balance += transaction["amount"]
                    
        return balance 