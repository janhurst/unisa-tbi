#!/usr/bin/env python
# coding: utf-8
import flask
import pandas as pd
import numpy as np
from flask_sqlalchemy import SQLAlchemy
from createDB import Patient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
#from sqlalchemy_paginator import Paginator


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

def patientdBypage(page_num):
   P = Patient.query.paginate(per_page=2,page=page_num)
   return P.items

def totalPages():
   P = Patient.query.paginate(per_page=2,page=1)
   Page = P.iter_pages()
   return Page

def newPatient(request,pred):
    patient = {}
    patient = Patient(
                  InjuryMech = request.get("InjuryMech",None),
                  Amnesia_verb = request.get("Amnesia_verb",None),
                  LOCSeparate = request.get("LOCSeparate",None),
                  LocLen = request.get("LocLen",None),
                  Seiz = request.get("Seiz",None),
                  SeizOccur = request.get("SeizOccur",None),
                  SeizLen = request.get("SeizLen",None),
                  ActNorm = request.get("ActNorm",None),
                  HA_verb = request.get("HA_verb",None),
                  HASeverity = request.get("HASeverity",None),
                  HAStart = request.get("HAStart",None),
                  Vomit = request.get("Vomit",None),
                  VomitNbr = request.get("VomitNbr",None),
                  VomitStart = request.get("VomitStart",None),
                  VomitLast = request.get("VomitLast",None),
                  Dizzy = request.get("Dizzy",None),
                  Intubated = request.get("Intubated",None),
                  Paralyzed = request.get("Paralyzed",None),
                  Sedated = request.get("Sedated",None),
                  GCSEye = request.get("GCSEye",None),
                  GCSVerbal = request.get("GCSVerbal",None),
                  GCSMotor = request.get("GCSMotor",None),
                  GCSTotal = request.get("GCSTotal",None),
                  AMS = request.get("AMS",None),
                  AMSAgitated = request.get("AMSAgitated",None),
                  AMSSleep = request.get("AMSSleep",None),
                  AMSSlow = request.get("AMSSlow",None),
                  AMSRepeat = request.get("AMSRepeat",None),
                  AMSOth = request.get("AMSOth",None),
                  SFxPalp = request.get("SFxPalp",None),
                  SFxPalpDepress = request.get("SFxPalpDepress",None),
                  FontBulg = request.get("FontBulg",None),
                  SFxBas = request.get("SFxBas",None),
                  SFxBasHem = request.get("SFxBasHem",None),
                  SFxBasOto = request.get("SFxBasOto",None),
                  SFxBasPer = request.get("SFxBasPer",None),
                  SFxBasRet = request.get("SFxBasRet",None),
                  SFxBasRhi = request.get("SFxBasRhi",None),
                  Hema = request.get("Hema",None),
                  HemaLoc = request.get("HemaLoc",None),
                  HemaSize = request.get("HemaSize",None),
                  Clav = request.get("Clav",None),
                  ClavFace = request.get("ClavFace",None),
                  ClavNeck = request.get("ClavNeck",None),
                  ClavFro = request.get("ClavFro",None),
                  ClavOcc = request.get("ClavOcc",None),
                  ClavPar = request.get("ClavPar",None),
                  ClavTem = request.get("ClavTem",None),
                  NeuroD = request.get("NeuroD",None),
                  NeuroDMotor = request.get("NeuroDMotor",None),
                  NeuroDSensory = request.get("NeuroDSensory",None),
                  NeuroDCranial = request.get("NeuroDCranial",None),
                  NeuroDReflex = request.get("NeuroDReflex",None),
                  NeuroDOth = request.get("NeuroDOth",None),
                  OSI = request.get("OSI",None),
                  OSIExtremity = request.get("OSIExtremity",None),
                  OSICut = request.get("OSICut",None),
                  OSICspine = request.get("OSICspine",None),
                  OSIFlank = request.get("OSIFlank",None),
                  OSIAbdomen = request.get("OSIAbdomen",None),
                  OSIPelvis = request.get("OSIPelvis",None),
                  OSIOth = request.get("OSIOth",None),
                  Drugs = request.get("Drugs",None),
                  AgeInMonth = request.get("AgeInMonth",None),
                  Gender = request.get("Gender",None),
                  Ethnicity = request.get("Ethnicity",None),
                  Race = request.get("Race",None),
                  Prediction=pred,
                  Evaluation=None,
                  Feedback=None)
    session.add(patient)
    session.commit()
    print("Patient added")
    return patient

def editPatient(request,patientId):
   editPatient = session.query(Patient).filter_by(id=patientId).one()
   editPatient.Feedback = request['Feedback']
   editPatient.Evaluation = request['Evaluation']
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
    return patient

