from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from ..database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)

    custom_categories = relationship(
        "Category",
        back_populates="owner",
        cascade="all, delete-orphan",
    )
    expenses = relationship(
        "Expense",
        back_populates="owner",
        cascade="all, delete-orphan",
    )
