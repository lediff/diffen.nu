# Grab all weights from the user table

from models import db,Weight

print(Weight.query.all())