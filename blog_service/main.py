from fastapi import FastAPI
from src.routes.user_routes import user_router
from src.routes.rolemaster import role_router
app=FastAPI()

app.include_router(user_router)
app.include_router(role_router)