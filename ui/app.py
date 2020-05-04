import flask
import pickle
import pandas as pd
import numpy as np
import sys


sys.path.append('../Python/')
import TranformInputData
import crudDB

# Use pickle to load in the pre-trained model
with open(f'sklearn.model.pkl', 'rb') as f:
    clf = pickle.load(f)
    selection_model = clf
    selected_feature = clf.features
    xTrain = clf.xTrain
    yTrain = clf.yTrain

# Initialise the Flask app
app = flask.Flask(__name__, template_folder='templates')

# Set up the main route
@app.route('/', methods=['GET', 'POST'])
def main():
    if flask.request.method == 'GET':
        # Just render the initial form, to get input
        return (flask.render_template('main.html'))

    if flask.request.method == 'POST':
        testData = TranformInputData.transform(flask.request.form,selected_feature)
        #Get the model's prediction
        prediction = selection_model.predict(testData.to_numpy())[0]
        pred = 0
        if prediction == 1:
            result = "CT Required"
            pred = 1
        else:
            result = "CT Not Required"
        crudDB.newPatient(flask.request.form,pred)
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
    patients = crudDB.showPatients()
    return flask.render_template('records.html', Patients = patients)

@app.route("/records/<int:id>/edit/", methods = ['GET', 'POST'])
def editRecord(id):
    if flask.request.method == 'GET':
        patient = crudDB.getPatientById(int(id))
        return flask.render_template('editRecord.html', id=id, prediction=patient.prediction)

    if flask.request.method == 'POST':
        crudDB.editPatient(flask.request.form.to_dict(), int(id))
        patients = crudDB.showPatients()
        return flask.render_template('records.html', Patients=patients)


@app.route("/records/<int:id>/delete/", methods = ['GET', 'POST'])
def deleteRecord(id):
    crudDB.deletePatient(int(id))
    patients = crudDB.showPatients()
    return flask.render_template('records.html', Patients=patients)