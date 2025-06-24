import strawberry
# from resolvers.user_resolver import get_users
from schema.user_schema import User_details
from typing import List
from strawberry.types import Info
from services.user_service import fetch_users

@strawberry.type
class Query:
    # users = strawberry.field(resolver=get_users)
    @strawberry.field
    async def get_users(info:Info) -> List[User_details]:
      return await fetch_users(info)
    
