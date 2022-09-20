import graphene
from graphqls.query import ScheduleObject
from models.schedule import ScheduleModel
from models.user import UserModel
from db import db

class DeleteSchedule(graphene.Mutation):
    # Return Values
    class Arguments:
        scheduleid = graphene.String()
        usertableid = graphene.String()
    schedule=graphene.Field(lambda:ScheduleObject)
    
    def mutate(self, info, scheduleid,usertableid):
        
        
        schedule =ScheduleModel.delete_schedule_with_user_id(usertableid,scheduleid)
        
        print(schedule)
        db.session.delete(schedule)
        db.session.commit()
        
    
        return DeleteSchedule()