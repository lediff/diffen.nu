from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField,validators, IntegerField,DateField,FloatField,DecimalField
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


class UpdateUserForm(FlaskForm):
    email = StringField('E-post:',validators=[InputRequired("Du måste ange e-post adress"),Email()])
    name = StringField('Namn:',validators=[InputRequired()])
    submit = SubmitField('Uppdatera')

    def check_email(self, field):
    # Check if not None for that user email!
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Your email has been registered already!')

class WeightTrackerForm(FlaskForm):
    kilo = DecimalField('Vikt: ',validators=[validators.DataRequired()])
    date = DateField('Datum för vägning: ',validators=[validators.DataRequired()])
    submit = SubmitField('Registrera vikt')