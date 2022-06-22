from flask import render_template, redirect, url_for, flash, request
from werkzeug.datastructures import Headers
from backend import app, db, bcrypt
from backend.forms import RegistrationForm, LoginForm, uploadfile
from backend.models import User
from flask_login import login_user, current_user, logout_user, login_required
from backend.loaddata import mydata




@app.route('/')
def index():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    return render_template('index.html')

@app.route('/signup', methods=['POST', 'GET'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.email.data}, Now you can login with your account details', 'success')
        return redirect(url_for('login'))
    return render_template('auth/signup.html', form=form)



@app.route('/login', methods=['POST', 'GET'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('dashboard'))
        else:
            flash(f'Login denied, Incorrect email or password!', 'danger')
    return render_template('auth/login.html', form=form)

    

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))




@app.route('/dashboard', methods=['POST','GET'])
@login_required
def dashboard():
    form = uploadfile()
    if form.validate_on_submit():
        file =  request.files['data']
        user = User.query.filter_by(username=current_user.username).first()
        user.file = file.read()
        db.session.commit()
        return redirect(url_for('dashboard'))
    else:
        dats = User.query.filter_by(username=current_user.username).first().file
        if dats:
            mydata(dats)
            return render_template('dashboard/dashboard.html', form=form,  headings=mydata.headers, data=mydata.data)

    return render_template('dashboard/dashboard.html', form=form)
    


@app.route('/machine_learning')
@login_required
def ml():
    return render_template('dashboard/machine_learning.html')

@app.route('/AboutUs')
@login_required
def about():
    return render_template('dashboard/aboutus.html')

