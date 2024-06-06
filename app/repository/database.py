import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

host = os.getenv('DB_HOST', "localhost")
user = os.getenv('PG_USER', "postgres")
password= os.getenv('PG_PASSWORD', "postgres")
port = os.getenv('DB_PORT', 5432)
database_name = os.getenv('DB_DATABASE_NAME', "postgres")

engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{database_name}')
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    return db  # Return the session directly