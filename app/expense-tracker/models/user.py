from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy import String, Integer, ForeignKey
from ..db import db


class User(db.Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    username: Mapped[str] = mapped_column(String, unique=True, index=True)
    email: Mapped[str] = mapped_column(String, unique=True, index=True)
    password: Mapped[str] = mapped_column(String)

    expenses: Mapped[list["Expense"]] = relationship("Expense", back_populates="user")