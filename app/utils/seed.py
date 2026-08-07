from sqlalchemy.orm import Session

from ..models import Category

DEFAULT_CATEGORIES = [
    "groceries",
    "leisure",
    "electronics",
    "utilities",
    "clothing",
    "others",
]


def seed_categories(db: Session) -> None:
    for name in DEFAULT_CATEGORIES:
        exists = (
            db.query(Category)
            .filter(Category.name == name, Category.is_default.is_(True))
            .first()
        )
        if not exists:
            db.add(Category(name=name, is_default=True, owner_id=None))
    db.commit()
