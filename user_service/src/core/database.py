from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from src.core.config import Config
from sqlalchemy.ext.asyncio import create_async_engine,AsyncSession

engine = create_engine("postgresql://postgres.litmwhoslkfocmnsulcb:MedyaanFastapi@aws-0-ap-south-1.pooler.supabase.com:5432/postgres")

SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

async_engine=create_async_engine(Config.DATABASE_URL)

async def async_get_db():
    AsyncSessionMaker=sessionmaker(bind=async_engine,class_=AsyncSession,expire_on_commit=False)

    async with AsyncSessionMaker() as session:
        yield session