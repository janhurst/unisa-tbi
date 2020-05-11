import flask
import pandas as pd
import numpy as np
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialise the Flask app
app = flask.Flask(__name__, template_folder='templates')
# Developement version
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////sapathology.db'
# Production Version
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:////sapathology.db'
db = SQLAlchemy(app)

class Patient(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    InjuryMech = db.Column(db.Integer, nullable=True, default=0)
    Amnesia_verb = db.Column(db.Integer, nullable=True, default=0)
    LOCSeparate = db.Column(db.Integer, nullable=True, default=0)
    LocLen = db.Column(db.Integer, nullable=True, default=0)
    Seiz = db.Column(db.Integer, nullable=True, default=0)
    SeizOccur = db.Column(db.Integer, nullable=True, default=0)
    SeizLen = db.Column(db.Integer, nullable=True, default=0)
    ActNorm = db.Column(db.Integer, nullable=True, default=0)
    HA_verb = db.Column(db.Integer, nullable=True, default=0)
    HASeverity = db.Column(db.Integer, nullable=True, default=0)
    HAStart = db.Column(db.Integer, nullable=True, default=0)
    Vomit = db.Column(db.Integer, nullable=True, default=0)
    VomitNbr = db.Column(db.Integer, nullable=True, default=0)
    VomitStart = db.Column(db.Integer, nullable=True, default=0)
    VomitLast = db.Column(db.Integer, nullable=True, default=0)
    Dizzy = db.Column(db.Integer, nullable=True, default=0)
    Intubated = db.Column(db.Integer, nullable=True, default=0)
    Paralyzed = db.Column(db.Integer, nullable=True, default=0)
    Sedated = db.Column(db.Integer, nullable=True, default=0)
    GCSEye = db.Column(db.Integer, nullable=True, default=0)
    GCSVerbal = db.Column(db.Integer, nullable=True, default=0)
    GCSMotor = db.Column(db.Integer, nullable=True, default=0)
    GCSTotal = db.Column(db.Integer, nullable=True, default=0)
    AMS = db.Column(db.Integer, nullable=True, default=0)
    AMSAgitated = db.Column(db.Integer, nullable=True, default=0)
    AMSSleep = db.Column(db.Integer, nullable=True, default=0)
    AMSSlow = db.Column(db.Integer, nullable=True, default=0)
    AMSRepeat = db.Column(db.Integer, nullable=True, default=0)
    AMSOth = db.Column(db.Integer, nullable=True, default=0)
    SFxPalp = db.Column(db.Integer, nullable=True, default=0)
    SFxPalpDepress = db.Column(db.Integer, nullable=True, default=0)
    FontBulg = db.Column(db.Integer, nullable=True, default=0)
    SFxBas = db.Column(db.Integer, nullable=True, default=0)
    SFxBasHem = db.Column(db.Integer, nullable=True, default=0)
    SFxBasOto = db.Column(db.Integer, nullable=True, default=0)
    SFxBasPer = db.Column(db.Integer, nullable=True, default=0)
    SFxBasRet = db.Column(db.Integer, nullable=True, default=0)
    SFxBasRhi = db.Column(db.Integer, nullable=True, default=0)
    Hema = db.Column(db.Integer, nullable=True, default=0)
    HemaLoc = db.Column(db.Integer, nullable=True, default=0)
    HemaSize = db.Column(db.Integer, nullable=True, default=0)
    Clav = db.Column(db.Integer, nullable=True, default=0)
    ClavFace = db.Column(db.Integer, nullable=True, default=0)
    ClavNeck = db.Column(db.Integer, nullable=True, default=0)
    ClavFro = db.Column(db.Integer, nullable=True, default=0)
    ClavOcc = db.Column(db.Integer, nullable=True, default=0)
    ClavPar = db.Column(db.Integer, nullable=True, default=0)
    ClavTem = db.Column(db.Integer, nullable=True, default=0)
    NeuroD = db.Column(db.Integer, nullable=True, default=0)
    NeuroDMotor = db.Column(db.Integer, nullable=True, default=0)
    NeuroDSensory = db.Column(db.Integer, nullable=True, default=0)
    NeuroDCranial = db.Column(db.Integer, nullable=True, default=0)
    NeuroDReflex = db.Column(db.Integer, nullable=True, default=0)
    NeuroDOth = db.Column(db.Integer, nullable=True, default=0)
    OSI = db.Column(db.Integer, nullable=True, default=0)
    OSIExtremity = db.Column(db.Integer, nullable=True, default=0)
    OSICut = db.Column(db.Integer, nullable=True, default=0)
    OSICspine = db.Column(db.Integer, nullable=True, default=0)
    OSIFlank = db.Column(db.Integer, nullable=True, default=0)
    OSIAbdomen = db.Column(db.Integer, nullable=True, default=0)
    OSIPelvis = db.Column(db.Integer, nullable=True, default=0)
    OSIOth = db.Column(db.Integer, nullable=True, default=0)
    Drugs = db.Column(db.Integer, nullable=True, default=0)
    AgeInMonth = db.Column(db.Integer, nullable=True, default=0)
    Gender = db.Column(db.Integer, nullable=True, default=0)
    Ethnicity = db.Column(db.Integer, nullable=True, default=0)
    Race = db.Column(db.Integer, nullable=True, default=0)
    Prediction = db.Column(db.Integer, nullable=True, default=0)
    Evaluation = db.Column(db.Integer, nullable=True, default=None)
    Feedback = db.Column(db.String(500), nullable=True, default=None)
    DateSubmited = db.Column(db.DateTime, nullable = True, default = datetime.utcnow())
    def __repr__(self):
        return f"Patient('{self.id}','{self.DateSubmited}')"



