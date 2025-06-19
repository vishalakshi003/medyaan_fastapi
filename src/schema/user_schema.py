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
class LoginReq:
    mobile_no:str
    password:str
@strawberry.type
class TokenRes:
    status:str
    token:str
