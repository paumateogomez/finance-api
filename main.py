from fastapi import FastAPI
from fastapi import HTTPException
from src.models.transaction import Transaction
app = FastAPI()

transactions = []


@app.get("/")
def home():
    return {"message": "Finance API is running"}


@app.get("/transactions")
def get_transactions():
    return transactions

@app.get("/transactions/{transaction_id}")
def get_transaction(transaction_id: int):
    for transaction in transactions:
        if transaction["id"] == transaction_id:
            return transaction
    raise HTTPException(status_code=404, detail="Transaction not found")

@app.post("/transactions")
def add_transaction(transaction: Transaction):
    new_transaction = transaction.model_dump()
    if not transactions:
        new_transaction["id"] = 1
    else:
        max_id = max(transaction["id"] for transaction in transactions)
        new_transaction["id"] = max_id + 1

    transactions.append(new_transaction)

    return {
        "message": "Transaction added successfully",
        "transaction": new_transaction
    }

@app.delete("/transactions/{transaction_id}")
def delete_transaction(transaction_id: int): 
    for transaction in transactions:
        if transaction["id"] == transaction_id:
            transactions.remove(transaction)
            return {"message": "Transaction deleted successfully"}
    raise HTTPException(status_code=404, detail="Transaction not found")   