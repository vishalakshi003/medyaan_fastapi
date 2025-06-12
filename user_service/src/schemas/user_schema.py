from pydantic import BaseModel, ConfigDict, EmailStr
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

    
class RoleCreate(BaseModel):
    name: str
    
class RoleResponse(BaseModel):
    id:int
    name:str

    model_config = ConfigDict(from_attributes=True)

    
    class config:
        from_attributes = True

class RoleMapCreate(BaseModel):
    userid:int
    roleid:int
    
class RoleMapResponse(BaseModel):
    id: int
    userid: int
    roleid: int

class UserResponse(UserBase):
    id: int
    created_at: datetime
    updated_at: datetime
    is_active: bool
    roles:List[RoleResponse]

    model_config = ConfigDict(from_attributes=True)

class UserCreate(UserBase):
    password: str