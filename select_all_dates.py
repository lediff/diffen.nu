# Grab all dates from the user table

from models import db,Date

print(Date.query.all())