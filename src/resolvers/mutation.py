import strawberry
from resolvers.user_resolver import create_user,login_api
from schema.user_schema import User_details,TokenResponse
from services.user_service import fetch_users, add_user,token
from schema.user_schema import Create_user, User_details,LoginRequest,TokenResponse
from strawberry.types import Info

@strawberry.type
class Mutation:
    # create_user: User_details = strawberry.mutation(resolver=create_user)
    # login_user: TokenResponse=strawberry.mutation(resolver=login_api)
    
    @strawberry.mutation
    async def create_user(data: Create_user,info:Info) -> User_details:
        await add_user(data,info)
    
    @strawberry.mutation
    async def login_api(data:LoginRequest,info:Info)->TokenResponse:
        return await token(data,info)
