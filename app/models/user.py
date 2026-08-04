from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from .. import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)

    custom_category = relationship("Category", back_populates="owner")
    expenses = relationship("Expense", back_populates="expenses")
