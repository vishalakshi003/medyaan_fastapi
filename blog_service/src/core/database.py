from src.core.config import Config
from sqlalchemy.ext.asyncio import create_async_engine,AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
# from sqlalchemy import create_engine
# import asyncpg

Base=declarative_base()
# sync_engine=create_engine()
# async_engine=create_async_engine(Config.DATABASE_URL)
# print(async_engine)

# async def get_async_db():
#     async_session=sessionmaker(bind=async_engine,class_=AsyncSession,expire_on_commit=False)
#     with async_session() as session:
#         yield session
