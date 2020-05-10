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
 
    # return the transformed dataframes
    return preprocess_pipeline.transform(df)

def make_preprocess_pipeline():
    """ Create a sklearn.Pipeline for the preprocessing steps """
    pipeline = Pipeline(steps=[
        ('convert_to_float', FunctionTransformer(_convert_to_float)),
    ], verbose=True)
    return pipeline

def _convert_to_float(df):
    """ Convert to float64 for sklearn compatibility """
    for col in df:
        logger.debug(f"{col} converting to float64")
        df.loc[:,col] = df[col].astype('float64')
    return df

# def _one_hot_encode(df):
#     logger.debug("One hot encoding remaining categorical columns")
#     df = pd.get_dummies(df)
#     df = df[[col for col in df if not col.endswith('_NA')]]
#     return df
