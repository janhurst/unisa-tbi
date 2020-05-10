""" This module loads the original PECARN Traumatic Brain Injury dataset into a pd.DataFrame()

When reading from the original CSV file the data is first coerced into a nullable type.

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

def load(fromCsv: bool = False):
    """ Load the PECARN data from either CSV or a cache Pickle file """
    if not fromCsv and path.exists(_TBI_PKL_FILE):
        return _frompkl()
    else:
        return _fromcsv()

def _fromcsv():
    """ Load the PECARN TBI dataset from a CSV file if it exists """
    logger.info('Loading from CSV file ' + _TBI_CSV_FILE)
    try:
        df = pd.read_csv(_TBI_CSV_FILE, index_col=0, dtype='Int64')
    
        # fix the data types
        df = _datatypes(df)

        # reorder the columns alphabetically
        df = df.reindex(sorted(df.columns), axis=1)

         # pickle the tbi data
        with open(_TBI_PKL_FILE, 'wb') as f:
            pickle.dump(df, f)

        return df
    except FileNotFoundError:
        logger.error(_TBI_CSV_FILE + ' not found')
        raise

def _frompkl():
    """ Load the PECARN TBI dataset from a Pickle file if it exists """
    logger.info('Loading from Pickle file ' + _TBI_PKL_FILE)
    with open(_TBI_PKL_FILE, 'rb') as f:
        return pickle.load(f)

_CATEGORICAL_THRESHOLD = 15

def _datatypes(df: pd.DataFrame):
    """ converts the Int64 data in each column to either boolean or categorical """
    numeric_cols = ['GCSTotal', 'AgeInMonth', 'AgeinYears']

    for col in df.drop(columns=numeric_cols):

        # if there are only two values (0 and 1, plus NaNs) then cast to nullable boolean type
        if df[col].nunique() == 2 and df[col].max() < 2:
            df[col] = df[col].astype('boolean')
        else:
            df[col] = df[col].astype('category')

    return df
