#!/usr/bin/env python
# coding: utf-8
import flask
import pandas as pd
import numpy as np
from flask_sqlalchemy import SQLAlchemy
from createDB import Patient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


#Connect to Database and create database session
engine = create_engine('sqlite:////sapathology.db',connect_args={'check_same_thread': False})
Patient.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# from sqlalchemy import inspect
# inspector = inspect(engine)
# for table_name in inspector.get_table_names():
#        print("Tables: %s" % table_name)
#Patient.__table__.create(bind = engine)


def showPatients():
   Patients = session.query(Patient).all()
   return Patients

def newPatient(request,pred):
    patient = {}
    patient = Patient(gcs=request.get("GCSTotal"),
                ams=request.get("AMS"),
                amsSleep=request.get("AMSSleep"),
                amsRepeat=request.get("AMSRepeat"),
                amsOth=request.get("AMSOth"),
                locSeparate=request.get("LOCSeparate"),
                sfxBasOto=request.get("SFxBasOto"),
                sfxPalp=request.get("SFxPalp"),
                highImpactInjSev=request.get("High_impact_InjSev"),
                osiCspine=request.get("OSICspine"),
                neuroD=request.get("NeuroD"),
                clavFace=request.get("ClavFace"),
                sfxBasRhi=request.get("SFxBasRhi"),
                hemaSize=request.get("HemaSize"),
                hemaLoc=request.get("HemaLoc"),
                sfxBasHem=request.get("SFxBasHem"),
                osiExtremity=request.get("OSIExtremity"),
                actNorm=request.get("ActNorm"),
                prediction=pred,
                evolution=None,
                feedback=None)
    session.add(patient)
    session.commit()
    print("Patient added")
    return patient

def editPatient(request,patientId):
   editPatient = session.query(Patient).filter_by(id=patientId).one()
   editPatient.feedback = request['feedback']
   editPatient.evolution = request['evolution']
   session.add(editPatient)
   session.commit()
   return editPatient

def deletePatient(patientId):
   patientToDelete = session.query(Patient).filter_by(id=patientId).one()
   session.delete(patientToDelete)
   session.commit()
   return id

def getPatientById(patientId):
    patient = session.query(Patient).filter_by(id=patientId).one()
    print(patient)
    return patient

