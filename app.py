import streamlit as st
from blockchain import Blockchain
from transaction import get_transaction
import time
from database import init_db, save_transaction
from database import get_all_transactions


page = st.sidebar.radio("Navigation", ["🏠 Add Transaction", "📜 Transaction History", "🔗 Blockchain Viewer"])

# Initialize blockchain
init_db()
if "blockchain" not in st.session_state:
    st.session_state.blockchain = Blockchain()
bc = st.session_state.blockchain

st.title("🧾 Blockchain Finance Logger")
st.write("Track your income and expenses securely using a custom blockchain.")

# --- Add Transaction ---
if page == "🏠 Add Transaction":
    st.title("➕ Add a New Transaction")

    with st.form("transaction_form"):
        t_type = st.selectbox("Transaction Type", ["income", "expense"])
        category = st.text_input("Category (e.g., salary, groceries)")
        amount = st.number_input("Amount", min_value=0.01, format="%.2f")
        note = st.text_input("Note (optional)")
        submitted = st.form_submit_button("Add Transaction")

        if submitted:
            if category.strip() == "":
                st.error("Category cannot be empty.")
            else:
                transaction = {
                    "type": t_type,
                    "category": category,
                    "amount": amount,
                    "note": note,
                    "timestamp": time.ctime()
                }
                bc.add_block([transaction])
                save_transaction(transaction)
                st.success("Transaction added and saved.")


# -- Transaction History Tab
elif page == "📜 Transaction History":
    st.title("📜 Transaction History")
    transactions = get_all_transactions()
    if not transactions:
        st.info("No transactions found.")
    else:
        for tx in reversed(transactions):
            with st.expander(f"{tx['timestamp']} | {tx['category']} | {tx['amount']:.2f}"):
                st.json(tx)

# --- View Blockchain ---
elif page == "🔗 Blockchain Viewer":
    st.title("🔗 Blockchain Viewer")
    from datetime import datetime

    st.subheader("🔗 Blockchain Viewer")

    for block in reversed(bc.chain):
        if block.transactions:
            tx = block.transactions[0]
            date_str = datetime.fromtimestamp(block.timestamp).strftime("%b %d")
            category = tx.get("category", "No Category")
            title = f"Block#{block.index} | {date_str} | {category}"
        else:
            title = f"Block#{block.index} | Genesis Block"

        with st.expander(title):
            st.json(block.__dict__)

    # --- Chain Validation ---
    st.subheader("🔐 Validate Blockchain")

    if bc.is_chain_valid():
        st.success("✅ The blockchain is valid.")
    else:
        st.error("❌ Blockchain integrity check failed!")
