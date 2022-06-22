from flask import Blueprint
from flask import render_template, redirect, url_for, flash, request
from backend import  db, bcrypt
from backend.dashboard.forms import uploadfile
from backend.models import User
from flask_login import current_user, login_required
from wtforms import ValidationError
from backend.dashboard.utils import show_data



dashboards = Blueprint('dashboards', __name__)



@dashboards.route('/dashboard', methods=['POST','GET'])
@login_required
def dashboard():
    form = uploadfile()
    if form.validate_on_submit():
        file =  request.files['data']
        user = User.query.filter_by(username=current_user.username).first()
        user.file = file.read()
        db.session.commit()
        return redirect(url_for('dashboards.dashboard'))
    else:
        dats = User.query.filter_by(username=current_user.username).first().file
        if dats:
            mydata = show_data(dats)
            if request.method == 'POST':
                user_input = request.form
                print(user_input)
                if user_input['input_value'] == 'show_data_shape':
                    output = show_data.df.shape
                return render_template('dashboard/dashboard.html', form=form,headings=mydata[0], data=mydata[1], output= output)
            return render_template('dashboard/dashboard.html', form=form,  headings=mydata[0], data=mydata[1])
    return render_template('dashboard/dashboard.html', form=form)
    


@dashboards.route('/machine_learning')
@login_required
def ml():
    return render_template('dashboard/machine_learning.html')

@dashboards.route('/AboutUs')
@login_required
def about():
    return render_template('dashboard/aboutus.html')

