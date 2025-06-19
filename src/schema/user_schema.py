import strawberry

@strawberry.type
class UserType:
    id: int
    name: str
    email: str

@strawberry.input
class CreateUserInput:
    name: str
    email: str
