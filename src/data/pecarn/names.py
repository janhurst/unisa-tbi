from sklearn.feature_extraction import DictVectorizer

variable_names = []

def to_new_names(df):
    """ Rename columns to new names to allow them to be more meaningful """
    for old_name, new_name in _name_map.items():
        df.rename(columns={old_name: new_name}, inplace=True)
    return df

def to_original_names(df):
    """ Rename columns back to original names """
    for old_name, new_name in _name_map.items():
        df.rename(columns={new_name: old_name}, inplace=True)
    return df

""" Name Maps

The map is used to allow to swap between old and new names. The names are changed by
expanding to full words and using CamelCase
"""
_name_map = {
    'Amnesia_verb': 'Amnesia',
    'LOCSeparate': 'LossOfConsciousness',
    'LocLen': 'LossOfConsciousnessDuration',
    'Seiz': 'Seizure',
    'SeizOccur': 'SeizureOccurence',
    'SeizLen': 'SeizureLength',
    'ActNorm': 'ActingNormal',
    'HA_verb': 'HeadAche',
    'HASeverity': 'HeadAcheSeverity',
    'HAStart': 'HeadAcheStart',
    'VomitNbr': 'VomitNumber',
    'AMSOth': 'AMSOther',
    'Hema': 'Hematoma',
    'HemaLoc': 'HematomaLocation',
    'HemaSize': 'HematomaSize',
    'Clav': 'ClavicalTrauma',
    'ClavFace': 'ClavicalTraumaFace',
    'ClavNeck': 'ClavicalTraumaNeck',
    'ClavFro': 'ClavicalTraumaScalpFrontal',
    'ClavOcc': 'ClavicalTraumaScalpOccipital',
    'ClavPar': 'ClavicalTraumaScalpParietal',
    'ClavTem': 'ClavicalTraumaScalpTemporal',

    # TODO consider other renames?
    'AgeInMonths': 'Age',
    'InjuryMech': 'InjuryMechanism',
}