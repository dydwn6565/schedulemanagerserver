import graphene
from graphqls.query import ScheduleObject
from models.schedule import ScheduleModel
from db import db

class DeleteSchedule(graphene.Mutation):
    # Return Values
    class Arguments:
        scheduleid = graphene.String()
    
    schedule=graphene.Field(lambda:ScheduleObject)
    
    def mutate(self, info, scheduleid):
        
        print("hit99")
        print("id"+scheduleid)
        print(type(scheduleid))
        # schedule =ScheduleModel.find_by_id(3)
        schedule =ScheduleModel.find_by_id(scheduleid)
        
        print(schedule)
        db.session.delete(schedule)
        db.session.commit()
        
    
        return DeleteSchedule()