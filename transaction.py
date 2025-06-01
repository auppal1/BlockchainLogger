import time


def get_transaction():
    try:
        t_type = input("Enter transaction type (income/expense): ").strip().lower()
        if t_type not in ["income", "expense"]:
            print("Invalid transaction type.")
            return None

        category = input("Enter category (e.g., food, salary): ").strip()
        if not category:
            print("Category cannot be empty.")
            return None

        amount_input = input("Enter amount: ").strip()
        try:
            amount = float(amount_input)
            if amount <= 0:
                print("Amount must be greater than 0.")
                return None
        except ValueError:
            print("Invalid amount format.")
            return None

        note = input("Optional note: ").strip()

        return {
            "type": t_type,
            "category": category,
            "amount": amount,
            "note": note,
            "timestamp": time.ctime()
        }
    except Exception as e:
        print(f"Error collecting transaction: {e}")
        return None
