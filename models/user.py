import sqlite3
from db import db

class UserModel(db.Model):
    __tablename__ ='users'

    id=db.Column(db.Integer,primary_key=True)
    userId = db.Column(db.String(80),unique=True,nullable=False)
    name=db.Column(db.String(80))
    password =db.Column(db.String(80),nullable=False)
    # schedules =db.relationship("ScheduleModel",backref="writer")

    def __init__(self,userId,name,password):
        self.userId = userId
        self.name = name
        self.password = password
        

    def json(self):
        return {'userId':self.userId, 'name':self.name, 'password':self.password}

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
    def find_by_userId(cls,userId):
        return cls.query.filter_by(userId=userId).first()

    @classmethod
    def find_by_id(cls,_id):
        return cls.query.filter_by(id=_id).first()