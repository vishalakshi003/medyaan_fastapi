from fastapi import FastAPI
from src.routes.blog import blog_router

from src.routes.user_routes import user_router
from src.routes.rolemaster import role_router
from scalar_fastapi import get_scalar_api_reference
app=FastAPI()

app.include_router(blog_router,tags=['Blogs'])

app.include_router(user_router,tags=['users'])
app.include_router(role_router,tags=['roles'])

"""used to connect scaler.docs"""
@app.get('/scalar',include_in_schema=False)
def get_scalar_docs():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title='Scalar API',
    )