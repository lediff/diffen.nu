# Create fake data into the sqlite database

from models import db,Users,Weight,Date

sven = Weight('100','2')
gunnar = Weight('130','1')

# Add users to the database
db.session.add_all([sven,gunnar])
db.session.commit()