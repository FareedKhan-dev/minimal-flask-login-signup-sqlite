from flask import Blueprint, session
from flask import render_template, redirect, url_for, flash
from backend import  db, bcrypt
from backend.users.forms import RegistrationForm, LoginForm
from backend.models import User

from flask_login import login_user, current_user, logout_user, login_required



users = Blueprint('users', __name__)



@users.route('/signup', methods=['POST', 'GET'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('dsahboards.dashboard'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.email.data}, Now you can login with your account details', 'success')
        return redirect(url_for('users.login'))
    return render_template('auth/signup.html', form=form)



@users.route('/login', methods=['POST', 'GET'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboards.dashboard'))
    
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            session.permanent = True
            return redirect(url_for('dashboards.dashboard'))
        else:
            flash(f'Login denied, Incorrect email or password!', 'danger')
    return render_template('auth/login.html', form=form)

    

@users.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))
