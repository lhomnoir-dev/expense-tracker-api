from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy import  ForeignKey, ForeignKey, Integer, String, Enum
import enum
from ..db import db


class ExpenseCategory(enum.Enum):
    GROCERIES = "Groceries"
    ELECTRONICS = "Electronics"
    LEISURE = "Leisure"
    HEALTH="Health"
    CLOTHING = "Clothing"
    FOOD = "Food"
    UTILITIES = "Utilities"
    OTHERS = "Others"

    
class Expense(db.Base):
    __tablename__ = "expenses"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    description: Mapped[str] = mapped_column(String, index=True)
    amount: Mapped[float] = mapped_column()
    category: Mapped[ExpenseCategory] = mapped_column(Enum(ExpenseCategory), index=True)

    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))
    user: Mapped["User"] = relationship("User", back_populates="expenses")