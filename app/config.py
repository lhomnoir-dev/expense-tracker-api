from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

engine = create_engine()
SessionLocal = sessionmaker()