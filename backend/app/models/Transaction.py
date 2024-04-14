from pydantic import BaseModel
from datetime import datetime


class Transaction(BaseModel):
    id: str
    client_id: str
    transaction_amount: float
    transaction_time: datetime
    description: str
