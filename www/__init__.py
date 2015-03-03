from flask import Flask, request, session, g
from flask.ext.bcrypt import Bcrypt
from flask.ext.seasurf import SeaSurf
from flask.ext.login import LoginManager




app = Flask(__name__)
app.config.from_object('settings')

login_manager = LoginManager()
login_manager.init_app(app)

bcrypt = Bcrypt(app)
csrf = SeaSurf(app)


from views import app_views
app.register_blueprint(app_views)