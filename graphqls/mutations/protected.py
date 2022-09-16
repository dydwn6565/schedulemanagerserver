import graphene

from graphqls.union.protectedunion import ProtectedUnion
from graphqls.messagefield import MessageField
from db import db

from flask_graphql_auth import (

    mutation_jwt_required,
)
class ProtectedMutation(graphene.Mutation):
    class Arguments(object):
        token = graphene.String()
    
    message = graphene.Field(ProtectedUnion)

    @classmethod
    @mutation_jwt_required
    def mutate(cls, _, info):
        return ProtectedMutation(
            message=MessageField(message="Protected mutation works")
        )
