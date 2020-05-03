"""
This module provides a set of preprocessing steps to the PECARN Traumatic Brain Injury dataset

"""
import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline 
from sklearn.preprocessing import FunctionTransformer

import logging
logger = logging.getLogger(__name__)

def preprocess(df):
    """ Preprocess the PECARN data """
    # deep copy the dataframe
    df = df.copy()

    # preprocessing steps in a sklearn transformer pipeline
    preprocess_pipeline = make_preprocess_pipeline()
 
    # split the class variable
    X = df.drop(columns='PosIntFinal')
    y = df[['PosIntFinal']]

    # return the transformed dataframes
    return preprocess_pipeline.transform(X), preprocess_pipeline.transform(y)

def make_preprocess_pipeline():
    """ Create a sklearn.Pipeline for the preprocessing steps """
    pipeline = Pipeline(steps=[
        ('impute_booleans_nans', FunctionTransformer(_impute_boolean_nans)),
        ('impute_categorical_nans', FunctionTransformer(_impute_categorical_nans)),
        ('convert_booleans_to_int', FunctionTransformer(_convert_boolean_to_int)),
        ('onehotencode', FunctionTransformer(_one_hot_encode))
    ], verbose=True)
    return pipeline

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
    NA = 92

    categorical_binary_cols = [col for col in df if df.dtypes[col] == 'category' and NA in df[col].cat.categories.values]
    for col in df[categorical_binary_cols]:
        # remove the 92 Not Applicable category
        if df[col].isna().sum() > 0:
            logger.debug(f"{col} setting {df[col].isna().sum()} NaN values to False/No")
        df[col] = df[col].cat.remove_categories([NA])
        df[col] = df.loc[df[col].isna(), col] = False
        
        # convert back to boolean
        df[col] = df[col].astype('boolean')

    # impute most frequent value for categories that still have NaN values
    categorical_cols = [col for col in df if df.dtypes[col] == 'category' and NA not in df[col].cat.categories.values]
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
