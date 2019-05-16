from flask import *


#initial setup of flask.
app = Flask(__name__)

@app.route("/")
def index():
    return "SIMPLE TEST"

