from sqlalchemy.orm import Session
from fastapi import HTTPException
from models import Item, Transaction, TransactionDetail
from schemas import CreateTransaction

def save_transaction(db: Session, transactions: list[CreateTransaction]):
    try:
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
    except:
        db.rollback()
        return "Failed to save transaction"

def get_items(db: Session):
    items = db.query(Item).all()
    if not items:
        raise HTTPException(status_code=404, detail="Item not found")

    return items

def get_transaction(db: Session, id: int):
    transaction = db.query(Transaction).filter_by(id = id).all()
    if not transaction:
        raise HTTPException(status_code=404, detail="Transaction not found")
    
    temp = db.query(TransactionDetail).filter_by(transaction_id=id).all()
    if not temp:
        raise HTTPException(status_code=404, detail="TransactionDetail not found")
    
    transaction.extend(temp)
    return transaction

def get_transactions(db: Session):
    transaction = db.query(Transaction).all()
    if not transaction:
        raise HTTPException(status_code=404, detail="Transactions not found")

    return transaction