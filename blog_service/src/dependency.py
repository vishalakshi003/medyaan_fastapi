from typing_extensions import Annotated
from src.core.database import get_async_db
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends

SessionDeps=Annotated[AsyncSession,Depends(get_async_db)]
