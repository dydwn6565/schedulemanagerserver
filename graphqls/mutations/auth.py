
import graphene
from flask_bcrypt import Bcrypt
from models.user import UserModel
from graphqls.messagefield import MessageField
from flask_jwt_extended import create_access_token
from flask_jwt_extended import create_refresh_token

# bcrypt = Bcrypt(app)
class AuthMutation(graphene.Mutation):
    class Arguments:
        userId = graphene.String()
        password = graphene.String()
        
    access_token = graphene.String()
    refresh_token = graphene.String()
    
    
    
    @classmethod
    def mutate(cls,_,info,userId, password):
        
        user = UserModel.find_by_userId(userId)
        
        print(user.json()["password"])
        print(password)
        if user :
            checkPassword = Bcrypt.check_password_hash(user.json()["password"], password) 
            print(checkPassword)
            if(checkPassword):

                return AuthMutation(
                access_token=create_access_token(identity =userId),
                refresh_token=create_refresh_token(userId),
                )
            return MessageField()
       