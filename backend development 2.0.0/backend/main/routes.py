from flask import redirect, url_for, render_template, Blueprint
from flask_login import current_user

main = Blueprint('main', __name__)

@main.route('/')
def index():
    if current_user.is_authenticated:
        return redirect(url_for('dashboards.dashboard'))
    return render_template('index.html')