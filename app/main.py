from fastapi import FastAPI

from .routes import expense_router, user_router
from .database import Base, engine

Base.metadata.create_all(engine)
app = FastAPI(title="Expense Tracker API")

app.include_router(user_router)
app.include_router(expense_router)


@app.get("/")
def read_root() -> dict[str, str]:
    return {"message": "Expense Tracker API is running"}
