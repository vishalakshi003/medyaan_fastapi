from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import date, datetime

class UserBase(BaseModel):
    name: str
    email: EmailStr
    balance: Optional[float]
    bio: Optional[str]
    preferences: Optional[dict]
    tags: Optional[List[str]]
    birth_date: Optional[date]

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    id: int
    created_at: datetime
    updated_at: datetime
    is_active: bool

    
