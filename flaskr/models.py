#from sqlalchemy import text,column,String,Integer
#from flask import current_app as app

from enum import unique
from . import db,event,logging

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(200),unique=True)
    password = db.Column(db.String(200),unique=True)
    firstname = db.Column(db.String(200))
    lastname = db.Column(db.String(200))

@event.listens_for(User, 'before_insert')
def validate_before_insert(mapper,connect,target):
    if not target.firstname:
        raise AssertionError("firstname required")
    if not target.lastname:
        raise AssertionError("lastname required")
    if not target.username:
        raise AssertionError("username required")
    if not target.password:
        raise AssertionError("password required")
    
        
