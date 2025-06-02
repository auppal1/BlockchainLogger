import json
import os

TRANSACTION_DIR = "data/transactions"


def init_db():
    os.makedirs(TRANSACTION_DIR, exist_ok=True)


def get_next_filename(category):
    existing_files = os.listdir(TRANSACTION_DIR)
    next_index = len(existing_files) + 1
    clean_category = "".join(c for c in category if c.isalnum() or c in (' ', '_')).strip().replace(" ", "_")
    filename = f"{next_index:04d}_{clean_category.lower()}.json"
    return os.path.join(TRANSACTION_DIR, filename)


def save_transaction(tx):
    try:
        filename = get_next_filename(tx["category"])
        with open(filename, "w") as f:
            json.dump(tx, f, indent=4)
    except Exception as e:
        print(f"Error saving transaction to JSON file: {e}")


def get_all_transactions():
    transactions = []
    try:
        for fname in sorted(os.listdir(TRANSACTION_DIR)):
            path = os.path.join(TRANSACTION_DIR, fname)
            with open(path, "r") as f:
                transactions.append(json.load(f))
    except Exception as e:
        print(f"Error loading transactions: {e}")
    return transactions
