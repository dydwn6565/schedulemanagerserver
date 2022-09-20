import graphene
from graphqls.query import UserObject
from models.user import UserModel
from db import db
class CreateUser(graphene.Mutation):
    
    class Arguments:
        userId = graphene.String(required=True)
        
        password = graphene.String(required=True)
        
    
    user=graphene.Field(lambda:UserObject)
    
    def mutate(self,info,userId,password):
        
        print(userId)
        user = UserModel.find_by_userId(userId)
        
        if user:
            print("hit60")
            return 
            
        print("hit62")
        user = UserModel(userId,password)
        db.session.add(user)
        db.session.commit()
        return CreateUser(user)
        
        
        