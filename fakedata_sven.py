# Create fake data into the sqlite database

from models import db,Users,Weight,Date
from datetime import date,datetime,timedelta

# Create a user
sven = Users('Sven')

# Add users to the database
db.session.add_all([sven])
db.session.commit()

# Verify
print("Verify insert")
print(Users.query.all())

sven = Users.query.filter_by(name='Sven').first()
print("Get user from database")
print(sven)

# Create weight
#weight = Weight('111',sven.id)
#db.session.add(weight)
#db.session.commit()

# Create date object
#date = Date(datetime(2019,1,17),sven.id,weight.id)

#db.session.add(date)
#db.session.commit()

i = 0
testvikt = 100
d = datetime(2020,1,1)
while i < 10:
    
    weight = Weight(testvikt,sven.id)

    db.session.add(weight)
    db.session.commit()

    date = Date(d,sven.id,weight.id)
    db.session.add(date)
    db.session.commit()

    testvikt = testvikt + 5
    d = d + timedelta(7)
    i = i + 1



# Verify Sven after the changes
print("Verify weight and date change to Sven")
sven = Users.query.filter_by(name='Sven').first()
print(sven)

print("nu fan")

sven.report_weights()