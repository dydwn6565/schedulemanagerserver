import sqlite3
from db import db


class ScheduleModel(db.Model):
    __tablename__ ='schedule'

    scheduleid=db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(256),index=True,nullable=False)
    description=db.Column(db.Text,nullable=False)
    start =db.Column(db.String(80),nullable=False)
    end =db.Column(db.String(80),nullable=True)
    color=db.Column(db.String(20),nullable=False)
    userId =db.Column(db.Integer, db.ForeignKey("users.usertableid"),nullable=False)

    def __init__(self,title,description,start,end,color,userId):
        self.title = title
        self.description = description
        self.start = start
        self.end = end
        self.userId= userId
        self.color=color
    def json(self):
        return {"id":self.scheduleid,'title':self.title, 'description':self.description, 'start':self.start,'userId':self.userId,"color":self.color}

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_to_db(self):
        db.session.delete(self)
        db.session.commit()
    

   
   
    @classmethod
    def find_by_id(cls,scheduleid):
        return cls.query.filter_by(scheduleid=scheduleid).first()
        # return cls.query.all()