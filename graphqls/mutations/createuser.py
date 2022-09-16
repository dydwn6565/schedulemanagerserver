import graphene
from graphqls.query import UserObject
from models.user import UserModel
from db import db
class CreateUser(graphene.Mutation):
    
    class Arguments:
        userId = graphene.String(required=True)
        
        password = graphene.String(required=True)
        # schedules = graphene.Int(required=True)
    
    user=graphene.Field(lambda:UserObject)
    
    def mutate(self,info,userId,password):
        
        print(userId)
        user = UserModel.find_by_userId(userId)
        # message = MessageModel("The username is already taken")
        if user:
            print("hit60")
            return 
            # return MessageField(message="The username is already taken"),401
        print("hit62")
        user = UserModel(userId,password)
        # if user:
            # access_token = graphene.String()
            # refresh_token = graphene.String()
        db.session.add(user)
        db.session.commit()
        return CreateUser(user)
        
        # user = UserModel(userId =userId,name=name,password=password)
        # users = UserModel.find_by_id
        