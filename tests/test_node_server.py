import pytest
from node.server import app
import json

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_new_transaction(client):
    """Test creating a new transaction"""
    # Test valid transaction
    response = client.post('/transaction/new',
                          json={
                              'sender': 'Alice',
                              'recipient': 'Bob',
                              'amount': 10.0
                          })
    assert response.status_code == 201
    data = json.loads(response.data)
    assert data['message'] == 'Transaction added successfully'
    assert data['transaction']['sender'] == 'Alice'
    assert data['transaction']['recipient'] == 'Bob'
    assert data['transaction']['amount'] == 10.0

    # Test missing fields
    response = client.post('/transaction/new',
                          json={
                              'sender': 'Alice',
                              'recipient': 'Bob'
                          })
    assert response.status_code == 400

def test_mine_block(client):
    """Test mining a new block"""
    # Add a transaction first
    client.post('/transaction/new',
                json={
                    'sender': 'Alice',
                    'recipient': 'Bob',
                    'amount': 10.0
                })

    # Test mining
    response = client.post('/mine',
                          json={'miner': 'miner1'})
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['message'] == 'New block mined successfully'
    assert 'block' in data

    # Test missing miner
    response = client.post('/mine',
                          json={})
    assert response.status_code == 400

def test_get_chain(client):
    """Test getting the blockchain"""
    response = client.get('/chain')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'chain' in data
    assert 'length' in data
    assert isinstance(data['chain'], list)
    assert isinstance(data['length'], int) 