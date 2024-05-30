"""
Routes and views for the flask application.
"""



from datetime import datetime
from flask import render_template,Response, request
from carParking import app

import os
import joblib
import ssl
import imutils,time

from carParking.detection.main import Detect
from carParking.detection.main import DetectTrack

ssl._create_default_https_context = ssl._create_unverified_context
os.environ['CURL_CA_BUNDLE'] = ''


@app.route('/')
@app.route('/home')
def home():
     return render_template("index.html")

@app.route('/start_tracking', methods=['POST'])
def start_tracking():
    selected_model = request.form.get('model')
    selected_tracker = request.form.get('tracker')
    
    print(selected_model)
    print(selected_tracker)

    # Start tracking using the selected model
    # You can call your detectTrack function here with the selected model
    if(selected_tracker == "none"):
        return Response(Detect(selected_model), mimetype='multipart/x-mixed-replace; boundary=frame')
    else:
       return Response(DetectTrack(selected_model,selected_tracker), mimetype='multipart/x-mixed-replace; boundary=frame')

        


