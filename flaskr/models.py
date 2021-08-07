#from sqlalchemy import text,column,String,Integer
#from flask import current_app as app

from enum import unique
from . import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(200),unique=True)
    password = db.Column(db.String(200),unique=True)
    firstname = db.Column(db.String(200))
    lastname = db.Column(db.String(200))

    # def __init__(self,firstname,lastname,username,password):
    #     self.firstname = firstname
    #     self.lastname = lastname
    #     self.username = username
    #     self.password = password
        
