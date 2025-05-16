import hashlib
import json

class ProofOfWork:
    def __init__(self, block, difficulty=4):
        self.block = block
        self.difficulty = difficulty
        self.nonce = 0

    def mine(self):
        target = '0' * self.difficulty
        while True:
            self.block.nonce = self.nonce
            block_hash = self.calculate_hash()
            if block_hash.startswith(target):
                return block_hash
            self.nonce += 1

    def calculate_hash(self):
        block_string = json.dumps({
            "index": self.block.index,
            "timestamp": self.block.timestamp,
            "transactions": self.block.transactions,
            "previous_hash": self.block.previous_hash,
            "nonce": self.block.nonce
        }, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def get_proof_of_work(self, block):
        block_string = json.dumps({
            "index": block.index,
            "timestamp": block.timestamp,
            "transactions": block.transactions,
            "previous_hash": block.previous_hash
        }, sort_keys=True).encode()
        
        proof = 0
        while True:
            guess = block_string + str(proof).encode()
            guess_hash = hashlib.sha256(guess).hexdigest()
            
            if guess_hash[:self.difficulty] == "0" * self.difficulty:
                return proof, guess_hash
            proof += 1

    def verify_proof(self, block, proof):
        block_string = json.dumps({
            "index": block.index,
            "timestamp": block.timestamp,
            "transactions": block.transactions,
            "previous_hash": block.previous_hash
        }, sort_keys=True).encode()
        
        guess = block_string + str(proof).encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        
        return guess_hash[:self.difficulty] == "0" * self.difficulty 