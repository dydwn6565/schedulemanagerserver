
import graphene
from flask import Flask
from flask_bcrypt import Bcrypt
from models.schedule import ScheduleModel
from graphqls.query import ScheduleObject

app = Flask(__name__)
bcrypt = Bcrypt(app)
class GetScheduleMutation(graphene.Mutation):
    class Arguments:
        usertableid = graphene.String()
     
    schedule=graphene.List(lambda:ScheduleObject)
    @classmethod
    def mutate(cls,_,info,usertableid):
        print(usertableid)
        schedule = ScheduleModel.find_by_id(usertableid)
        print(schedule)
        
        if schedule :
           
            
            
                return GetScheduleMutation(
                    schedule
                
                )
            
        return GetScheduleMutation()
       