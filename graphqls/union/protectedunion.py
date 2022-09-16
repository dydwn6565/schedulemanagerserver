
import graphene
from graphqls.messagefield import MessageField
from flask_graphql_auth import (
    AuthInfoField,
)
class ProtectedUnion(graphene.Union):
    class Meta:
        types = (MessageField, AuthInfoField)
        # types = (MessageField)

    @classmethod
    def resolve_type(cls, instance, info):
        return type(instance)
