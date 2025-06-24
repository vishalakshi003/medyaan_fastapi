from graphql import GraphQLError
from models.user_model import CustomUser
from schema.user_schema import User_details,Create_user,TokenResponse
from config.database import get_db
from sqlalchemy.future import select
# from strawberry.types import Info
from sqlalchemy.ext.asyncio import AsyncSession
from utils.password import generate_access_token, password_context
from typing import List


async def fetch_users(info) -> List[User_details]:
    db:AsyncSession=info.context["db"]
    payload=info.context["user"]
    # if not payload:
    #     raise GraphQLError('unauthorized')

    if payload is not None:
       id = payload["user"]["id"]
       result = await db.execute(select(CustomUser).where(CustomUser.id==id))
    else:
        result = await db.execute(select(CustomUser))
    users = result.scalars().all()
    return [User_details(id=u.id, mobile_number=u.mobile_number, email=u.email) for u in users]

async def add_user(data,info) -> User_details:
    try:
        db: AsyncSession = info.context["db"]
        # async with db.begin():
        if data.password != data.password1:
            raise GraphQLError('enter correct password',extensions={"status_code":400})
        hash_password=password_context.hash(data.password)
        emails_exists_res=await db.execute(select(CustomUser).where(CustomUser.email==data.email))
        email_exists=emails_exists_res.scalar_one_or_none()
        if email_exists:
            raise GraphQLError('email already exists',extensions={"status_code":400})
        
        users=CustomUser(email=data.email,mobile_number=data.mobile_number,password=hash_password)
        db.add(users)
        await db.commit()
        await db.refresh(users)
        print(users)
        return users

    except GraphQLError as gql_error:
        raise gql_error 
    
async def token(data,info)->TokenResponse:
    db:AsyncSession=info.context["db"]
    result=await db.execute(select(CustomUser).where(CustomUser.mobile_number==data.mobile_number))
    user = result.scalar_one_or_none()
    if not user or not password_context.verify(data.password,user.password):
        raise GraphQLError('mobile no or password is invalid')
    token = generate_access_token(data={
            "user":{
                    "id":user.id,
                    "email":user.email,
                },})
    return TokenResponse(
            status="success",
            token= token)