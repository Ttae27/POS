from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv
import os

load_dotenv()
host = os.getenv('HOST')
port = os.getenv('PORT')
user = os.getenv('USER')
password = os.getenv('PASSWORD')
dbname = os.getenv('DB_NAME')

URL_DATABASE = 'postgresql://' + user + ':' + password + '@' + host + ':' + port + '/' + dbname

engine = create_engine(URL_DATABASE)
sessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()