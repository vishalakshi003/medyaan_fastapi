from models.user_model import User
from schema.user_schema import UserType
from config.database import get_db
from sqlalchemy.future import select

async def fetch_users() -> list[UserType]:
    async for db in get_db():
        result = await db.execute(select(User))
        users = result.scalars().all()
        return [UserType(id=u.id, name=u.name, email=u.email) for u in users]

async def add_user(data) -> UserType:
    async for db in get_db():
        user = User(name=data.name, email=data.email)
        db.add(user)
        await db.commit()
        await db.refresh(user)
        return UserType(id=user.id, name=user.name, email=user.email)
