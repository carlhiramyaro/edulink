from . import db
from flask_login import UserMixin


"""Defines Database User objects"""
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique = True)
    password = db.Column(db.String(150))
    name = db.Column(db.String(150))
    age = db.Column(db.INT())
