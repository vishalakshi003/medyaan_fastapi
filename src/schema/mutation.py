import strawberry
from resolvers.user_resolver import create_user
from schema.user_schema import CreateUserInput, UserType

@strawberry.type
class Mutation:
    create_user: UserType = strawberry.mutation(resolver=create_user)
