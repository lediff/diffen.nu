# Create fake data into the sqlite database

from models import db,Users,Weight,Date
from datetime import datetime

# Create two Users
gunnar = Date(datetime(2020,1,1),'1')
sven = Date(datetime(2020,1,1),'2')

# Add users to the database
db.session.add_all([gunnar,sven])
db.session.commit()