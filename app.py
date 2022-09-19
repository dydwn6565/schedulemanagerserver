
from tabnanny import check
from flask import Flask,request
import json
from flask_cors import CORS, cross_origin

from flask_jwt_extended import create_access_token
from flask_jwt_extended import create_refresh_token
from flask_jwt_extended import JWTManager
from flask_graphql import GraphQLView

from graphqls.query import Query
import graphene

# from flask_bcrypt import Bcrypt

from graphqls.mutations.createuser import CreateUser
from graphqls.mutations.auth import AuthMutation
from graphqls.mutations.createschedule import CreateSchedule
from graphqls.mutations.deleteuser import DeleteUser
from graphqls.mutations.deleteschedule import DeleteSchedule
from graphqls.mutations.protected import ProtectedMutation
from graphqls.mutations.refresh import RefreshMutation
from graphqls.mutations.getschedule import GetScheduleMutation
from models.user import UserModel
app = Flask(__name__)


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["PROPAGATE_EXCEPTIONS"]= True
app.config["JWT_SECRET_KEY"] = "something"  # change this!
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = 100  # 10 minutes
app.config["JWT_REFRESH_TOKEN_EXPIRES"] = 30  # 30 days

CORS(app, resources={r"*": {"origins": "*"}})

# @app.before_first_request
# def create_tables():
#     db.create_all()

jwt = JWTManager(app)



class Mutation(graphene.ObjectType):
    get_schedule =GetScheduleMutation.Field()
    create_user =CreateUser.Field()
    delete_user = DeleteUser.Field()
    create_schedule =CreateSchedule.Field()
    delete_schedule = DeleteSchedule.Field()
    auth = AuthMutation.Field()
    refresh = RefreshMutation.Field()
    protected = ProtectedMutation.Field()
schema = graphene.Schema(query=Query,mutation=Mutation)


# app.add_url_rule(
#     '/graphql-api',
#     view_func=GraphQLView.as_view(
#         'graphql',
#         schema=schema,
#         graphiql=True # for having the GraphiQL interface
#     )
# )
@app.route("/")
def home():
    return "hi"
# @app.route('/', methods=['POST'])
# # @cross_origin(origin="*")
# def root_route():
#     print("hit")
#     args= request.get_json().get("query")
#     print(type(args))
    
#     result = schema.execute(args)
#     print(result)
#     return {
#         "data": result.data
#     },200
    
if __name__ == '__main__':
    from db import db
    db.init_app(app)
    
    app.run(port=5000, debug=True)
