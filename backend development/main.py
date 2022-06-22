from flask import Flask, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from form import RegistrationForm, LoginForm


app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

from models import User




@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup', methods=['POST', 'GET'])
def signup():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.email.data}!, Now you can login with your account details', 'success')
        return redirect(url_for('signup'))
    return render_template('auth/signup.html', form=form)



@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'fareed@gmail.com' and form.password.data == '12345':
            flash(f'Succesfull log In!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash(f'Login denied, Incorrect email or password!', 'danger')
    return render_template('auth/login.html', form=form)

@app.route('/')
def logout():
    return render_template('index.html')




@app.route('/dashboard')
def dashboard():
    return render_template('dashboard/dashboard.html')

@app.route('/machine_learning')
def ml():
    return render_template('dashboard/machine_learning.html')

@app.route('/AboutUs')
def about():
    return render_template('dashboard/aboutus.html')



if __name__ == '__main__':
    app.run(debug=True)