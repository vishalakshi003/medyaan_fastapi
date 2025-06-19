from schema.user_schema import CreateUserInput, UserType,LoginReq,TokenRes
from services.user_service import fetch_users, add_user,token

async def get_users() -> list[UserType]:
    return await fetch_users()

async def create_user(data: CreateUserInput) -> UserType:
    return await add_user(data)
async def login_api(data:LoginReq)->TokenRes:
    return await token(data)
