from flask import *

#initial setup of flask.
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    #if speech has been recieved
    if request.method == 'POST':
        #convert speech into pdf and save pdf to the server
        speech = request.form["speech"]
        return speech
    
    return render_template("index.html")

