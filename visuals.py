#Save images to the below folder
#os.getcwd() + os.sep + 'static' + os.sep + 'dashboards'

import pandas as pd
TBI = pd.read_csv('TBIPUD.csv')
for col in list(TBI):
        TBI[col] = TBI[col].astype(float).astype('Int64')
        if col not in ['AgeinYears', 'AgeInMonth']:
            TBI[col] = TBI[col].astype('category')
# Create list comprehension of the columns you want to lose
column_names = TBI.columns
columns_to_drop = [column_names[i] for i in [0, 101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118]]
# Drop unwanted columns
TBI = TBI.drop(columns_to_drop, inplace=False, axis=1)

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
TBI['EmplType'].cat.categories= TBI_EmplType
TBI['Certification'].cat.categories= TBI_CertType
TBI['InjuryMech'].cat.categories= TBI_InjMech
TBI['High_impact_InjSev'].cat.categories= TBI_InjSev
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
TBI['GCSGroup'].cat.categories= TBI_GCSGroup
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
TBI['CTForm1'].cat.categories= TBI_YesNo
TBI['IndAge'].cat.categories= TBI_YesNoNA
TBI['IndAmnesia'].cat.categories= TBI_YesNoNA
TBI['IndAMS'].cat.categories= TBI_YesNoNA
TBI['IndClinSFx'].cat.categories= TBI_YesNoNA
TBI['IndHA'].cat.categories= TBI_YesNoNA
TBI['IndHema'].cat.categories= TBI_YesNoNA
TBI['IndLOC'].cat.categories= TBI_YesNoNA
TBI['IndMech'].cat.categories= TBI_YesNoNA
TBI['IndNeuroD'].cat.categories= TBI_YesNoNA
TBI['IndRqstMD'].cat.categories= TBI_YesNoNA
TBI['IndRqstParent'].cat.categories= TBI_YesNoNA
TBI['IndRqstTrauma'].cat.categories= TBI_YesNoNA
TBI['IndSeiz'].cat.categories= TBI_YesNoNA
TBI['IndVomit'].cat.categories= TBI_YesNoNA
TBI['IndXraySFx'].cat.categories= TBI_YesNoNA
TBI['IndOth'].cat.categories= TBI_YesNoNA
TBI['CTSed'].cat.categories= TBI_YesNoNA
TBI['CTSedAgitate'].cat.categories= TBI_YesNoNA
TBI['CTSedAge'].cat.categories= TBI_YesNoNA
TBI['CTSedRqst'].cat.categories= TBI_YesNoNA
TBI['CTSedOth'].cat.categories= TBI_YesNoNA
#TBI['AgeInMonth'].cat.categories= ##########################
#TBI['AgeinYears'].cat.categories=###########################
TBI['AgeTwoPlus'].cat.categories= TBI_AgeTwo
TBI['Gender'].cat.categories= TBI_Gender
TBI['Ethnicity'].cat.categories= TBI_Ethn
TBI['Race'].cat.categories= TBI_Race
TBI['Observed'].cat.categories= TBI_YesNo
TBI['EDDisposition'].cat.categories= TBI_Disp
TBI['CTDone'].cat.categories= TBI_YesNo
TBI['EDCT'].cat.categories= TBI_YesNoNA
TBI['PosCT'].cat.categories= TBI_YesNoNA
TBI['DeathTBI'].cat.categories= TBI_YesNo
TBI['HospHead'].cat.categories= TBI_YesNo
TBI['HospHeadPosCT'].cat.categories= TBI_YesNo
TBI['Intub24Head'].cat.categories= TBI_YesNo
TBI['Neurosurgery'].cat.categories= TBI_YesNo
TBI['PosIntFinal'].cat.categories= TBI_YesNo

#Age distribution
ax = TBI.groupby(['AgeinYears'])['PosIntFinal'].count().plot.bar(figsize=(16,6))
_ = ax.set_xlabel('Age in years')
_ = ax.set_ylabel('Frequency')

from matplotlib import pyplot as plt
plt.savefig('age.png')

#Distribution of Sex

ax = TBI.groupby(['Gender','PosIntFinal'])['PosIntFinal'].count().plot.bar(figsize=(16,6))
_ = ax.set_xlabel('Sex')
_ = ax.set_ylabel('Frequency')
plt.savefig('gender.png')


#Distribution of Race

ax = TBI.groupby(['Race'])['PosIntFinal'].count().plot.bar(title="Distribution of Race", figsize=(16,6))
_ = ax.set_xlabel('Race')
_ = ax.set_ylabel('Frequency')
plt.savefig('race.png')


#Distribution of ethnicity

ax = TBI.groupby(['Ethnicity'])['PosIntFinal'].count().plot.bar(title="Distribution of Ethnicity", figsize=(16,6))
_ = ax.set_xlabel('Age')
_ = ax.set_ylabel('Frequency')
plt.savefig('ethnicity.png')

# cleaned PECARN data have to pass


