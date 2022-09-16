
import graphene
from flask import Flask
from flask_bcrypt import Bcrypt
from models.schedule import ScheduleModel
from graphqls.query import ScheduleObject
# from graphqls.messagefield import MessageField
# from flask_jwt_extended import create_access_token
# from flask_jwt_extended import create_refresh_token
app = Flask(__name__)
bcrypt = Bcrypt(app)
class GetScheduleMutation(graphene.Mutation):
    class Arguments:
        usertableid = graphene.String()
        # password = graphene.String()
        # usertableid = graphene.Int()
    # scheduleid = graphene.String()
    # title = graphene.String()
    
    # description = graphene.String()
    # start = graphene.String()
    # end = graphene.String()
    # color = graphene.String()

    # schedule= graphene.List(ScheduleObject)
    schedule=graphene.List(lambda:ScheduleObject)
    @classmethod
    def mutate(cls,_,info,usertableid):
        print(usertableid)
        schedule = ScheduleModel.find_by_id(usertableid)
        print(schedule)
        # print(user.json()["password"])
        # print(password)
        if schedule :
           
            
            
                return GetScheduleMutation(
                    schedule
                # usertableid = user.usertableid,
                # access_token=create_access_token(identity =userId),
                # refresh_token=create_refresh_token(userId),
                )
            
        return GetScheduleMutation()
       