from fastapi import FastAPI
from src.models.transaction import Transaction
from src.services.transaction_service import (
    get_all_transactions,
    get_transaction_by_id,
    create_transaction,
    delete_transaction_by_id,
    load_transactions,
    get_balance,
    update_transaction_by_id,
    get_transactions_by_type
)

app = FastAPI()

load_transactions()

@app.get("/")
def home():
    return {"message": "Finance API is running"}


@app.get("/transactions")
def get_transactions():
    return get_all_transactions()


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

@app.get("/transactions/type/{transaction_type}")
def filter_transactions(transaction_type: str):
    return get_transactions_by_type(transaction_type)       

