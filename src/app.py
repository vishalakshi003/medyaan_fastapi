from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from schema.query import Query
from schema.mutation import Mutation
import strawberry

schema = strawberry.Schema(query=Query, mutation=Mutation)
graphql_app = GraphQLRouter(schema)

app = FastAPI(title="GraphQL Service")
app.include_router(graphql_app, prefix="/graphql")
