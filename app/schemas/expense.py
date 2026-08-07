from __future__ import annotations
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field, ConfigDict


class ExpenseBase(BaseModel):
    description: str = Field(..., min_length=1)
    amount: float = Field(..., gt=0)
    category_id: Optional[int] = None
    custom_category: Optional[str] = None
    owner_id: int


class ExpenseCreate(ExpenseBase):
    pass


class ExpenseUpdate(BaseModel):
    description: Optional[str] = Field(None, min_length=1)
    amount: Optional[float] = Field(None, gt=0)
    category_id: Optional[int] = None
    owner_id: Optional[int] = None


class ExpenseResponse(ExpenseBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
    created_date: datetime


