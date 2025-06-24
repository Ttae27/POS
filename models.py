from sqlalchemy import Column, ForeignKey, Integer, String, Date, Time
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import Base, engine

class BaseModel(Base):
    __abstract__ = True

    id = Column(Integer, primary_key=True)

class Transaction(BaseModel):
    __tablename__ = 'transactions'

    date = Column(Date)
    time = Column(Time)
    total = Column(Integer)
    transaction_detail: Mapped[list["TransactionDetail"]] = relationship(back_populates='transaction')

class TransactionDetail(BaseModel):
    __tablename__ = 'transaction_details'

    quantity = Column(Integer)
    subtotal = Column(Integer)
    item_barcode = Column(ForeignKey("items.barcode"))
    item: Mapped['Item'] = relationship()
    transaction_id: Mapped[int] = mapped_column(ForeignKey('transactions.id'))
    transaction: Mapped['Transaction'] = relationship(back_populates='transaction_detail')

class Item(Base):
    __tablename__ = 'items'

    barcode = Column(String, primary_key=True) 
    name = Column(String)
    price = Column(Integer)
    quantity = Column(Integer)

Base.metadata.create_all(engine)