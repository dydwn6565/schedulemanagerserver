
import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from models.schedule import ScheduleModel
from models.user import UserModel

class ScheduleObject(SQLAlchemyObjectType):
   class Meta:
       model = ScheduleModel
       interfaces = (graphene.relay.Node, )

# class MessageObject(SQLAlchemyObjectType):
#    class Meta:
#        model = MessageModel
#        interfaces = (graphene.relay.Node, )

class UserObject(SQLAlchemyObjectType):
   class Meta:
       model = UserModel
       interfaces = (graphene.relay.Node, )



class Query(graphene.ObjectType):
    node = graphene.relay.Node.Field()
    all_schedules = SQLAlchemyConnectionField(ScheduleObject)
    all_users = SQLAlchemyConnectionField(UserObject)

