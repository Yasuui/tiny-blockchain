import pytest
from src.blockchain.transaction import Transaction
import json
from datetime import datetime

def test_create_transaction():
    transaction = Transaction("Alice", "Bob", 10.0)
    assert transaction.sender == "Alice"
    assert transaction.recipient == "Bob"
    assert transaction.amount == 10.0
    assert transaction.timestamp is not None

def test_transaction_to_dict():
    transaction = Transaction("Alice", "Bob", 10.0)
    transaction_dict = transaction.to_dict()
    assert transaction_dict['sender'] == "Alice"
    assert transaction_dict['recipient'] == "Bob"
    assert transaction_dict['amount'] == 10.0
    assert 'timestamp' in transaction_dict

def test_transaction_to_json():
    transaction = Transaction("Alice", "Bob", 10.0)
    json_str = transaction.to_json()
    data = json.loads(json_str)
    assert data['sender'] == "Alice"
    assert data['recipient'] == "Bob"
    assert data['amount'] == 10.0
    assert 'timestamp' in data

def test_transaction_from_dict():
    data = {
        'sender': 'Alice',
        'recipient': 'Bob',
        'amount': 10.0,
        'timestamp': datetime.now().timestamp()
    }
    transaction = Transaction.from_dict(data)
    assert transaction.sender == "Alice"
    assert transaction.recipient == "Bob"
    assert transaction.amount == 10.0
    assert transaction.timestamp == data['timestamp']

def test_transaction_from_json():
    json_str = '{"sender": "Alice", "recipient": "Bob", "amount": 10.0, "timestamp": 1234567890.0}'
    transaction = Transaction.from_json(json_str)
    assert transaction.sender == "Alice"
    assert transaction.recipient == "Bob"
    assert transaction.amount == 10.0
    assert transaction.timestamp == 1234567890.0

def test_transaction_hash():
    transaction = Transaction("Alice", "Bob", 10.0)
    hash1 = transaction.hash()
    # Same transaction should have same hash
    assert transaction.hash() == hash1
    # Different transaction should have different hash
    transaction2 = Transaction("Alice", "Bob", 20.0)
    assert transaction2.hash() != hash1 