"""
This module provides a set of preprocessing steps to the PECARN Traumatic Brain Injury dataset

"""
import pandas as pd

import logging
logger = logging.getLogger(__name__)

def preprocess(df):
    """ Preprocess the PECARN data """
    # deep copy the dataframe
    df = df.copy()

    # preprocessing steps
    
    # remove dependent columns
    #df = _remove_dependents(df)

    # impute NaN values
    df = _impute_boolean_nans(df)
    df = _impute_categorical_nans(df)

    # now that boolean columns are gauranteed to have no NaN values we can
    # convert booleans to integer so that sklearn understands them
    df = _convert_boolean_to_int(df)

    # turn the remaining categorical columns into booleans (actually integers)
    df = _one_hot_encode(df)

    # return an X (input) matrix and y (class) vector
    return df.drop(columns='PosIntFinal'), df['PosIntFinal']

def _remove_dependents(df):
    """ Remove columns that are not independent 
    
    There are a number of columns where additional information is collected when the response
    is a "Yes". The additional columns have a value of Not Applicable when the "parent" column
    is a "No". 
    
    This implies that the parent No response is already encoded in the additional columns and
    is potentially a confounding variable.

    Here, these parent variables are simply removed.
    """
    drop_cols = ['AgeTwoPlus','Seizure','HeadAche','Vomit','AMS','SFxPalp','SFxBas','Hematoma',
        'ClavicalTrauma','NeuroD','OSI']
    drop_cols.sort()

    # log what is being dropped
    for col in drop_cols:
        logger.debug(f"{col} dropping, not independent")
        
    # do the actual drop        
    df = df.drop(columns=drop_cols)
    return df

_NA = 92

def _impute_boolean_nans(df):
    """ Impute boolean NaNs to False 
    
    Note these are actually Int64 with only two categories
    """
    boolean_cols = [col for col in df if df.dtypes[col] == 'boolean']
    for col in df[boolean_cols]:
        logger.debug(f"{col} setting {df[col].isna().sum()} NaN values to 0")
        df.loc[df[col].isna(), col] = 0
    return df

def _impute_categorical_nans(df):
    """ Impute categorical NaNs

    For categorical types that are just boolean plus NA, we will drop the NA category,
    then set the NaN to False, and finally convert back to boolean

    For any remaining categorical types that have multiple categories, we will set the NaN values to
    the NA value, which will be dropped in the one hot encode step.
    """
    categorical_binary_cols = [col for col in df if df.dtypes[col] == 'category' and _NA in df[col].cat.categories.values]
    for col in df[categorical_binary_cols]:
        # remove the 92 Not Applicable category
        if df[col].isna().sum() > 0:
            logger.debug(f"{col} setting {df[col].isna().sum()} NaN values to False/No")
        df[col] = df[col].cat.remove_categories([_NA])
        df[col] = df.loc[df[col].isna(), col] = False
        
        # convert back to boolean
        df[col] = df[col].astype('boolean')

    # impute most frequent value for categories that still have NaN values
    categorical_cols = [col for col in df if df.dtypes[col] == 'category' and _NA not in df[col].cat.categories.values]
    for col in df[categorical_cols]:
        if df[col].isna().sum() > 0:
            logger.debug(f"{col} setting {df[col].isna().sum()} NaN values to {df[col].value_counts().index[0]}")
            df.loc[df[col].isna(), col] = df[col].value_counts().index[0]

    return df

def _convert_boolean_to_int(df):
    """ Convert boolean nullable types to integer """
    boolean_cols = [col for col in df if df.dtypes[col] == 'boolean']
    for col in df[boolean_cols]:
        logger.debug(f"{col} converting boolean to uint8")
        df[col] = df[col].astype('uint8')
    return df

def _one_hot_encode(df):
    logger.debug("One hot encoding remaining categorical columns")
    df = pd.get_dummies(df)
    df = df[[col for col in df if not col.endswith('_NA')]]
    return df
