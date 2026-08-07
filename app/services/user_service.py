from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from ..models import User
from ..schemas.user import UserCreate
from ..utils.hashing import hash_password, verify_password


def create_user(user: UserCreate, db: Session):
    try:
        db_user = User(
            username=user.username,
            email=user.email,
            password=hash_password(user.password)
            
        )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    except SQLAlchemyError as e:
        raise e
    
