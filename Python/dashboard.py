import DataCleaning
import Imputation
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt 

pecarn_data = pd.read_csv('TBI PUD 10-08-2013.csv', index_col=0)
clean_data = DataCleaning.datacleaning(pecarn_data)
TBI = Imputation.impute(clean_data)

TBI.loc[TBI['AgeInMonth'] < 24, 'Age'] = '2-18 years' 
TBI.loc[TBI['AgeInMonth'] >= 24, 'Age'] = '0-2 years' 

#Codes expansion
TBI_EmplType = ['Nurse Practitioner', 'Physician Assistant', 'Resident', 'Fellow', 'Faculty']
TBI_CertType = ['Emergency Medicine', 'Pediatrics', 'Pediatrics Emergency Medicine', 'Emergency Medicine and Pediatrics', 'Other']
TBI_InjSev = ['Low', 'Moderate', 'High']
TBI_YesNoPV = ['No', 'Yes', 'Pre-verbal/Non-verbal']
TBI_InjMech = ['Occupant in motor vehicle collision (MVC)', 'Pedestrian struck by moving vehicle', 'Bike rider struck by automobile', 'Bike collision or fall from bike while riding', 'Other wheeled transport crash', 'Fall to ground from standing/walking/running', 'Walked or ran into stationary object', 'Fall from an elevation', 'Fall down stairs', 'Sports', 'Assault', 'Object struck head - accidental', 'Other mechanism']
TBI_YesNoLOC = ['No', 'Yes', 'Suspected']
TBI_LocLen = ['< 5 sec', '5 sec - < 1 min', '1 -5 min', ' > 5 min', 'Not applicable']
TBI_YesNo = ['No', 'Yes']
TBI_SeizOcc = ['Immediately on contact', 'Within 30 minutes of injury', ' > 30 minutes after injury', 'Not applicable']
TBI_SeizLen = ['< 1 min', '1 - < 5 min', '5 - 15 min', '> 15 min', 'Not applicable']
TBI_HASev = ['Mild (barely noticeable)', 'Moderate', 'Severe (intense)', 'Not applicable']
TBI_Start = ['Before head injury', 'Within 1 hr of event', '1 - 4 hrs after event', '> 4 hrs after event', 'Not applicable']
TBI_VomEpi = ['Once', 'Twice', '> 2 times', 'Not applicable']
TBI_Start = ['Before head injury', 'Within 1 hr of event', '1 - 4 hrs after event', '> 4 hrs after event', 'Not applicable']
TBI_VomLast = ['< 1 hr before ED evaluation', '1 -4 hrs before ED evaluation', '> 4 hrs before ED evaluation', 'Not applicable']
TBI_GCSEye = ['None', 'Pain', 'Verbal', 'Spontaneous']
TBI_GCSVerbal = ['None', 'Incomprehensible sounds (moans)', 'Inappropriate words (cries to pain)', 'Confused (irritable/cries)', 'Oriented (coos/babbles)']
TBI_GCSMotor = ['None', 'Abnormal extension posturing', 'Abnormal flexure posturing', 'Withdraws to pain', 'Localizes pain (withdraws to touch)', 'Follow commands (spontaneous movement)']
TBI_GCSGroup = ['3 - 13', '14 - 15']
TBI_HemLoc = ['Frontal', 'Occipital', 'Parietal/Temporal', 'Not applicable']
TBI_HemSz = ['Small (<1 cm, barely palpable)', 'Medium (1-3 cm)', 'Large (>3 cm)', 'Not applicable']
TBI_YesNoNA = ['No', 'Yes', 'Not applicable']
TBI_YesNoUnc = ['No', 'Yes', 'Unclear exam']
TBI_YesNoClo = ['No/Closed', 'Yes']
TBI_AgeTwo = ['< 2 years', '> = 2 years']
TBI_Gender = ['Male', 'Female']
TBI_Ethn = ['Hispanic', 'Non-Hispanic']
TBI_Race = ['White', 'Black', 'Asian', ' American Indian/Alaskan Native', 'Pacific Islander', 'Other']
TBI_Disp = ['Home', 'OR', 'Admit - general inpatient', 'Admit short-stay (< 24 hr)/observation unit', 'ICU', 'Transferred to another hospital', 'AMA', ' Death in ED', 'Other']


