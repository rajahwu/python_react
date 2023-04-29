from flask import Flask

app = Flask(__name__)


@app.route("/data")
def index():
    return { "main": "flask-app" }
