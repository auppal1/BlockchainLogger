from blockchain import Blockchain
from transaction import get_transaction


def main():
    bc = Blockchain()

    while True:
        print("\n--- Blockchain Finance Logger ---")
        print("1. Add transaction")
        print("2. View blockchain")
        print("3. Verify chain")
        print("4. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            tx = get_transaction()
            if tx:
                bc.add_block([tx])
                print("Transaction added in a new block!")
        elif choice == "2":
            bc.print_chain()
        elif choice == "3":
            valid = bc.is_chain_valid()
            print("Blockchain is valid!" if valid else "Blockchain has issues!")
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid option. Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
