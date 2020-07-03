from graphene import Schema
from api import RootQuery

schema = Schema(
    query=RootQuery
)
