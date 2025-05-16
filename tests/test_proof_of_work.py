import pytest
from blockchain.blockchain import Block
from blockchain.proof_of_work import ProofOfWork

def test_proof_of_work():
    # Create a block with some dummy data
    block = Block(1, [], 1234567890, "previous_hash")
    # Create a ProofOfWork instance with difficulty 4
    pow = ProofOfWork(block, difficulty=4)
    # Mine the block
    block_hash = pow.mine()
    # Verify that the hash starts with 4 zeros
    assert block_hash.startswith('0' * 4) 