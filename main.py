from fastapi import FastAPI
from src.models.transaction import Transaction
app = FastAPI()

transactions = []


@app.get("/")
def home():
    return {"message": "Finance API is running"}


@app.get("/transactions")
def get_transactions():
    return transactions


@app.post("/transactions")
def add_transaction(transaction: Transaction):
    transactions.append(transaction.model_dump())

    return {
        "message": "Transaction added successfully",
        "transaction": transaction
    }