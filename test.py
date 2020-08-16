from application.models import User

sune = User.query.filter_by(email='diffen@me2.com').first()

print(sune)