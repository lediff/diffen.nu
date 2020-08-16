from application import app, db
from flask import render_template, redirect, request, url_for, flash, abort
from flask_login import login_user, login_required, logout_user
from application.models import User
from application.forms import LoginForm, RegistrationForm


# logger.basicConfig(level="DEBUG")


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/discord')
def discord():
    return render_template('discord.html')


@app.route('/weight_tracker')
def weight_tracker():
    return render_template('weight_tracker.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("You are now logged out!")
    return redirect(url_for('index'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if user and user.check_password(form.password.data):
            login_user(user)

            flash('Logged in successfully!')

            next = request.args.get('next')

            if next == None or not next[0] == '/':
                next = url_for('profile')

            return redirect(next)
   

    return render_template('login.html', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        user = User(email=form.email.data,
                    name=form.name.data,
                    password=form.password.data)

        some_shitty_test = form.check_email(form.email.data)
        if some_shitty_test == "1":
            exit
        else:
            db.session.add(user)
            db.session.commit()
            flash("You have successfully registered!")

            return redirect(url_for('login'))

        


    return render_template('register.html', form=form)


@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
