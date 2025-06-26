from pydantic import BaseModel
from typing import List
from datetime import date, time

class TransactionDetail(BaseModel):
    barcode: str
    quantity: int
    subtotal: int

class CreateTransaction(BaseModel):
    total: int
    date: date
    time: time
    details: List[TransactionDetail]