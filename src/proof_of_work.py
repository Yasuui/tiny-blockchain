import hashlib
import json

class ProofOfWork:
    def __init__(self, difficulty=4):
        self.difficulty = difficulty

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