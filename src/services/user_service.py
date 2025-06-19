from graphql import GraphQLError
from models.user_model import CustomUser
from schema.user_schema import UserType,TokenRes
from config.database import get_db
from sqlalchemy.future import select
from strawberry.types import Info
from sqlalchemy.ext.asyncio import AsyncSession
from src.utils.password import generate_access_token, password_context

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
    
    
async def token(data,info:Info)->TokenRes:
    db:AsyncSession=info.context["db"]
    user=db.execute(select(CustomUser).where(CustomUser.mobile_number==data.mobile_no))
    if not user or not password_context.verify(data.password,user.password):
        raise GraphQLError('mobile no or password is invalid')
    token = generate_access_token(data={
            "user":{
                    "id":user.id,
                    "email":user.email,
                },})
    return TokenRes(
            status="success",
            token= token)