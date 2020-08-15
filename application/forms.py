from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,SubmitField,PasswordField
from wtforms.validators import DataRequired,Email,EqualTo
from wtforms import ValidationError

class RegistrationForm(FlaskForm):
    email = StringField('E-post: ',validators=[DataRequired(),Email()])
    name = StringField('Namn: ',validators=[DataRequired()])
    password = PasswordField('Lösenord: ',validators=[DataRequired(),EqualTo('pass_confirm',message='Password must match!')])
    pass_confirm = PasswordField('Verifiering av lösenord: ',validators=[DataRequired()])
    submit = SubmitField('Registrera')

    def check_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidatornError('Email address already exists!')
    
    def check_username(self,field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already exists')


class LoginForm(FlaskForm):
    email = StringField('E-post: ',validators=[DataRequired(),Email()])
    name = StringField('Namn:',validators=[DataRequired()])
    password = PasswordField('Lösenord: ',validators=[DataRequired()])
    submit = SubmitField('Logga in')
