from application import app, db
from flask import render_template, redirect, request, url_for, flash, abort
from flask_login import login_user, login_required, logout_user, current_user
from application.models import User,Weight
from application.forms import LoginForm, RegistrationForm,WeightTrackerForm,UpdateUserForm
from operator import attrgetter

# logger.basicConfig(level="DEBUG")

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/discord')
def discord():
    return render_template('discord.html')


@app.route('/weight_tracker', methods=['GET', 'POST'])
def weight_tracker():
    weights = Weight.query.filter_by(fk_user_id=current_user.id).order_by(Weight.date.asc())

    return render_template('weight_tracker.html',weights=weights)

@app.route('/weight_tracker_register' , methods=['GET', 'POST'])
def weight_tracker_register():
    form = WeightTrackerForm()

    if form.validate_on_submit():
        weight = Weight(kilo=form.kilo.data,date=form.date.data,fk_user_id=current_user.id)
     
        db.session.add(weight)
        db.session.commit()
        
        return redirect(url_for('weight_tracker'))

    return render_template('weight_tracker_register.html',form=form)


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

            if next ==None or not next[0]=='/':
                next = url_for('index')

            return redirect(next)            

        return redirect(url_for('index'))
   

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


@app.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    
    user = User.query.filter_by(id=current_user.id).first_or_404()
    bmi_length = (user.length / 100) * (user.length / 100)
 
    if request.method == 'POST':
        weights = Weight.query.filter_by(fk_user_id=current_user.id).all()

        for gunnar in weights:
            
            bmi = gunnar.kilo / bmi_length
            bmi = round(bmi, 1)

            gunnar.bmi = bmi
            db.session.commit()
            print(f"bmi {bmi}")


    return render_template('profile.html',user=user)

@app.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():

    form = UpdateUserForm()

    if form.validate_on_submit():
        current_user.email = form.email.data
        current_user.name = form.name.data
        current_user.length = form.length.data
        db.session.commit()
        flash("cool shit")

        db.session.commit()

        return redirect(url_for('profile'))

    elif request.method == 'GET':
        form.name.data = current_user.name
        form.email.data = current_user.email
        form.length.data = current_user.length

    return render_template('edit_profile.html',form=form)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

