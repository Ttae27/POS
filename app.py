from sqlalchemy.orm import Session
from models import Item, Transaction, TransactionDetail
from schemas import CreateTransaction
from datetime import datetime

def get_item(db: Session, code: str):
    item = db.query(Item).filter_by(barcode=code).first()
    if item:
        return item
    return None

def save_transaction(db: Session, transactions: list[CreateTransaction]):
    for transaction in transactions:
        detail_list = []
        for detail in transaction.details:
            kanom = db.query(Item).filter_by(barcode=detail.barcode).first()
            kanom.quantity -= detail.quantity
            db.add(kanom)

            trans_detail = TransactionDetail(quantity=detail.quantity, subtotal=detail.subtotal, item=kanom)
            detail_list.append(trans_detail)
        trans = Transaction(date=transaction.date, time=transaction.time, total=transaction.total)
        trans.transaction_detail.extend(detail_list)

        db.add_all(detail_list)
        db.add(trans)
    db.commit()

    return "Successfully save transaction"

def get_items(db: Session):
    items = db.query(Item).all()
    return items

def get_transaction(db: Session, id: int):
    transaction = db.query(Transaction).filter_by(id = id).all()
    temp = db.query(TransactionDetail).filter_by(transaction_id=id).all()
    transaction.extend(temp)
    return transaction

def get_transactions(db: Session):
    transaction = db.query(Transaction).all()
    return transaction