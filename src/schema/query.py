import strawberry
from resolvers.user_resolver import get_users

@strawberry.type
class Query:
    users = strawberry.field(resolver=get_users)
