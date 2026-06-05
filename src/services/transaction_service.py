from fastapi import HTTPException
import json

transactions = []

DATA_FILE = "data/transactions.json"


def load_transactions():
    global transactions

    try:
        with open(DATA_FILE, "r") as file:
            transactions = json.load(file)
    except:
        transactions = []


def save_transactions():
    with open(DATA_FILE, "w") as file:
        json.dump(transactions, file, indent=4)


def get_all_transactions():
    return transactions


def get_transaction_by_id(transaction_id: int):
    for transaction in transactions:
        if transaction["id"] == transaction_id:
            return transaction

    raise HTTPException(
        status_code=404,
        detail="Transaction not found"
    )


def create_transaction(transaction_data: dict):

    if not transactions:
        transaction_data["id"] = 1
    else:
        max_id = max(transaction["id"] for transaction in transactions)
        transaction_data["id"] = max_id + 1

    transactions.append(transaction_data)
    save_transactions()

    return transaction_data


def delete_transaction_by_id(transaction_id: int):

    for transaction in transactions:

        if transaction["id"] == transaction_id:
            transactions.remove(transaction)
            save_transactions()

            return {
                "message": "Transaction deleted successfully"
            }

    raise HTTPException(
        status_code=404,
        detail="Transaction not found"
    )