# Create fake data into the sqlite database

from models import db,Users,Weight,Date

# Create two Users
gunnar = Users('Gunnar')
sven = Users('Sven')

# Add users to the database
db.session.add_all([gunnar,sven])
db.session.commit()