"""
This module provides cleaning operations over the original PECARN TBI dataset.

The cleaning logic applied is:
 - remove columns that are not known when a patient presents
 - remove columns that don't directly relate to the diagnosis
 - fill missing GCS values when possible
 - remove some records with small numbers of NaN values
 - set better categories for some NaN values
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

    # remove the NA category, as it is not very helpful
    df = _remove_NA_category(df)

    # deal with NaNs
    df = _impute_boolean_nans(df)
    df = _impute_categorical_nans(df)
    df = _impute_numeric_nans(df)

    return df

def _drop_columns(df):
    """ remove columns that we don't have when a new patient is presented at an ED """
    drop_cols = []

    # duplicate or implied by other columns
    drop_cols.append('AgeinYears')  
    drop_cols.append('AgeTwoPlus')  
    drop_cols.append('High_impact_InjSev')

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

    # then drop the GCSTotal, and GCSGroup, we no longer need them
    df.drop(columns='GCSTotal', inplace=True)
    df.drop(columns='GCSGroup', inplace=True)
    
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
    df.loc[df['InjuryMech'].isna(), 'InjuryMech'] = 90
    return df

def _clean_LOCSeparate(df):
    """ Set the LOCSeparate NaN values to No """
    logger.debug(f"LOCSeparate setting {df['LOCSeparate'].isna().sum()} NaN values to No (0)")
    df.loc[df['LOCSeparate'].isna(), 'LOCSeparate'] = 0
    return df

def _clean_Amnesia_verb(df):
    """ Set the Amnesia_verb NaN values to No """
    logger.debug(f"Amnesia_verb setting {df['Amnesia_verb'].isna().sum()} NaN values to No (0)")
    df.loc[df['Amnesia_verb'].isna(), 'Amnesia_verb'] = 0
    return df

def _remove_NA_category(df):
    """ Remove the NA (92) category """
    NA = 92
    category_with_na = [col for col in df.select_dtypes(include='category') if NA in df[col].cat.categories.values]

    for col in category_with_na:
        # remove the NA/92 category, which will change NA values to NaNs
        df[col] = df[col].cat.remove_categories([NA])

        # if there are now only 2 categories, convert to boolean
        if len(df[col].cat.categories) == 2:
            df[col] = df[col].astype('boolean')
    
    return df
 
def _impute_boolean_nans(df):
    """ Impute boolean NaNs to False """
    for col in df.select_dtypes(include='boolean'):
        if df[col].isna().sum() > 0:
            logger.debug(f"{col} setting {df[col].isna().sum()} NaN values to 0")
            df.loc[df[col].isna(), col] = 0
    return df

def _impute_categorical_nans(df):
    """ Impute categorical NaNs to most frequent value """
    # impute most frequent value for categories that still have NaN values
    for col in df.select_dtypes(include='category'):
        if df[col].isna().sum() > 0:
            logger.debug(f"{col} setting {df[col].isna().sum()} NaN values to {df[col].value_counts().index[0]}")
            df.loc[df[col].isna(), col] = df[col].value_counts().index[0]

    return df

def _impute_numeric_nans(df):
    """ Impute numeric NaNs to the mean """
    for col in df.select_dtypes(include='int64'):
        if df[col].isna().sum() > 0:
            logger.debug(f"{col} setting {df[col].isna().sum()} NaN values to {df[col].mean()}")
            df.loc[df[col].isna(), col] = df[col].mean()
    return df