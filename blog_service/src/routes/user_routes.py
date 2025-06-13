
from fastapi import APIRouter,Depends, HTTPException
from sqlalchemy import select
from src.dependency import SessionDeps
from..schemas.user_schema import CreateUser, LoginRequest
from ..models.user_models import BlogCustomUser,BlogRoleMapping,BlogRoleMaster
from src.utils import generate_access_token, password_context
from sqlalchemy.ext.asyncio import AsyncSession
user_router=APIRouter()

@user_router.post('/create/user')
async def create_user(user:CreateUser,db:SessionDeps)-> dict:
    try:
        async with db.begin():
            new_user=BlogCustomUser(
                user_name=user.user_name,
                email=user.email,
                mobile_number=user.mobile_number,
                password=password_context.hash(user.password),
                id_proof=user.id_proof        
            )
            db.add(new_user)
            await db.flush()# to push data to get user id
            result=await db.execute(select(BlogRoleMaster).where(BlogRoleMaster.name.in_(user.roles)))
            if not result:
                raise HTTPException(status_code=404,detail="role not found")
            roles=result.scalars()
            for role in roles:
                db.add(BlogRoleMapping(user_id=new_user.id,role_id=role.id))
        await db.refresh(new_user)
        return {"status": "success", "message": "Registration completed", "user_id": new_user.id}
    except Exception as e:
        await db.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    
@user_router.post('/login')
async def login_user(request:LoginRequest,db:SessionDeps):
    results=await db.execute(select(BlogCustomUser).where(BlogCustomUser.mobile_number==request.mobilenumber))
    users=results.scalar()
    if not users or not password_context.verify(request.password,users.password):
        raise HTTPException(status_code=404,detail='mobile no or password is invalid')
    token = generate_access_token(data={
            "user":{
                    "id":users.id,
                    "email":users.email,
                },})
    return token