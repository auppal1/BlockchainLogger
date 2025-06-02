import hashlib
import json
import time


class Block:
    def __init__(self, index, transactions, timestamp, previous_hash):
        self.index = index
        self.transactions = transactions
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        try:
            block_string = json.dumps({
                "index": self.index,
                "transactions": self.transactions,
                "timestamp": self.timestamp,
                "previous_hash": self.previous_hash
            }, sort_keys=True).encode()
            return hashlib.sha256(block_string).hexdigest()
        except Exception as e:
            print(f"Error hashing block: {e}")
            return None

    def __str__(self):
        return json.dumps(self.__dict__, indent=4)


class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, [], time.time(), "0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, transactions):
        latest_block = self.get_latest_block()
        new_block = Block(
            index=latest_block.index + 1,
            transactions=transactions,
            timestamp=time.time(),
            previous_hash=latest_block.hash
        )
        self.chain.append(new_block)

    def is_chain_valid(self):
        try:
            for i in range(1, len(self.chain)):
                current = self.chain[i]
                previous = self.chain[i - 1]
                if current.hash != current.calculate_hash():
                    print(f"Invalid hash at block {i}")
                    return False
                if current.previous_hash != previous.hash:
                    print(f"Invalid link between blocks {i - 1} and {i}")
                    return False
            return True
        except Exception as e:
            print(f"Chain verification error: {e}")
            return False

    def print_chain(self):
        from utils import print_block
        for block in self.chain:
            print_block(block)
