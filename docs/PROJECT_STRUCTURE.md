# Project Structure and Branching Strategy

## Branching Strategy

We follow a simplified Git Flow branching strategy:

- `main`: Production-ready code
- `develop`: Integration branch for features
- `feature/*`: Feature branches for new functionality
  - `feature/test-implementation`: Test suite implementation
  - `feature/blockchain-core`: Core blockchain functionality

## Project Structure

```
tiny-blockchain/
├── src/
│   ├── blockchain/
│   │   ├── __init__.py
│   │   ├── blockchain.py      # Core blockchain implementation
│   │   └── proof_of_work.py   # Proof of work mechanism
│   ├── utils/
│   │   ├── __init__.py
│   │   └── helpers.py         # Utility functions
│   └── main.py               # Application entry point
├── tests/
│   ├── __init__.py
│   ├── test_blockchain.py    # Blockchain tests
│   └── test_proof_of_work.py # Proof of work tests
├── docs/
│   ├── PROJECT_STRUCTURE.md  # This file
│   └── API.md               # API documentation
├── requirements.txt
└── README.md
```

## Development Workflow

1. Create feature branches from `develop`
2. Implement and test features
3. Create pull requests to merge into `develop`
4. After testing, merge `develop` into `main` for releases

## Code Organization

- Core blockchain logic is separated from utility functions
- Tests mirror the structure of the source code
- Documentation is kept up-to-date with code changes
- Each module has its own test suite 