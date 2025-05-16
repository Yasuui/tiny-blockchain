# Tiny Blockchain

A simple, educational implementation of a blockchain in Python. This project demonstrates the core concepts of blockchain technology including blocks, transactions, proof of work, and mining.

## Features

- Block creation and chaining
- Transaction management
- Proof of Work consensus mechanism
- Mining rewards
- Balance tracking
- Basic test suite

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/tiny-blockchain.git
cd tiny-blockchain
```

2. Create and activate a virtual environment (recommended):
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows, use: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the example blockchain:
```bash
python src/main.py
```

Run tests:
```bash
pytest tests/
```

## Project Structure

```
tiny-blockchain/
├── src/
│   ├── blockchain.py    # Core blockchain implementation
│   ├── proof_of_work.py # Proof of work mechanism
│   └── main.py         # Example usage
├── tests/
│   └── test_blockchain.py
└── docs/
    └── architecture.md
```

## How It Works

1. **Blocks**: Each block contains:
   - Index
   - Timestamp
   - List of transactions
   - Previous block's hash
   - Current block's hash

2. **Transactions**: Simple transfers between addresses with amounts

3. **Mining**: 
   - Miners solve proof of work puzzles
   - Successful mining adds new blocks
   - Miners receive rewards

4. **Proof of Work**:
   - Adjustable difficulty
   - SHA-256 hashing
   - Verification mechanism

## Contributing

Show support by ⭐ project 

## Credits

This project is based on the following resources:
- [Learn Blockchains by Building One](https://medium.com/crypto-currently/lets-build-the-tiniest-blockchain-e70965a248b) by Gerald Nash
- [Original GitHub Repository](https://github.com/codecrafters-io/build-your-own-x.git)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.