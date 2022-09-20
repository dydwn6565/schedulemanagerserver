import sqlite3
from db import db

class MessageModel(db.Model):
    __tablename__ ='message'

    id=db.Column(db.Integer,primary_key=True)
    message = db.Column(db.String(100),unique=True,nullable=False)
    
    

    def __init__(self,message):
        self.message = message
        
        self.password = message
        

    def json(self):
        return {'message':self.message}

   