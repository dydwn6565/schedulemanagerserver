import graphene


class MessageField(graphene.ObjectType):
    
    message = graphene.String()