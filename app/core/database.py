from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

DB_HOST = os.getenv("OLTP_DB_HOST")
DB_PORT = os.getenv("OLTP_DB_PORT")
DB_NAME = os.getenv("OLTP_DB_NAME")
DB_USER = os.getenv("OLTP_DB_USER")
DB_PASSWORD = os.getenv("OLTP_DB_PASSWORD")

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()