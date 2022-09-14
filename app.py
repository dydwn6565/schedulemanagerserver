
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_graphql_auth import (
    AuthInfoField,
    GraphQLAuth,
    get_jwt_identity,
    get_raw_jwt,
    # create_access_token,
    # create_refresh_token,
    query_jwt_required,
    mutation_jwt_refresh_token_required,
    mutation_jwt_required,
)
from flask_jwt_extended import create_access_token
from flask_jwt_extended import create_refresh_token
from flask_jwt_extended import JWTManager
from flask_graphql import GraphQLView
from models.user import UserModel
from models.schedule import ScheduleModel
import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
app = Flask(__name__)
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["PROPAGATE_EXCEPTIONS"]= True
app.config["JWT_SECRET_KEY"] = "something"  # change this!
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = 10  # 10 minutes
app.config["JWT_REFRESH_TOKEN_EXPIRES"] = 30  # 30 days



@app.before_first_request
def create_tables():
    db.create_all()

jwt = JWTManager(app)


class ScheduleObject(SQLAlchemyObjectType):
   class Meta:
       model = ScheduleModel
       interfaces = (graphene.relay.Node, )

class UserObject(SQLAlchemyObjectType):
   class Meta:
       model = UserModel
       interfaces = (graphene.relay.Node, )

class Query(graphene.ObjectType):
    node = graphene.relay.Node.Field()
    all_schedules = SQLAlchemyConnectionField(ScheduleObject)
    all_users = SQLAlchemyConnectionField(UserObject)


class CreateUser(graphene.Mutation):
    
    class Arguments:
        userId = graphene.String(required=True)
        name = graphene.String(required=True)
        password = graphene.String(required=True)
        # schedules = graphene.Int(required=True)
    
    user=graphene.Field(lambda:UserObject)
    
    def mutate(self,info,userId,name,password):
        # db.create_all()
        print(userId)
        user = UserModel.find_by_userId(userId)
        # print("hit58")
        if user:
            print("hit60")
            return MessageField(message="The username is already taken")
        print("hit62")
        user = UserModel(userId,name,password)
        # if user:
            # access_token = graphene.String()
            # refresh_token = graphene.String()
        db.session.add(user)
        db.session.commit()
        return CreateUser(user)
        # user = UserModel(userId =userId,name=name,password=password)
        # users = UserModel.find_by_id
        

        


class CreateSchedule(graphene.Mutation):

    class Arguments:
        title = graphene.String(required=True)
        description = graphene.String(required=True)
        start = graphene.String(required=True)
        end = graphene.String(required=True)
        userId = graphene.Int(required=True)
        # schedules = graphene.Int(required=True)

    user=graphene.Field(lambda:UserObject)
    
    def mutate(self,info,title,description,start,end,userId):
        
        schedule = ScheduleModel(title =title,description=description,start=start,end=end,userId=userId)
        # db.create_all()
        db.session.add(schedule)
        db.session.commit()

        return CreateSchedule()


class MessageField(graphene.ObjectType):
    message = graphene.String()


class ProtectedUnion(graphene.Union):
    class Meta:
        types = (MessageField, AuthInfoField)

    @classmethod
    def resolve_type(cls, instance, info):
        return type(instance)


class AuthMutation(graphene.Mutation):
    class Arguments:
        userId = graphene.String()
        password = graphene.String()
        
    access_token = graphene.String()
    refresh_token = graphene.String()
    
    
    
    @classmethod
    def mutate(cls,_,info,userId, password):
        
        user = UserModel.find_by_userId(userId)
        if user :
            print("hit")
            return AuthMutation(
            access_token=create_access_token(identity =userId),
            refresh_token=create_refresh_token(userId),
        )
       


class ProtectedMutation(graphene.Mutation):
    class Arguments(object):
        token = graphene.String()
    
    message = graphene.Field(ProtectedUnion)

    @classmethod
    @mutation_jwt_required
    def mutate(cls, _, info):
        return ProtectedMutation(
            message=MessageField(message="Protected mutation works")
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



class Mutation(graphene.ObjectType):
    create_user =CreateUser.Field()
    create_schedule =CreateSchedule.Field()
    auth = AuthMutation.Field()
    refresh = RefreshMutation.Field()
    protected = ProtectedMutation.Field()
schema = graphene.Schema(query=Query,mutation=Mutation)


app.add_url_rule(
    '/graphql-api',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True # for having the GraphiQL interface
    )
)

# @app.before_first_request
# def create_tables():
#     db.create_all()

# @app.route("/")
# def home():
#     return "Hello, Flask!"

# @app.route("/asf")
# def home():
#     return "Hello, Flask!"

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    
    app.run(port=5000, debug=True)
