from blockchain import Blockchain
from proof_of_work import ProofOfWork

def main():
    # Create a new blockchain
    blockchain = Blockchain()
    pow = ProofOfWork()

    # Create some example transactions
    blockchain.add_transaction("Alice", "Bob", 10)
    blockchain.add_transaction("Bob", "Charlie", 5)

    # Mine a block
    print("Mining block...")
    blockchain.mine_pending_transactions("miner1")

    # Print the blockchain
    print("\nBlockchain:")
    for block in blockchain.chain:
        print(f"\nBlock #{block.index}")
        print(f"Timestamp: {block.timestamp}")
        print(f"Transactions: {block.transactions}")
        print(f"Previous Hash: {block.previous_hash}")
        print(f"Hash: {block.hash}")

    # Print balances
    print("\nBalances:")
    print(f"Alice: {blockchain.get_balance('Alice')}")
    print(f"Bob: {blockchain.get_balance('Bob')}")
    print(f"Charlie: {blockchain.get_balance('Charlie')}")
    print(f"Miner1: {blockchain.get_balance('miner1')}")

if __name__ == "__main__":
    main() 