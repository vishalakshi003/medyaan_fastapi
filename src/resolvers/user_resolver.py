from schema.user_schema import Create_user, User_details,LoginRequest,TokenResponse
from services.user_service import fetch_users, add_user,token
from strawberry.types import Info
from typing import List
async def get_users(info:Info) -> List[User_details]:
    return await fetch_users(info)

async def create_user(data: Create_user,info:Info) -> User_details:
    return await add_user(data,info)
async def login_api(data:LoginRequest,info:Info)->TokenResponse:
    return await token(data,info)
