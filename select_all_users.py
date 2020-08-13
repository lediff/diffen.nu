# Grab all users from the user table

from models import db,Users

print(Users.query.all())