from fastapi import APIRouter, HTTPException
from typing import Dict
from datetime import datetime
from app.models.Transaction import Transaction


router = APIRouter(
    prefix="/transactions",
    tags=["Transactions"],
)

database: Dict[str, Transaction] = {
    "1": Transaction(
        id="1",
        client_id="client_1",
        transaction_amount=100.0,
        transaction_time=datetime(2024, 4, 13, 10, 30),
        description="Example transaction 1",
    ),
    "2": Transaction(
        id="2",
        client_id="client_2",
        transaction_amount=150.0,
        transaction_time=datetime(2024, 4, 13, 11, 45),
        description="Example transaction 2",
    ),
    "3": Transaction(
        id="3",
        client_id="client_1",
        transaction_amount=200.0,
        transaction_time=datetime(2024, 4, 13, 13, 15),
        description="Example transaction 3",
    ),
}


# Create
@router.post("/", response_model=Transaction)
async def create_transaction(transaction: Transaction):
    if transaction.id in database:
        raise HTTPException(status_code=400, detail="Transaction ID already exists")
    database[transaction.id] = transaction
    return transaction


# Read
@router.get("/{transaction_id}", response_model=Transaction)
async def read_transaction(transaction_id: str):
    if transaction_id not in database:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return database[transaction_id]


# Update
@router.put("/{transaction_id}", response_model=Transaction)
async def update_transaction(transaction_id: str, transaction: Transaction):
    if transaction_id not in database:
        raise HTTPException(status_code=404, detail="Transaction not found")
    database[transaction_id] = transaction
    return transaction


# Delete
@router.delete("/{transaction_id}", response_model=Transaction)
async def delete_transaction(transaction_id: str):
    if transaction_id not in database:
        raise HTTPException(status_code=404, detail="Transaction not found")
    deleted_transaction = database.pop(transaction_id)
    return deleted_transaction
