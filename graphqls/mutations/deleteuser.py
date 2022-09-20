
import graphene

from graphqls.messagefield import MessageField
from db import db

class DeleteUser(graphene.Mutation):
    # Return Values
    class Arguments:
        id = graphene.String()
    
    message=graphene.Field(lambda:MessageField)
    
    def mutate(self, info, id):
        print("hit99")
        print(id)
        db.session.delete(id)
        db.session.commit()
        
    
        return MessageField("Successfullly deleted")
