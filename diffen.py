from application import app,db
from flask import render_template,redirect,request,url_for,flash,abort
from flask_login import login_user,login_required,logout_user
from application.models import User

#logger.basicConfig(level="DEBUG")

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/discord')
def discord():
	return render_template('discord.html')

@app.route('/weight_tracker')
def weight_tracker():
	return render_template('weight_tracker.html')

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')

 