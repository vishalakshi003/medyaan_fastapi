from fastapi import FastAPI
from src.routes.user_route import user_router
app = FastAPI()
app.include_router(user_router)
@app.get('/')
async def home():
    return {"messgae":"initiated"}