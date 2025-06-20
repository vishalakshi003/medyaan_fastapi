from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from api.graphql.query import Query
from api.graphql.mutation import Mutation
import strawberry
from config.database import get_context

schema = strawberry.Schema(query=Query, mutation=Mutation)
graphql_app = GraphQLRouter(schema,context_getter=get_context)

app = FastAPI(title="GraphQL Service")
app.include_router(graphql_app, prefix="/graphql")
