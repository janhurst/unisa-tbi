import flask
import pickle
import pandas as pd
import numpy as np
import sys
import io
from flask_sqlalchemy import SQLAlchemy
from createDB import Patient

sys.path.append('../Python/')
import DataCleaning
import Imputation
import FeatureEngineering
import TranformInputData
import Model

pecarn_data = pd.read_csv('TBI PUD 10-08-2013.csv', index_col=0)
clean_data = DataCleaning.datacleaning(pecarn_data)
imputed_data = Imputation.impute(clean_data)
binary_data = FeatureEngineering.binarized(imputed_data)
selected_feature,selection_model = Model.getModel(binary_data)

# Initialise the Flask app
app = flask.Flask(__name__, template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////sapathology.db'
db = SQLAlchemy(app)

# Set up the main route
@app.route('/', methods=['GET', 'POST'])
def main():
    if flask.request.method == 'GET':
        # Just render the initial form, to get input
        return (flask.render_template('main.html'))

    if flask.request.method == 'POST':
        # Store data into DB
        p = {}
        p = Patient(gcs=flask.request.form.get("GCSTotal"),
                          ams=flask.request.form.get("AMS"),
                          amsSleep =flask.request.form.get("AMSSleep"),
                          amsRepeat =flask.request.form.get("AMSRepeat"),
                          amsOth =flask.request.form.get("AMSOth"),
                          locSeparate =flask.request.form.get("LOCSeparate"),
                          sfxBasOto =flask.request.form.get("SFxBasOto"),
                          sfxPalp =flask.request.form.get("SFxPalp"),
                          highImpactInjSev =flask.request.form.get("High_impact_InjSev"),
                          osiCspine =flask.request.form.get("OSICspine"),
                          neuroD =flask.request.form.get("NeuroD"),
                          clavFace =flask.request.form.get("ClavFace"),
                          sfxBasRhi =flask.request.form.get("SFxBasRhi"),
                          hemaSize =flask.request.form.get("HemaSize"),
                          hemaLoc =flask.request.form.get("HemaLoc"),
                          sfxBasHem =flask.request.form.get("SFxBasHem"),
                          osiExtremity =flask.request.form.get("OSIExtremity"),
                          actNorm =flask.request.form.get("ActNorm") )
        db.session.add(p)
        db.session.commit()

        testData = TranformInputData.transform(flask.request.form,selected_feature)
        #Get the model's prediction
        prediction = selection_model.predict(testData.to_numpy())[0]
        if prediction == 1:
            result = "CT Required"
        else:
            result = "CT Not Required"

        # Render the form again, but add in the prediction and remind user
        # of the values 'BinarizedTestData'they input before
        return flask.render_template('main.html',
                                     result=result,
                                     )

# Set up the main route
@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    return flask.render_template('dashboard.html')

# Set up the main route
@app.route('/records', methods=['GET', 'POST'])
def record():
    patients = Patient.query.all()
    return flask.render_template('records.html', Patients = patients)

if __name__ == '__main__':
    app.run()
