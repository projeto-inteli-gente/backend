from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
from urllib.parse import quote
import os

from intelligentedb.indicators.read_data import *

load_dotenv()
USER = os.getenv("DB_USERNAME")
NAME = os.getenv("DB_NAME")
PORT = os.getenv("DB_PORT")
HOST = os.getenv("DB_HOST")
PASSWORD = quote(os.getenv("DB_PASSWORD"))

DATABASE_URL = f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{NAME}"

engine = create_engine(DATABASE_URL, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()