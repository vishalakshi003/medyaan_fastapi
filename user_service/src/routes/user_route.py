from sqlalchemy import Select
from src.models.customuser import CustomUser
from ..schemas.user_schema import *
from fastapi import Depends,APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from src.core.database import get_db,async_get_db
from sqlalchemy.orm import Session,joinedload,selectinload
from src.models.rolemaster import *
user_router=APIRouter()
@user_router.post('/create/users',status_code=201,response_model=UserResponse)
async def create_user(data:UserCreate,db:AsyncSession=Depends(async_get_db)):
    new_user=CustomUser(**data.model_dump())
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return new_user
    
@user_router.get('/get/users',response_model=UserResponse)
async def get_user(id:int,db:AsyncSession=Depends(async_get_db)):
    user_details=await db.get(CustomUser,id)
    return user_details

@user_router.post("/create_role",response_model=RoleResponse)
def create_role(role:RoleCreate,db:Session=Depends(get_db)):
    role_obj = RoleMaster(**role.model_dump())
    db.add(role_obj)
    db.commit()
    db.refresh(role_obj)
    
    return role_obj
@user_router.get("/get-roles",response_model=List[RoleResponse])
def get_role(db:Session=Depends(get_db)):
    role_data = db.query(RoleMaster).all()
    return role_data


@user_router.post("/map-role",response_model=RoleMapResponse)
def createRoleMap(role_map:RoleMapCreate,db:Session=Depends(get_db)):
    rolemap_obj = RoleMapping(**role_map.model_dump())
    db.add(rolemap_obj)
    db.commit()
    db.refresh(rolemap_obj)
    
    return rolemap_obj

@user_router.get("/get_role-map",response_model=List[RoleMapResponse])
def GetRoleResponse(db:Session=Depends(get_db)):
    role_map_data = db.query(RoleMapping).all()
    return role_map_data


@user_router.get('/get/users/sync',response_model=List[UserResponse])
def get_user(db:Session=Depends(get_db)):
    
    user_details = db.query(CustomUser).options(joinedload(CustomUser.role_mappings).joinedload(RoleMapping.role)).all()
    for user in user_details:
        temp = []
        for mapping in user.role_mappings:
            temp.append(RoleResponse.from_orm(mapping.role))
        user.roles = temp
    return user_details

@user_router.get('/get_users/async',response_model=List[UserResponse])
async def get_user_async(db:AsyncSession=Depends(async_get_db)):
    try:
        result = await db.execute(Select(CustomUser).options(selectinload(CustomUser.role_mappings).selectinload(RoleMapping.role)))
        user_details = result.scalars().all()
    except Exception as e:
        user_details=[]
        print(e)
    for user in user_details:
        temp = []
        for mapping in user.role_mappings:
            temp.append(RoleResponse.from_orm(mapping.role))
        user.roles = temp
    return user_details
