import pytest
from blockchain.blockchain import Blockchain
from blockchain.transaction import Transaction

def test_integration():
    # Create a blockchain
    blockchain = Blockchain()
    
    # Add a transaction
    blockchain.add_transaction("Alice", "Bob", 10.0)
    
    # Mine a block
    blockchain.mine_pending_transactions("miner1")
    
    # Verify the block was mined
    assert len(blockchain.chain) == 2
    assert blockchain.chain[1].transactions[0]["from"] == "Alice"
    assert blockchain.chain[1].transactions[0]["to"] == "Bob"
    assert blockchain.chain[1].transactions[0]["amount"] == 10.0
    
    # Verify the mining reward
    assert blockchain.chain[1].transactions[1]["from"] == "network"
    assert blockchain.chain[1].transactions[1]["to"] == "miner1"
    assert blockchain.chain[1].transactions[1]["amount"] == blockchain.mining_reward
    
    # Verify balances
    assert blockchain.get_balance("Alice") == -10.0
    assert blockchain.get_balance("Bob") == 10.0
    assert blockchain.get_balance("miner1") == blockchain.mining_reward 