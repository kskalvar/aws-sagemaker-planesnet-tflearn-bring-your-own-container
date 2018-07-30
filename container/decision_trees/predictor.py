
# This is the file that implements a flask server to do inferences. It's the file that you will modify to
# implement the scoring for your own algorithm.

# ksk this is the original script called by AWS SageMaker

from __future__ import print_function

import flask
import time
import datetime

import sys
import os
import numpy as np
from PIL import Image
from scipy import ndimage
from model import model as tfmodel

import hickle

prefix = '/opt/ml/'
model_path = os.path.join(prefix, 'model')
tfmodel.load('/opt/ml/model/model.tfl')

chip = None
data = None

# A singleton for holding the model. This simply loads the model and holds it.
# It has a predict function that does a prediction based on the model and the input data.

class ScoringService(object):
    model = None            # Where we keep the model when it's loaded
    prediction = None

    @classmethod
    def get_model(cls):
        
        print('ScoringService::get_model')
        """Get the model object for this instance, loading it if it's not already loaded."""
        if cls.model == None:
           cls.model = tfmodel

        return cls.model
       
    @classmethod
    def predict(cls, chip):
 
        print('ScoringService::predict')
        clf = cls.get_model()
        cls.prediction = clf.predict_label([chip / 255.])[0][0]
           
        string = "{}".format(cls.prediction)
        return string
           
# The flask app for serving predictions
app = flask.Flask(__name__)

@app.route('/ping', methods=['GET'])
def ping():
    
    print('predictor::ping')
        
    """Determine if the container is working and healthy. In this sample container, we declare
    it healthy if we can load the model successfully."""
    health = ScoringService.get_model() is not None  # You can insert a health check here

    status = 200 if health else 404
    return flask.Response(response='model status %s' % status, status=status, mimetype='text/plain')

@app.route('/invocations', methods=['POST'])
def transformation():
    
    
    print('predictor::transformation')
    
    now = datetime.datetime.now()
    filename = '/tmp/flask-stream-tflearn-%s' % now.isoformat()
    
    with open(filename, "w") as f:
        chunk = flask.request.stream.read()
        f.write(chunk)
        f.close()
    
    chip = hickle.load(filename)
    prediction = ScoringService.predict(chip)
    result = 'transformation prediction: %s' % prediction
    
    if os.path.exists(filename):
       os.remove(filename)

    return flask.Response(response=result, status=200, mimetype='text/plain')
