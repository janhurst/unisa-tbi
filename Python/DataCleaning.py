#!/usr/bin/env python
# coding: utf-8


import pandas as pd 
import numpy as np

# Reading Data

def datacleaning(pecarn_data):
    # Data Type

    pecarn_data.dtypes
    pecarn_dataTypeFrame = pd.DataFrame(pecarn_data.dtypes)
    pecarn_dataTypeFrame.to_csv(r'datatype.csv', index=False, header=True)
    # Convert all data into INT64
    # print("Convert all data into INT64")
    pecarn_df = pd.DataFrame(pecarn_data)
    pecarn_df = pecarn_df.astype(float).astype('Int64')
    pecarn_df.dtypes

    # Counting NAN
    count_nan = pecarn_df.isnull().sum()
    count_nan.sort_values(ascending=False).head(50)


    # Droping unncessory dataset - this needs to revised
    # EMployeID, Certification not important, AgeinMonth,Vomit and GCSGroup is repeated
    Not_Imp_Data = ['EmplType',
                    'Certification',
                    'AgeinYears',
                    'AgeTwoPlus',
                    'GCSGroup',
                    'High_impact_InjSev']
    ## PosCT = finding 1 to 23, therefore findings are removed
    CT_Data = ['Observed',
               'EDDisposition',
               'CTDone',
               'EDCT',
               'PosCT',
               'Finding1',
               'Finding2',
               'Finding3',
               'Finding4',
               'Finding5',
               'Finding6',
               'Finding7',
               'Finding8',
               'Finding9',
               'Finding10',
               'Finding11',
               'Finding12',
               'Finding13',
               'Finding14',
               'Finding20',
               'Finding21',
               'Finding22',
               'Finding23',
               'CTSed',
               'CTSedAgitate',
               'CTSedAge',
               'CTSedRqst',
               'CTSedOth']
    ## Not relevant to model : If CT is being Order
    CT_Order = ['CTForm1',
                'IndAge',
                'IndAmnesia',
                'IndAMS',
                'IndClinSFx',
                'IndHA',
                'IndHema',
                'IndLOC',
                'IndMech',
                'IndNeuroD',
                'IndRqstMD',
                'IndRqstParent',
                'IndRqstTrauma',
                'IndSeiz',
                'IndVomit',
                'IndXraySFx',
                'IndOth']

    # Based on physician's evaluation
    #physician_evalution = ['CTSed',
    #                       'Sedated',
    #                       'Paralyzed',
    #                       'Intubated']
    # Based on physician's evaluation
    physician_evalution = ['CTSed']

    # POSTINFFInal is enough no need to 4 variable which derives class otherwise it would have higher correlation
    High_Correlated = ['DeathTBI',
                       'Neurosurgery',
                       'Intub24Head',
                       'HospHeadPosCT',
                       'HospHead']
    print("Data Cleaning Done")
    to_drop = Not_Imp_Data + CT_Data + CT_Order + physician_evalution + High_Correlated
    pecarn_df.drop(to_drop, inplace=True, axis=1)
    return pecarn_df

