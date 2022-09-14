import sqlite3
from db import db
from models.user import UserModel

class ScheduleModel(db.Model):
    __tablename__ ='schedule'

    id=db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(256),index=True,nullable=False)
    description=db.Column(db.Text,nullable=False)
    start =db.Column(db.String(80),nullable=False)
    end =db.Column(db.String(80),nullable=False)
    userId =db.Column(db.Integer, db.ForeignKey("users.id"),nullable=False)

    def __init__(self,title,description,start,end):
        self.title = title
        self.description = description
        self.start = start
        self.end = end

    def json(self):
        return {'title':self.title, 'description':self.description, 'start':self.start,'end':self.end}

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_to_db(self):
        db.session.delete(self)
        db.session.commit()
    

    @classmethod
    def find_by_name(cls,name):
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_by_id(cls,_id):
        return cls.query.filter_by(id=_id).first()