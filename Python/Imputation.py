#!/usr/bin/env python
# coding: utf-8


import pandas as pd 
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import DataCleaning
from sklearn.impute import SimpleImputer

def impute(pecarn_df):
    # create an imputer using the 'most_frequent' strategy
    imputer = SimpleImputer(missing_values=np.nan, strategy='most_frequent', verbose=2)

    # fit the imputer for any columns that have NaNs
    total_nans = pecarn_df.isna().sum().sum()
    cols_with_nan = list(pecarn_df.columns[pecarn_df.isna().sum() > 0])
    #print(f"  Removing {total_nans} NaN values from {len(cols_with_nan)} columns")

    # Convert into Category
    pecarn_df['AgeinYears'] = pd.to_numeric(pecarn_df['AgeinYears'])
    pecarn_df['GCSTotal'] = pd.to_numeric(pecarn_df['GCSTotal'])
    for col in list(pecarn_df):
        if col not in ['AgeinYears']:
            if col not in ['GCSTotal']:
                pecarn_df[col] = pecarn_df[col].astype('category')

    pecarn_df.dtypes
    imputer.fit(pecarn_df[cols_with_nan])
    imputed = imputer.fit_transform(pecarn_df[cols_with_nan])
    imputed

    # store the imputed values
    data_imputed = pecarn_df
    data_imputed[cols_with_nan] = imputed

    # convert the imputed values back to categorical
    for col in list(data_imputed[cols_with_nan]):
        data_imputed[col] = data_imputed[col].astype('Int64').astype('category')

    # In[38]:
    print("Imputation Done")
    return data_imputed
