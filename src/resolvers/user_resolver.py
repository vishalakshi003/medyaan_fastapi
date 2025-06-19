from schema.user_schema import Create_user, User_details,LoginReq,TokenRes
from services.user_service import fetch_users, add_user,token
from strawberry.types import Info
from typing import List
async def get_users() -> List[User_details]:
    return await fetch_users()

async def create_user(data: Create_user,info:Info) -> User_details:
    return await add_user(data,info)
async def login_api(data:LoginReq)->TokenRes:
    return await token(data)