#Conversion
TBI['InjuryMech'].cat.categories= TBI_InjMech
TBI['Amnesia_verb'].cat.categories= TBI_YesNoPV
TBI['LOCSeparate'].cat.categories= TBI_YesNoLOC
TBI['LocLen'].cat.categories= TBI_LocLen
TBI['Seiz'].cat.categories= TBI_YesNo
TBI['SeizOccur'].cat.categories= TBI_SeizOcc
TBI['SeizLen'].cat.categories= TBI_SeizLen
TBI['ActNorm'].cat.categories= TBI_YesNo
TBI['HA_verb'].cat.categories= TBI_YesNoPV
TBI['HASeverity'].cat.categories= TBI_HASev
TBI['HAStart'].cat.categories= TBI_Start
TBI['Vomit'].cat.categories= TBI_YesNo
TBI['VomitNbr'].cat.categories= TBI_VomEpi
TBI['VomitStart'].cat.categories= TBI_Start
TBI['VomitLast'].cat.categories= TBI_VomLast
TBI['Dizzy'].cat.categories= TBI_YesNo
TBI['Intubated'].cat.categories= TBI_YesNo
TBI['Paralyzed'].cat.categories= TBI_YesNo
TBI['Sedated'].cat.categories= TBI_YesNo
TBI['GCSEye'].cat.categories= TBI_GCSEye
TBI['GCSVerbal'].cat.categories= TBI_GCSVerbal
TBI['GCSMotor'].cat.categories= TBI_GCSMotor
#TBI['GCSTotal'].cat.categories= ########################
TBI['AMS'].cat.categories= TBI_YesNo
TBI['AMSAgitated'].cat.categories= TBI_YesNoNA
TBI['AMSSleep'].cat.categories= TBI_YesNoNA
TBI['AMSSlow'].cat.categories= TBI_YesNoNA
TBI['AMSRepeat'].cat.categories= TBI_YesNoNA
TBI['AMSOth'].cat.categories= TBI_YesNoNA
TBI['SFxPalp'].cat.categories= TBI_YesNoUnc
TBI['SFxPalpDepress'].cat.categories= TBI_YesNoNA
TBI['FontBulg'].cat.categories= TBI_YesNoClo
TBI['SFxBas'].cat.categories= TBI_YesNo
TBI['SFxBasHem'].cat.categories= TBI_YesNoNA
TBI['SFxBasOto'].cat.categories= TBI_YesNoNA
TBI['SFxBasPer'].cat.categories= TBI_YesNoNA
TBI['SFxBasRet'].cat.categories= TBI_YesNoNA
TBI['SFxBasRhi'].cat.categories= TBI_YesNoNA
TBI['Hema'].cat.categories= TBI_YesNo
TBI['HemaLoc'].cat.categories= TBI_HemLoc
TBI['HemaSize'].cat.categories= TBI_HemSz
TBI['Clav'].cat.categories= TBI_YesNo
TBI['ClavFace'].cat.categories= TBI_YesNoNA
TBI['ClavNeck'].cat.categories= TBI_YesNoNA
TBI['ClavFro'].cat.categories= TBI_YesNoNA
TBI['ClavOcc'].cat.categories= TBI_YesNoNA
TBI['ClavPar'].cat.categories= TBI_YesNoNA
TBI['ClavTem'].cat.categories= TBI_YesNoNA
TBI['NeuroD'].cat.categories= TBI_YesNo
TBI['NeuroDMotor'].cat.categories= TBI_YesNoNA
TBI['NeuroDSensory'].cat.categories= TBI_YesNoNA
TBI['NeuroDCranial'].cat.categories= TBI_YesNoNA
TBI['NeuroDReflex'].cat.categories= TBI_YesNoNA
TBI['NeuroDOth'].cat.categories= TBI_YesNoNA
TBI['OSI'].cat.categories= TBI_YesNo
TBI['OSIExtremity'].cat.categories= TBI_YesNoNA
TBI['OSICut'].cat.categories= TBI_YesNoNA
TBI['OSICspine'].cat.categories= TBI_YesNoNA
TBI['OSIFlank'].cat.categories= TBI_YesNoNA
TBI['OSIAbdomen'].cat.categories= TBI_YesNoNA
TBI['OSIPelvis'].cat.categories= TBI_YesNoNA
TBI['OSIOth'].cat.categories= TBI_YesNoNA
TBI['Drugs'].cat.categories= TBI_YesNo
#TBI['AgeInMonth'].cat.categories= ##########################
#TBI['AgeinYears'].cat.categories=###########################
TBI['Gender'].cat.categories= TBI_Gender
TBI['Ethnicity'].cat.categories= TBI_Ethn
TBI['Race'].cat.categories= TBI_Race
TBI['PosIntFinal'].cat.categories= TBI_YesNo

feature_list = list(TBI.columns)
feature_list = [i for i in feature_list if not "PosIntFinal" in i]
feature_list = [i for i in feature_list if not "AgeInMonth" in i]
#print(feature_list)
y, hue = "proportion", "PosIntFinal"
hue_order = ["Yes", "No"]
for feature in feature_list:
    x = feature
    plt.figure()
    chart = (TBI[feature].groupby(TBI['PosIntFinal']).value_counts(normalize=True).rename(y).reset_index().pipe((sns.barplot, "data"), x=x, y=y, hue=hue))
    chart.set_xticklabels(chart.get_xticklabels(), rotation=45, horizontalalignment='right')
    plt.tight_layout()
    plt.savefig("../static/graph/"+feature+".png")
    plt.close('all')

