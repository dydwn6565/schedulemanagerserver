import graphene

from graphqls.union.protectedunion import ProtectedUnion
from graphqls.messagefield import MessageField
from db import db
from flask_jwt_extended import create_access_token
from flask_graphql_auth import (

    mutation_jwt_refresh_token_required,
    get_jwt_identity
)

class RefreshMutation(graphene.Mutation):
    class Arguments(object):
        refresh_token = graphene.String()

    new_token = graphene.String()

    @classmethod
    @mutation_jwt_refresh_token_required
    def mutate(self, _):
        current_user = get_jwt_identity()
        return RefreshMutation(
            new_token=create_access_token(identity=current_user),
            
        )