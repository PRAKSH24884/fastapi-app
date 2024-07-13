import os
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv

load_dotenv()

DB_URL = os.getenv('DB_URL')
print('DB_URL', DB_URL)
# database = databases.Database(DB_URL)
# metadata = sqlalchemy.MetaData()
# Base = declarative_base()

# metadata.create_all(engine)

engine = create_engine(DB_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
