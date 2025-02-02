from io import BytesIO
from fastapi import FastAPI, Depends
from starlette.responses import StreamingResponse
from sqlalchemy.orm import Session
from app import get_item, create_qr_payload, save_transaction, get_items, get_transaction, get_transactions
from database import get_db, db
from schemas import CreateTransaction
import qrcode

app = FastAPI()

@app.get("/items")
def get_all_item(db: Session = Depends(get_db)):
    return get_items(db)

@app.get("/get_qr")
def getqr(total_price: int):
    payload = create_qr_payload(total_price)
    img = qrcode.make(payload)
    buf = BytesIO()
    img.save(buf)
    buf.seek(0)
    return StreamingResponse(buf, media_type="image/jpeg")

@app.get("/items/{barcode}")
def scan_barcode(barcode: str, db: Session = Depends(get_db)):
    return get_item(db, barcode)

@app.post("/transaction")
def make_transaction(items: list[CreateTransaction], total: int, db: Session = Depends(get_db)):
    return save_transaction(db, items, total)

@app.get("/transaction")
def show_all_transaction(db: Session = Depends(get_db)):
    return get_transactions(db)

@app.get("/transaction/{id}")
def show_transaction(id: int, db: Session = Depends(get_db)):
    return get_transaction(db, id)

