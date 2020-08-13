import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)

##############
### Models ###
##############

class Users(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.Text)
    # One to many
    # name to many weights
    weights = db.relationship('Weight',backref='users',lazy='dynamic')
    # One to one
    date = db.relationship('Date',backref='users',uselist=False)

    def __init__(self,name):
        self.name = name
    
    def __repr__(self):
        if self.date:
            return f"Namn: {self.name} and has the weight measured on the {self.date}."
        else:
            return f"{self.name} hasn't been on the scale yet!"

    def report_weights(self):
        print("Here are my weights:")
        for weight in self.weights:
            print(weight.kilo)


class Weight(db.Model):
    __tablename__ = 'weight'

    id = db.Column(db.Integer,primary_key=True)
    kilo = db.Column(db.Integer)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))

    def __init__(self,kilo,user_id):
        self.kilo = kilo
        self.user_id = user_id

class Date(db.Model):
    __tablename__ = 'dates'

    id = db.Column(db.Integer,primary_key=True)
    date = db.Column(db.Date)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    weight_id = db.Column(db.Integer,db.ForeignKey('weight.id'))

    def __init__(self,date,user_id,weight_id):
        self.date = date
        self.user_id = user_id
        self.weight_id = weight_id