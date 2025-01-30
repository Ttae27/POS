from io import BytesIO
from fastapi import FastAPI, Depends
from starlette.responses import StreamingResponse
from sqlalchemy.orm import Session
from app import get_item, create_qr_payload, save_transaction, get_items
from database import  get_db
from schemas import CreateTransaction
import qrcode

app = FastAPI()

@app.get("/get_all")
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

@app.get("/{barcode}")
def scan_barcode(barcode: str, db: Session = Depends(get_db)):
    return get_item(db, barcode)

@app.post("/transaction")
def make_transaction(items: list[CreateTransaction], amount: int, db: Session = Depends(get_db)):
    return save_transaction(db, items, amount)

