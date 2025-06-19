import strawberry

@strawberry.input
class Create_user:
    email:str
    mobile_number:str
    password:str
    password1:str
@strawberry.type
class User_details:
    id:int
    email:str
    mobile_number:str

@strawberry.input
class LoginRequest:
    mobile_number:str
    password:str
@strawberry.type
class TokenResponse:
    status:str
    token:str
