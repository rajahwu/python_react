from flask import Flask
from .config import Config
from flask_login import LoginManager
from .models import db, User

app = Flask(__name__)
app.config.from_object(Config)
login = LoginManager(app)
login.login_view = "session.login"


@app.route("/data")
def index():
    return { "main": "flask-app" }
