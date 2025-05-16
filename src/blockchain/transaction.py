from dataclasses import dataclass
from typing import Dict
import json
import hashlib
from datetime import datetime

@dataclass
class Transaction:
    sender: str
    recipient: str
    amount: float
    timestamp: float = None

    def __post_init__(self):
        if self.timestamp is None:
            self.timestamp = datetime.now().timestamp()

    def to_dict(self) -> Dict:
        """Convert transaction to dictionary format"""
        return {
            'sender': self.sender,
            'recipient': self.recipient,
            'amount': self.amount,
            'timestamp': self.timestamp
        }

    def to_json(self) -> str:
        """Convert transaction to JSON string"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_dict(cls, data: Dict) -> 'Transaction':
        """Create a Transaction instance from a dictionary"""
        return cls(
            sender=data['sender'],
            recipient=data['recipient'],
            amount=data['amount'],
            timestamp=data.get('timestamp')
        )

    @classmethod
    def from_json(cls, json_str: str) -> 'Transaction':
        """Create a Transaction instance from a JSON string"""
        data = json.loads(json_str)
        return cls.from_dict(data)

    def hash(self) -> str:
        """Generate a hash of the transaction"""
        transaction_string = self.to_json()
        return hashlib.sha256(transaction_string.encode()).hexdigest() 