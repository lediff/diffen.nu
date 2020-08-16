from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField,validators
from wtforms.validators import Email,EqualTo,InputRequired,ValidationError,DataRequired
from application.models import User

class RegistrationForm(FlaskForm):
    email = StringField('E-post:',validators=[InputRequired("Du måste ange e-post adress"),Email()])
    name = StringField('Namn:',validators=[InputRequired()])
    password = PasswordField('Lösenord:',validators=[InputRequired(),EqualTo('pass_confirm',message='Password must match!')])
    pass_confirm = PasswordField('Verifiering av lösenord:',validators=[InputRequired()])
    submit = SubmitField('Registrera')

    def check_email(self,field):
        if User.query.filter_by(email=field).first():
            return "1"
        else:
            return "0"
            #raise ValidationError('Email address already exists!')


class LoginForm(FlaskForm):
    email = StringField('E-post: ',validators=[validators.DataRequired(), 
             validators.Email()])
    password = PasswordField('Lösenord: ',validators=[InputRequired("Du måste ange ett lösenord")])
    submit = SubmitField('Logga in')
