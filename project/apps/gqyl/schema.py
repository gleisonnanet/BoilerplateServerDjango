import graphene

from project.apps.gqyl.mutations import Mutations
from project.apps.gqyl.query import QueryDefinition


class Query(QueryDefinition, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutations)
