from sqlalchemy.orm import Session
from models import Item, Transaction, TransactionDetail
from promptpay import qrcode
from schemas import CreateTransaction
from datetime import datetime

def get_item(db: Session, code: str):
    item = db.query(Item).filter_by(barcode=code).first()
    return item

def create_qr_payload(total_price: int):
    phone_number = "0972525215"
    payload = qrcode.generate_payload(phone_number, total_price)
    return payload

def save_transaction(db: Session, items: list[CreateTransaction], amount: int):
    all_detail = []
    for item in items:
        kanom = db.query(Item).filter_by(id=item.id).first()
        trans_detail = TransactionDetail(quantity=item.quantity, total=item.total, item=kanom)

        kanom.quantity -= item.quantity
        db.add(kanom)

        all_detail.append(trans_detail)

    transaction = Transaction(date=datetime.now().date(), time=datetime.now().time(), amount=amount)
    transaction.transaction_detail.extend(all_detail)

    db.add_all(all_detail)
    db.add(transaction)
    db.commit()
    return "Successfully save transaction!"

def get_items(db: Session):
    items = db.query(Item).all()
    return items