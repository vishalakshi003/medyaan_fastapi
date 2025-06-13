from fastapi import FastAPI
from src.routes.blog import blog_router

from src.routes.user_routes import user_router
from src.routes.rolemaster import role_router

app=FastAPI()

app.include_router(blog_router,tags=['Blogs'])

app.include_router(user_router,tags=['users'])
app.include_router(role_router,tags=['roles'])
