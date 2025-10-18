from sqlalchemy import URL, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import DATABASE_NAME, DATABASE_HOST, DATABASE_PASSWORD, DATABASE_USER
from sqlmodel import create_engine, SQLModel

url_object = URL.create("postgresql",
                        username=DATABASE_USER,
                        password=DATABASE_PASSWORD,
                        host=DATABASE_HOST,
                        database=DATABASE_NAME)

engine = create_engine(url_object)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def init_db():
    SQLModel.metadata.create_all(engine)
