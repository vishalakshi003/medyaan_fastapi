from models.user_model import User
from schema.user_schema import UserType

def map_user_to_type(user: User) -> UserType:
    return UserType(id=user.id, name=user.name, email=user.email)
