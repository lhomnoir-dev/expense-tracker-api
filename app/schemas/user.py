from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field, ConfigDict, EmailStr

class UserModel(BaseModel):
    username: str = Field(..., min_length=2)
    email: EmailStr
    
class UserCreate(UserModel):
    password: str = Field(..., min_length=6)
    
class UserResponse(UserModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    