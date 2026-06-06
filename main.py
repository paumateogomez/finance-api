from fastapi import FastAPI
from src.models.transaction import Transaction
from src.database import initialize_database
from src.services.transaction_service import (
    get_transaction_by_id,
    create_transaction,
    delete_transaction_by_id,
    get_balance,
    update_transaction_by_id,
    get_filtered_transactions,
    get_statistics_by_category,
    get_transaction_count,
    get_statistics
)

app = FastAPI()

initialize_database()

@app.get("/")
def home():
    return {"message": "Finance API is running"}


@app.get("/transactions")
def get_transactions(
    type: str = None,
    category: str = None,
    sort: str = None
):
    return get_filtered_transactions(
        type,
        category,
        sort
    )


@app.get("/transactions/{transaction_id}")
def get_transaction(transaction_id: int):
    return get_transaction_by_id(transaction_id)


@app.post("/transactions")
def add_transaction(transaction: Transaction):
    transaction_data = transaction.model_dump()
    new_transaction = create_transaction(transaction_data)

    return {
        "message": "Transaction added successfully",
        "transaction": new_transaction
    }


@app.delete("/transactions/{transaction_id}")
def delete_transaction(transaction_id: int):
    return delete_transaction_by_id(transaction_id)

@app.get("/balance")
def get_balance_endpoint():
    return get_balance()

@app.put("/transactions/{transaction_id}")
def update_transaction(
    transaction_id: int,
    transaction: Transaction
):
    transaction_data = transaction.model_dump()

    return update_transaction_by_id(
        transaction_id,
        transaction_data
    )

@app.get("/statistics/categories")
def statistics_by_category():
    return get_statistics_by_category()

@app.get("/statistics/count")
def transaction_count():
    return get_transaction_count()

@app.get("/statistics")
def get_statistics_endpoint():
    return get_statistics()
