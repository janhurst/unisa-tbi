import flask
import pickle
import pandas as pd
import numpy as np
import sys
import matplotlib.pyplot as plt

sys.path.append('Python/')
import TranformInputData
import crudDB

# Use pickle to load in the pre-trained model
with open(f'model/sklearn.model.pkl', 'rb') as f:
    clf = pickle.load(f)
    selection_model = clf
    selected_feature = clf.features

# Initialise the Flask app
app = flask.Flask(__name__, template_folder='templates', static_folder='static')

# Set up the main route
@app.route('/', methods=['GET', 'POST'])
def main():
    if flask.request.method == 'GET':
        # Just render the initial form, to get input
        return (flask.render_template('main.html'))

    if flask.request.method == 'POST':
        #print(flask.request.form)
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
                                     result=result
                                     )


@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    return flask.render_template('dashboard.html')

@app.route('/records', methods=['GET'], defaults={"page_num": 1}) 
@app.route('/records/<int:page_num>', methods=['GET'])
def recordPage(page_num):
    page = crudDB.totalPages()
    patients =  crudDB.patientdBypage(page_num)
    return flask.render_template("records.html", page_num=page_num, Patients=patients, page=page)

@app.route("/records/<int:id>/edit/", methods = ['GET', 'POST'])
def editRecord(id):
    if flask.request.method == 'GET':
        patient = crudDB.getPatientById(int(id))
        return flask.render_template('editRecord.html', id=id, Prediction=patient.Prediction)

    if flask.request.method == 'POST':
        crudDB.editPatient(flask.request.form.to_dict(), int(id))
        page = crudDB.totalPages()
        patients =  crudDB.patientdBypage(1)
        return flask.render_template("records.html", Patients=patients, page=page, page_num=1)


@app.route("/records/<int:id>/delete/", methods = ['GET', 'POST'])
def deleteRecord(id):
    crudDB.deletePatient(int(id))
    page = crudDB.totalPages()
    patients =  crudDB.patientdBypage(1)
    return flask.render_template("records.html", Patients=patients, page=page, page_num=1)