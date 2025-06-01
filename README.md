#  Blockchain Finance Logger

A simple Python project to record and verify your personal financial transactions using a custom-built blockchain. Each transaction (income or expense) is securely stored in a block, forming an immutable chain that you can verify at any time.

This is a beginner-friendly project built entirely in Python and designed to be extendable — perfect for learning blockchain concepts while creating something useful.

---

##  Features

- Record income and expense transactions
- Automatically creates blocks for each transaction
- View the full blockchain in a readable format
- Verify the integrity of the entire chain
- Simple CLI (command-line) interface
- Modular structure for easy maintenance and upgrades

---

##  Project Structure

finance_blockchain/
-  main.py # Entry point and CLI loop
- blockchain.py # Blockchain and Block classes
- transaction.py # User input and transaction validation
- utils.py # Helper functions (like pretty-printing blocks)


##  How It Works

Each transaction is added as a new block to the blockchain.
Every block contains:
- A timestamp
- A transaction (type, amount, category, note)
- A cryptographic hash
- The hash of the previous block

The blockchain is stored in memory and can be verified for tampering.

## Ideas for Future Improvements

- Save blockchain data to a JSON file or database
- Add digital signatures with public/private keys
- Build a simple web or mobile interface
- Use sockets to sync blockchains across peers
- Convert into a minimal cryptocurrency simulation

