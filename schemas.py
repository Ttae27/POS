from pydantic import BaseModel

class CreateTransaction(BaseModel):
    id: int
    quantity: int
    total: int