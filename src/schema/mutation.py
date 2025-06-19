import strawberry
from resolvers.user_resolver import create_user,login_api
from schema.user_schema import User_details,TokenRes

@strawberry.type
class Mutation:
    create_user: User_details = strawberry.mutation(resolver=create_user)
    login_user: TokenRes=strawberry.mutation(resolver=login_api)
