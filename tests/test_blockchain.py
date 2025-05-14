import pytest
from src.blockchain import Blockchain, Block
from src.proof_of_work import ProofOfWork

def test_create_blockchain():
    blockchain = Blockchain()
    assert len(blockchain.chain) == 1
    assert blockchain.chain[0].index == 0
    assert blockchain.chain[0].previous_hash == "0"

def test_add_transaction():
    blockchain = Blockchain()
    blockchain.add_transaction("Alice", "Bob", 10)
    assert len(blockchain.pending_transactions) == 1
    assert blockchain.pending_transactions[0]["from"] == "Alice"
    assert blockchain.pending_transactions[0]["to"] == "Bob"
    assert blockchain.pending_transactions[0]["amount"] == 10

def test_mine_block():
    blockchain = Blockchain()
    blockchain.add_transaction("Alice", "Bob", 10)
    blockchain.mine_pending_transactions("miner1")
    assert len(blockchain.chain) == 2
    assert len(blockchain.pending_transactions) == 1
    assert blockchain.pending_transactions[0]["to"] == "miner1"

def test_get_balance():
    blockchain = Blockchain()
    blockchain.add_transaction("Alice", "Bob", 10)
    blockchain.mine_pending_transactions("miner1")
    assert blockchain.get_balance("Alice") == -10
    assert blockchain.get_balance("Bob") == 10
    assert blockchain.get_balance("miner1") == 10 