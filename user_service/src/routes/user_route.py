from src.models.customuser import CustomUser
from ..schemas.user_schema import UserCreate,UserResponse
from fastapi import Depends,APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from src.core.database import get_db,async_get_db
from sqlalchemy.orm import Session
user_router=APIRouter()
@user_router.post('/create/users',status_code=201,response_model=UserResponse)
async def create_user(data:UserCreate,db:AsyncSession=Depends(async_get_db)):
    new_user=CustomUser(**data.model_dump())
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return new_user
    
@user_router.get('/get/users',response_model=UserResponse)
async def get_user(id:int,db:AsyncSession=Depends(async_get_db)):
    user_details=await db.get(CustomUser,id)
    return user_details

