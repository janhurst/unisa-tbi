"""
This module provides a convenient method to load the PECARN Traumatic Brain Injury dataset.

To use this module, place the PECARN TBI CSV file in the current working directory.
"""
from os import environ, path, getcwd
import pandas as pd 
import pickle
import logging

logger = logging.getLogger(__name__)

# the original PECARN dataset's file name and the cached pickle filename
_TBI_CSV_FILE = 'TBI PUD 10-08-2013.csv' 
_TBI_PKL_FILE = 'PECARN_TBI.pkl'

# construct the full file names
_TBI_CSV_FILE = getcwd() + path.sep + _TBI_CSV_FILE
_TBI_PKL_FILE = getcwd() + path.sep + _TBI_PKL_FILE

def load(fromCsv: bool = False, withLabels: bool = True):
    """ Load the PECARN data from either CSV or a cache Pickle file """
    if (not fromCsv or not withLabels) and path.exists(_TBI_PKL_FILE):
        return _frompkl()
    else:
        return _fromcsv(withLabels)

def _fromcsv(withLabels):
    """ Load the PECARN TBI dataset from a CSV file if it exists """
    logger.info('Loading from CSV file ' + _TBI_CSV_FILE)
    try:
        tbi = pd.read_csv(_TBI_CSV_FILE, index_col=0, dtype='Int64')
    
        # fix the data types
        tbi = _datatypes(tbi)

        # reorder the columns alphabetically
        tbi = tbi.reindex(sorted(tbi.columns), axis=1)

        # add label categories
        if withLabels:
            tbi = _label_categories(tbi)

        # pickle the tbi data
        with open(_TBI_PKL_FILE, 'wb') as f:
            pickle.dump(tbi, f)

        return tbi
    except FileNotFoundError:
        logger.error(_TBI_CSV_FILE + ' not found')
        raise

def _frompkl():
    """ Load the PECARN TBI dataset from a Pickle file if it exists """
    logger.info('Loading from Pickle file ' + _TBI_PKL_FILE)
    with open(_TBI_PKL_FILE, 'rb') as f:
        return pickle.load(f)

_CATEGORICAL_THRESHOLD = 15

def _datatypes(tbi: pd.DataFrame):
    """ converts the Int64 data in each column to either boolean or categorical """
    for col in tbi:

        # if there are only two values (0 and 1, plus NaNs) then cast to nullable boolean type
        if tbi[col].nunique() == 2 and tbi[col].max() < 2:
            tbi[col] = tbi[col].astype('boolean')
        else:
            # categorical if there are not too many unique values
            if tbi[col].nunique() < _CATEGORICAL_THRESHOLD:            
                tbi[col] = tbi[col].astype('category')

    # fix GCSTotal, it gets mistakenly set to category with the above logic
    tbi['GCSTotal'] = tbi['GCSTotal'].astype('Int64')

    return tbi

def _label_categories(tbi):
    """ change the categorical labels to those defined in the PECARN data dictionary """
    for col, labels in _category_labels.items():
        logger.debug(f"relabelling {col}")
        tbi[col].cat.categories = labels
    return tbi

""" Category definitions """
_yesnona = ['No', 'Yes', 'NA']

_category_labels = {
    'Certification': ['Emergency Medicine', 'Pediatrics', 'Pediatrics Emergency Medicine', 'Emergency Medicine and Pediatrics', 'Other'],

    # injury type
    'High_impact_InjSev': ['Low', 'Moderate', 'High'],
    'InjuryMech': ['Occupant Vehicle', 'Pedestrian Vehicle', 'Bike Vehicle', 'Bike', 'Other Transport',
        'Fall to Ground', 'Stationary Object', 'Fall Elevation', 'Fall Stairs', 'Sports', 'Assault', 'Object Struck Head', 'Other'],

    # amnesia and loss of consciousness
    'Amnesia_verb': ['No','Yes','Pre/Non Verbal'],
    'LOCSeparate': ['No','Yes','Suspected'],
    'LocLen': ['<5sec','5sec-<1min','1-5min','>5min', 'NA'],

    # seizure
    'SeizOccur': ['Immediate','Within 30min','After 30min','NA'],
    'SeizLen': ['<1min', '1-<5min', '5-15min', '>15min','NA'],

    # headache
    'HA_verb': ['No','Yes','Non Verbal'],
    'HASeverity': ['Mild','Moderate','Severe','NA'],
    'HAStart': ['Before', 'Within 1hr', '1-4hr', '>4hrs','NA'],

    # vomit
    'VomitNbr': ['Once',' Twice', '>2 times', 'NA'],
    'VomitStart': ['Before', 'Within 1hr', '1-4hr', '>4hrs','NA'],
    'VomitLast': ['<1hr', '1-4hrs','>4hrs', 'NA'],

    # altered mental state
    'AMSAgitated': _yesnona,
    'AMSSleep': _yesnona,
    'AMSSlow': _yesnona,
    'AMSRepeat': _yesnona,
    'AMSOth': _yesnona,

    # skull fractures
    'SFxPalp': ['No', 'Yes', 'Unclear'],
    'SFxPalpDepress': _yesnona,
    'SFxBasHem': _yesnona,
    'SFxBasOto': _yesnona,
    'SFxBasPer': _yesnona,
    'SFxBasRet': _yesnona,
    'SFxBasRhi': _yesnona,

    # hematoma
    'HemaLoc': ['Frontal', 'Occipital','Parietal/Temporal','NA'],
    'HemaSize': ['Small','Medium','Large','NA'],

    # Trauma above clavicle
    'ClavFace': _yesnona,
    'ClavNeck': _yesnona,
    'ClavFro': _yesnona,
    'ClavOcc': _yesnona,
    'ClavPar': _yesnona,
    'ClavTem': _yesnona,

    # Neurological Deficit
    'NeuroDMotor': _yesnona,
    'NeuroDSensory': _yesnona,
    'NeuroDCranial': _yesnona,
    'NeuroDReflex': _yesnona,
    'NeuroDOth': _yesnona,

    # Other Substantial Injury
    'OSIExtremity': _yesnona,
    'OSICut': _yesnona,
    'OSICspine': _yesnona,
    'OSIFlank': _yesnona,
    'OSIAbdomen': _yesnona,
    'OSIPelvis': _yesnona,
    'OSIOth': _yesnona,

    # CT sedation
    'CTSed': _yesnona,
    'CTSedAgitate': _yesnona,
    'CTSedAge': _yesnona,
    'CTSedRqst': _yesnona,
    'CTSedOth': _yesnona,

    # demographics
    'Gender': ['Male', 'Female'],
    'Ethnicity': ['Hispanic', 'Non-Hispanic'],
    'Race': ['White', 'Black', 'Asian', 'Native', 'Pacific', 'Other'],

    # ED data
    'EDDisposition': ['Home','OR', 'Admit', 'Admit Short', 'ICU', 'Transfer', 'AMA', 'Death in ED', 'Other'],

    # CT scan data
    'EDCT': _yesnona,

    # outcome variables
    'PosCT': _yesnona
}