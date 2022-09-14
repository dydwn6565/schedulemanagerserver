import sqlite3
from models.user import UserModel
# from flask_graphql import GraphQLView
class UserRegister():


    def post(self):
        data = UserModel(data["userId"])

        if(UserModel.find_by_name(data["userId"])):
            return{"message": "A user with that userid already exists"},400

        user = UserModel(data["userId"],data["password"])
        user.save_to_db()

        return {"message":"User created successfully."},201