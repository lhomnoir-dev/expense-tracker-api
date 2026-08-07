from typing import Any

from sqlalchemy.orm import Session

from ..models import Expense, Category
from ..schemas.expense import ExpenseCreate, ExpenseUpdate
from ..utils.seed import seed_categories


def get_default_category(db: Session) -> Category | None:
    return db.query(Category).filter(Category.is_default.is_(True)).first()


def get_or_create_category(db: Session, name: str, user_id: int) -> Category:
    category = (
        db.query(Category)
        .filter(Category.name == name, Category.owner_id == user_id)
        .first()
    )
    if category:
        return category

    new_category = Category(name=name, is_default=False, owner_id=user_id)
    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    return new_category


def get_expenses(db: Session, skip: int = 0, limit: int = 100) -> list[Expense]:
    return db.query(Expense).offset(skip).limit(limit).all()


def get_expense(db: Session, expense_id: int) -> Expense | None:
    return db.query(Expense).filter(Expense.id == expense_id).first()


def create_expense(db: Session, expense: ExpenseCreate) -> Expense:
    category_id = expense.category_id
    if expense.custom_category:
        category = get_or_create_category(db, expense.custom_category, expense.owner_id)
        category_id = category.id
    elif category_id is None:
        seed_categories(db)
        default_category = get_default_category(db)
        if default_category is None:
            raise ValueError("No default category available")
        category_id = default_category.id

    db_expense = Expense(
        description=expense.description,
        amount=expense.amount,
        category_id=category_id,
        owner_id=expense.owner_id,
    )
    db.add(db_expense)
    db.commit()
    db.refresh(db_expense)
    return db_expense


def update_expense(
    db: Session, expense_id: int, expense: ExpenseUpdate
) -> Expense | None:
    db_expense = get_expense(db, expense_id)
    if not db_expense:
        return None

    update_data = expense.model_dump(exclude_none=True)
    for field, value in update_data.items():
        setattr(db_expense, field, value)

    db.commit()
    db.refresh(db_expense)
    return db_expense


def delete_expense(db: Session, expense_id: int) -> bool:
    db_expense = get_expense(db, expense_id)
    if not db_expense:
        return False

    db.delete(db_expense)
    db.commit()
    return True
