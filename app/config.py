import os
from dotenv import load_dotenv

load_dotenv()

DB_user=os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")

DATABASE_URL = f"postgresql://{DB_user}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"