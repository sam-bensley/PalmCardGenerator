from flask import *
from generatePalmCards import *
import uuid
#initial setup of flask.
app = Flask(__name__)

randomSessionID = str(uuid.uuid4())

@app.route("/", methods=['GET', 'POST'])
def index():
    #if speech has been recieved
    if request.method == 'POST':
        #convert speech into pdf and save pdf to the server
        speech = request.form["speech"]
        convertTextToPDF(speech, randomSessionID+'.pdf')
        return send_file("speeches/"+randomSessionID+".pdf", attachment_filename='PalmCards.pdf')
    
    return render_template("index.html")
