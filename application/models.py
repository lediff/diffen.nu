from application import db,login_manager
from werkzeug.security import generate_password_hash, check_password_hash 
from flask_login import UserMixin

@login_manager.user_loader 
def load_user(user_id):
    return User.query.get(user_id)

##########d####
### Models ###
##############

class User(db.Model,UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(64))
    email = db.Column(db.String(64),unique=True,index=True)
    password_hash = db.Column(db.String(128))
    # One to many
    # name to many weights
    #weights = db.relationship('Weight',backref='users',lazy='dynamic')
    # One to one
    #date = db.relationship('Date',backref='users',uselist=False)

    def __init__(self,name,email,password):
        self.name = name
        self.email = email
        self.password_hash = generate_password_hash(password)
    
    def check_password(self,password):
        return check_password_hash(self.password_hash,password)

    def report_weights(self):
        print("Here are my weights:")
        for weight in self.weights:
            print(weight.kilo)

    def __repr__(self):
        return f"Username {self.username}"


class Weight(db.Model):
    __tablename__ = 'weight'

    id = db.Column(db.Integer,primary_key=True)
    kilo = db.Column(db.Float)
    date = db.Column(db.Date)
    fk_user_id = db.Column(db.Integer,db.ForeignKey('users.id'))

    def __init__(self,kilo,date,fk_user_id):
        self.kilo = kilo
        self.date = date
        self.fk_user_id = fk_user_id