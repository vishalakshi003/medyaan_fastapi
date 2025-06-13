from typing import List
from fastapi import APIRouter,Depends, HTTPException
from src.core.database import get_async_db
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload,joinedload
from sqlalchemy import select,Select
from src.schemas.blog import *
from src.models.Blog import *
from src.models.user_models import *

blog_router = APIRouter()

@blog_router.get("/get-blogs",response_model=List[BlogResponse])
async def get_blogs(db:AsyncSession=Depends(get_async_db)):
    blog_details = Select(Blog).options(joinedload(Blog.user))
    result = await db.execute(blog_details)
    return result.scalars().all()

@blog_router.post("/create-blog",response_model=BlogResponse,responses={404:{"description":"Not Found"}})
async def create_blog(data:BlogCreate,db:AsyncSession=Depends(get_async_db)):
    
    id = data.userid
    id_result = (await db.execute(Select(BlogCustomUser).where(BlogCustomUser.id == id))).scalars().first()
    if id_result is None:
        raise HTTPException(status_code=404, detail="User not found")
    blog_data = Blog(**data.model_dump())
    db.add(blog_data)
    await db.commit()
    await db.refresh(blog_data)
    return blog_data

    