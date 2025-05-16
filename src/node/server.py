from flask import Flask, request, jsonify
from blockchain.transaction import Transaction
from blockchain.blockchain import Blockchain
import json

app = Flask(__name__)
blockchain = Blockchain()

@app.route('/transaction/new', methods=['POST'])
def new_transaction():
    """Create a new transaction"""
    try:
        data = request.get_json()
        
        # Validate required fields
        required_fields = ['sender', 'recipient', 'amount']
        if not all(field in data for field in required_fields):
            return jsonify({'error': 'Missing required fields'}), 400
        
        # Create transaction
        transaction = Transaction(
            sender=data['sender'],
            recipient=data['recipient'],
            amount=float(data['amount'])
        )
        
        # Add to pending transactions
        blockchain.add_transaction(
            transaction.sender,
            transaction.recipient,
            transaction.amount
        )
        
        return jsonify({
            'message': 'Transaction added successfully',
            'transaction': transaction.to_dict()
        }), 201
        
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/mine', methods=['POST'])
def mine_block():
    """Mine a new block"""
    try:
        # Get miner address from request
        data = request.get_json()
        if not data or 'miner' not in data:
            return jsonify({'error': 'Miner address required'}), 400
            
        # Mine the block
        blockchain.mine_pending_transactions(data['miner'])
        
        return jsonify({
            'message': 'New block mined successfully',
            'block': blockchain.chain[-1].to_dict()
        }), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/chain', methods=['GET'])
def get_chain():
    """Get the full blockchain"""
    return jsonify({
        'chain': [block.to_dict() for block in blockchain.chain],
        'length': len(blockchain.chain)
    }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000) 