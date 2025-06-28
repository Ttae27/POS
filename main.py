from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app import save_transaction, get_items, get_transaction, get_transactions
from database import get_db
from schemas import CreateTransaction

app = FastAPI()

@app.get("/items")
def get_all_item(db: Session = Depends(get_db)):
    return get_items(db)

@app.post("/transaction")
def trans(transac: list[CreateTransaction], db: Session = Depends(get_db)):
    return save_transaction(db, transac)

@app.get("/transaction")
def show_all_transaction(db: Session = Depends(get_db)):
    return get_transactions(db)

@app.get("/transaction/{id}")
def show_transaction(id: int, db: Session = Depends(get_db)):
    return get_transaction(db, id)