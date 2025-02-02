from pydantic import BaseModel

class CreateTransaction(BaseModel):
    barcode: str
    quantity: int
    subtotal: int