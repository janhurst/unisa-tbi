import flask
import pandas as pd
import numpy as np
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialise the Flask app
app = flask.Flask(__name__, template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////sapathology.db'
db = SQLAlchemy(app)

class Patient(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    gcs = db.Column(db.Integer, nullable = True)
    ams = db.Column(db.Integer, nullable = True, default = 0)
    amsSleep = db.Column(db.Integer, nullable= True, default = 0)
    amsRepeat = db.Column(db.Integer, nullable=True, default = 0)
    amsOth = db.Column(db.Integer, nullable=True, default = 0)
    locSeparate = db.Column(db.Integer, nullable=True, default = 0)
    sfxBasOto = db.Column(db.Integer, nullable=True, default = 0)
    sfxPalp = db.Column(db.Integer, nullable=True, default = 0)
    highImpactInjSev = db.Column(db.Integer, nullable=True, default = 0)
    osiCspine = db.Column(db.Integer, nullable=True, default = 0)
    neuroD = db.Column(db.Integer, nullable=True, default = 0)
    clavFace = db.Column(db.Integer, nullable=True, default = 0)
    sfxBasRhi = db.Column(db.Integer, nullable=True, default = 0)
    hemaSize = db.Column(db.Integer, nullable=True, default = 0)
    hemaLoc = db.Column(db.Integer, nullable=True, default = 0)
    sfxBasHem = db.Column(db.Integer, nullable=True, default = 0)
    osiExtremity = db.Column(db.Integer, nullable=True, default = 0)
    actNorm = db.Column(db.Integer, nullable=True, default = 0)
    prediction = db.Column(db.Integer, nullable=True, default=0)
    evolution = db.Column(db.Integer, nullable=True, default=None)
    feedback = db.Column(db.String(500), nullable=True, default=None)
    dateSubmited = db.Column(db.DateTime, nullable = True, default = datetime.utcnow())
    def __repr__(self):
        return f"Patient('{self.gcs}','{self.dateSubmited}')"



