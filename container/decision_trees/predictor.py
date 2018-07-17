# This is the file that implements a flask server to do inferences. It's the file that you will modify to
# implement the scoring for your own algorithm.

from __future__ import print_function

import flask
import time

import sys
import os
import numpy as np
from PIL import Image
from scipy import ndimage
from model import model as tfmodel

prefix = '/opt/ml/'
model_path = os.path.join(prefix, 'model')
tfmodel.load('/opt/ml/model/model.tfl')

# A singleton for holding the model. This simply loads the model and holds it.
# It has a predict function that does a prediction based on the model and the input data.

class ScoringService(object):
    model = None                # Where we keep the model when it's loaded

    @classmethod
    def get_model(cls):
        """Get the model object for this instance, loading it if it's not already loaded."""
        if cls.model == None:
           cls.model = tfmodel

        return cls.model

    @classmethod
    def predict(cls, in_fname): 
        """For the input, do the predictions and return them.

        Args:
            input (a pandas dataframe): The data on which to do the predictions. There will be
                one prediction per row in the dataframe"""

        out_fname = None  

        clf = cls.get_model()
        im = Image.open(in_fname)
        arr = np.array(im)[:,:,0:3]
        shape = arr.shape

        # Set output fname
        if not out_fname:
            out_fname = os.path.splitext(in_fname)[0] + '_detection.png'

        # Create detection variables
        detections = np.zeros((shape[0], shape[1]), dtype='uint8')
        output = np.copy(arr)

        # Sliding window parameters
        step = 2
        win = 20
    
        # Loop through pixel positions
        print('Processing...')
        for i in range(0, shape[0]-win, step):
            print('row %1.0f of %1.0f' % (i, (shape[0]-win-1)))
    
            for j in range(0, shape[1]-win, step):
    
                # Extract sub chip
                chip = arr[i:i+win,j:j+win,:]
    
                # Predict chip label
                # prediction = model.predict_label([chip / 255.])[0][0]
                prediction = clf.predict_label([chip / 255.])[0][0]
    
                # Record positive detections
                if prediction == 1:
                    detections[i+int(win/2), j+int(win/2)] = 1

        # Process detection locations
        dilation = ndimage.binary_dilation(detections, structure=np.ones((3,3)))
        labels, n_labels = ndimage.label(dilation)
        center_mass = ndimage.center_of_mass(dilation, labels, np.arange(n_labels)+1)
    
        # Loop through detection locations
        if type(center_mass) == tuple: center_mass = [center_mass]
        for i, j in center_mass:
            i = int(i - win/2)
            j = int(j - win/2)
            
            # Draw bouding boxes in output array
            output[i:i+win, j:j+2, 0:3] = [255,0,0]
            output[i:i+win, j+win-2:j+win, 0:3] = [255,0,0]
            output[i:i+2, j:j+win, 0:3] = [255,0,0]
            output[i+win-2:i+win, j:j+win, 0:3] = [255,0,0]
    
        # Save output image
        outIm = Image.fromarray(output)
        outIm.save(out_fname)

# The flask app for serving predictions
app = flask.Flask(__name__)

@app.route('/ping', methods=['GET'])
def ping():
        
    print ("ping()")

    """Determine if the container is working and healthy. In this sample container, we declare
    it healthy if we can load the model successfully."""
    health = ScoringService.get_model() is not None  # You can insert a health check here

    status = 200 if health else 404
    return flask.Response(response='\n', status=status, mimetype='application/json')

@app.route('/invocations', methods=['POST'])
def transformation():

    print ("transformation start")

    """Do an inference on a single batch of data. In this sample server, we take data as CSV, convert
    it to a pandas data frame for internal use and then convert the predictions back to CSV (which really
    just means one prediction per line, since there's a single column.
    """
    result = None

    time.sleep(30)
    with open("image.png","wb") as fo:
       fo.write(flask.request.data)

    ScoringService.predict("image.png")

    print ("transformation end")
