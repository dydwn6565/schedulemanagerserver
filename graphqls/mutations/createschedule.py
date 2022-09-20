

import graphene
from graphqls.query import ScheduleObject
from models.schedule import ScheduleModel
from graphqls.messagefield import MessageField
from db import db
class CreateSchedule(graphene.Mutation):

    class Arguments:
        title = graphene.String(required=True)
        description = graphene.String(required=True)
        start = graphene.String(required=True)
        end = graphene.String()
        color=graphene.String(required=True)
        userId = graphene.Int(required=True)
        

    schedule=graphene.Field(lambda:ScheduleObject)
    
    def mutate(self,info,title,description,start,end,color,userId):
        
        schedule = ScheduleModel(title ,description,start,end,color,userId)
        
        
        db.session.add(schedule)
        
        db.session.commit()

        
        return MessageField(message="Successfullly inserted")
        
