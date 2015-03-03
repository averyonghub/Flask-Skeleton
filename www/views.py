from flask import Blueprint, render_template, abort, flash, request, redirect
from . import app
from flask.ext.login import current_user, login_required

app_views = Blueprint('app', __name__,
                        template_folder='templates')


@app_views.route('/')
def home():
	return render_template('landing.html')