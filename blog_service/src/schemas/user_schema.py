from pydantic import BaseModel
from typing import Optional,List,Dict,Any
class UserBase(BaseModel):
    name:str
    email:str
    mobile_number:str
    id_proof: List[Dict[str, Any]]

class CreateUser(UserBase):
    password:str
    roles: List[str] 

class UserResponse(UserBase):
    id:int


class RoleBase(BaseModel):
    name:str
    desc:Optional[str]=None
class CreateRole(RoleBase):
    pass
class RoleResponse(RoleBase):
    id:int


class LoginRequest(BaseModel):
    mobilenumber:str
    password:str