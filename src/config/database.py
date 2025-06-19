from fastapi import Depends,Request
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from config.settings import Config
from sqlalchemy.ext.declarative import declarative_base

from utils.password import jwt_decode_payload

Base=declarative_base()
engine = create_async_engine(Config.DATABASE_URL)
AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session

# async def get_context(db: AsyncSession = Depends(get_db)):
#     return {"db": db}

async def get_context(request:Request,db: AsyncSession = Depends(get_db)):
    user = None
    auth_header = request.headers.get("Authorization")
    if auth_header and auth_header.startswith("Bearer "):
        token = auth_header.split(" ")[1]
        user = jwt_decode_payload(token)

    return {"db": db,"user":user}