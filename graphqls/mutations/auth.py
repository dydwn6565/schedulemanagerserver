
import graphene
from flask import Flask
from flask_bcrypt import Bcrypt
from models.user import UserModel
from graphqls.messagefield import MessageField
from flask_jwt_extended import create_access_token
from flask_jwt_extended import create_refresh_token
app = Flask(__name__)
bcrypt = Bcrypt(app)
class AuthMutation(graphene.Mutation):
    class Arguments:
        userId = graphene.String()
        password = graphene.String()
        usertableid = graphene.Int()
    access_token = graphene.String()
    refresh_token = graphene.String()
    usertableid = graphene.Int()
    
    
    @classmethod
    def mutate(cls,_,info,userId, password):
        
        user = UserModel.find_by_userId(userId)
        
        # print(user.json()["password"])
        # print(password)
        if user :
            print(type(user.usertableid))
            checkPassword = bcrypt.check_password_hash(user.json()["password"], password) 
            print(checkPassword)
            if(checkPassword):

                return AuthMutation(
                usertableid = user.usertableid,
                access_token=create_access_token(identity =userId),
                refresh_token=create_refresh_token(userId),
                )
            return AuthMutation()
        return AuthMutation()
       