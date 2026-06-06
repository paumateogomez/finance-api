from fastapi import HTTPException
from src.database import insert_transaction, get_transaction_by_id_from_db, delete_transaction_by_id_from_db, update_transaction_by_id_from_db, get_total_amount_by_type, get_filtered_transactions_from_db, get_statistics_by_category_from_db, get_transaction_count_from_db

def get_transaction_by_id(transaction_id: int):
    row = get_transaction_by_id_from_db(transaction_id)
    if row is not None:
        return {
            "id": row[0],
            "type": row[1],
            "amount": row[2],
            "category": row[3]
        }
    raise HTTPException(
        status_code=404,     detail="Transaction not found"
    )


def create_transaction(transaction_data: dict):
    transaction_id = insert_transaction(transaction_data)

    transaction_data["id"] = transaction_id

    return transaction_data


def delete_transaction_by_id(transaction_id: int):

    row = get_transaction_by_id_from_db(transaction_id)

    if row is not None:
        delete_transaction_by_id_from_db(transaction_id)

        return {
            "message": "Transaction deleted successfully"
        }

    raise HTTPException(
        status_code=404,
        detail="Transaction not found"
    )
    
def get_balance():
    income = get_total_amount_by_type("income")
    expenses = get_total_amount_by_type("expense")

    balance = income - expenses

    return {
        "balance": balance,
        "income": income,
        "expenses": expenses
    }

def update_transaction_by_id(transaction_id: int, updated_data: dict):
    row = get_transaction_by_id_from_db(transaction_id)
    if row is not None:
        updated_transaction = {
            "id": row[0],
            "type": updated_data.get("type", row[1]),
            "amount": updated_data.get("amount", row[2]),
            "category": updated_data.get("category", row[3])
        }

        update_transaction_by_id_from_db(transaction_id, updated_transaction)

        return updated_transaction
    raise HTTPException(
        status_code=404,   detail="Transaction not found" 
    )   

def get_filtered_transactions( transaction_type=None, category=None, sort = None):
    raw_transactions = get_filtered_transactions_from_db(transaction_type, category, sort)

    transactions = [
        {
            "id": row[0],
            "type": row[1],
            "amount": row[2],
            "category": row[3]
        }
        for row in raw_transactions
    ]   
    return transactions

def get_statistics_by_category():
    rows = get_statistics_by_category_from_db()

    statistics = [
        {
            "category": row[0],
            "total": row[1]
        }
        for row in rows
    ]

    return statistics

def get_transaction_count():
    count = get_transaction_count_from_db()

    return {
        "total_transactions": count
    }

def get_statistics():
    balance_data = get_balance()
    category_statistics = get_statistics_by_category()
    transaction_count = get_transaction_count()

    return {
        "total_transactions": transaction_count["total_transactions"],
        "income": balance_data["income"],
        "expenses": balance_data["expenses"],
        "balance": balance_data["balance"],
        "categories": category_statistics
    }