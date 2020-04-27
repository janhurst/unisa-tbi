"""
This module provides cleaning operations over the original PECARN TBI dataset.

The cleaning logic applied is:
 - remove columns that are not known when a patient presents
 - remove columns that don't directly relate to the diagnosis
 - rename columns to make them easier to read
 - relabel the categories to make them more meaningful 
"""
import pandas as pd
import logging

logger = logging.getLogger(__name__)

def clean(df):
    """ Clean the PECARN data """
    
    # deep copy the dataframe
    df = df.copy() 
    
    # apply cleaning logic - note the order here is somewhat important to ensure
    # that each cleaning logic can be "switch off" later
    df = _drop_columns(df)

    # apply logic that has a basis in domain knowledge
    df = _clean_gcs(df)

    # drop some records that have small number of NaNs
    df = _clean_PosIntFinal(df)
    df = _clean_Gender(df)

    # remove some NaNs by setting to a more appropriate value
    df = _clean_InjuryMech(df)
    df = _clean_LOCSeparate(df)
    df = _clean_Amnesia_verb(df)

    # finally rename
    df = to_new_names(df)

    return df

def _drop_columns(df):
    """ remove columns that we don't have when a new patient is presented at an ED """
    drop_cols = []

    # duplicate or implied by other columns
    drop_cols.append('AgeinYears')  
    drop_cols.append('High_impact_InjSev')
    drop_cols.append('GCSGroup')

    # variables that are not relevant
    drop_cols.append('Certification')       
    drop_cols.append('EmplType')

    # observations that categorize the data but don't help to predict
    drop_cols.append('EDCT')
    drop_cols.append('PosCT')
    drop_cols.append('EDDisposition')
    drop_cols.append('Observed')

    # the "conditions" that are used to determine the PosIntFinal class
    drop_cols.append('DeathTBI')
    drop_cols.append('HospHead')
    drop_cols.append('HospHeadPosCT')
    drop_cols.append('Neurosurgery')
    drop_cols.append('Intub24Head')

    # the following are information that is determined after the case outcome
    drop_cols.extend( [col for col in df if col.startswith('Ind')] )
    drop_cols.extend( [col for col in df if col.startswith('Finding')] )
    drop_cols.extend( [col for col in df if col.startswith('CT')] )

    # sort the variable alphabetically - just for convenience
    drop_cols.sort()
    
    # do the actual drop    
    return df.drop(columns=drop_cols)

def _clean_gcs(df):
    """ Fill GCSEye, GCSVerbal, GCSMotor when the GCSTotal is 15 """
    logger.debug("Filling missing GCSEye, GCSVerbal, GCSMotor when GCSTotal is 15")
    gcs_fill = df['GCSTotal'].eq(15) & (df['GCSEye'].isna() | df['GCSVerbal'].isna() | df['GCSMotor'].isna())
    df.loc[gcs_fill, 'GCSEye'] = 4
    df.loc[gcs_fill, 'GCSVerbal'] = 5
    df.loc[gcs_fill, 'GCSMotor'] = 6

    # then drop the GCSTotal
    df.drop(columns='GCSTotal', inplace=True)
    
    return df

def _clean_PosIntFinal(df):
    """ Drop 20 rows where PosIntFinal is NaN """
    logger.debug(f"PosIntFinal Dropping {df['PosIntFinal'].isna().sum()} rows where PosIntFinal is NaN")
    return df[~df['PosIntFinal'].isna()]

def _clean_Gender(df):
    """ Drop 3 rows where Gender is NaN """
    logger.debug(f"Gender Dropping {df['Gender'].isna().sum()} rows where Gender is NaN")
    return df[~df['Gender'].isna()]

def _clean_InjuryMech(df):
    """ Set the InjuryMech NaN values to 90 Other """
    logger.debug(f"InjuryMech setting {df['InjuryMech'].isna().sum()} NaN values to Other (90)")
    df.loc[df['InjuryMech'].isna(), 'InjuryMech'] = 'Other'
    return df

def _clean_LOCSeparate(df):
    """ Set the LOCSeparate NaN values to No """
    logger.debug(f"LOCSeparate setting {df['LOCSeparate'].isna().sum()} NaN values to No")
    df.loc[df['LOCSeparate'].isna(), 'LOCSeparate'] = 'No'
    return df

def _clean_Amnesia_verb(df):
    """ Set the Amnesia_verb NaN values to No """
    logger.debug(f"Amnesia_verb setting {df['Amnesia_verb'].isna().sum()} NaN values to No")
    df.loc[df['Amnesia_verb'].isna(), 'Amnesia_verb'] = 'No'
    return df

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