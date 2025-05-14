# Tiny Blockchain Architecture

This document describes the architecture of our tiny blockchain implementation.

## Core Components

### Block
- Represents a single block in the blockchain
- Contains:
  - Index
  - Timestamp
  - List of transactions
  - Previous block's hash
  - Current block's hash

### Blockchain
- Maintains the chain of blocks
- Handles:
  - Creating the genesis block
  - Adding new transactions
  - Mining new blocks
  - Calculating account balances

### Proof of Work
- Implements the mining mechanism
- Features:
  - Adjustable difficulty
  - Proof verification
  - Hash calculation

## Transaction Flow

1. Transactions are added to the pending transactions pool
2. Miners can mine new blocks containing pending transactions
3. Successful mining adds the block to the chain
4. Miners receive a reward for successful mining

## Security Features

- Cryptographic hashing (SHA-256)
- Proof of work consensus mechanism
- Immutable block structure
- Transaction verification

## Future Improvements

- Network layer for P2P communication
- Wallet implementation
- Smart contracts support
- Consensus mechanism improvements 