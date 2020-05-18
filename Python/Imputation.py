#!/usr/bin/env python
# coding: utf-8


import pandas as pd 
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from Python import DataCleaning
from sklearn.impute import SimpleImputer

def impute(pecarn_df):
    # create an imputer using the 'most_frequent' strategy
    imputer = SimpleImputer(missing_values=np.nan, strategy='most_frequent', verbose=2)

    # fit the imputer for any columns that have NaNs
    total_nans = pecarn_df.isna().sum().sum()
    cols_with_nan = list(pecarn_df.columns[pecarn_df.isna().sum() > 0])
    #print(f"  Removing {total_nans} NaN values from {len(cols_with_nan)} columns")

    # Convert into Category
    pecarn_df['AgeInMonth'] = pd.to_numeric(pecarn_df['AgeInMonth'])
    pecarn_df['GCSTotal'] = pd.to_numeric(pecarn_df['GCSTotal'])
    pecarn_df['GCSEye'] = pd.to_numeric(pecarn_df['GCSEye'])
    pecarn_df['GCSMotor'] = pd.to_numeric(pecarn_df['GCSMotor'])
    pecarn_df['GCSVerbal'] = pd.to_numeric(pecarn_df['GCSVerbal'])
    for col in list(pecarn_df):
        if col not in ['AgeInMonth']:
            if col not in ['GCSEye']:
                if col not in ['GCSMotor']:
                    if col not in ['GCSVerbal']:
                        if col not in ['GCSTotal']:
                            pecarn_df[col] = pecarn_df[col].astype('category')

    
    # Clean GCS
    #print(pecarn_df['GCSEye'].isna().sum().sum())
    #print(pecarn_df['GCSVerbal'].isna().sum().sum())
    #print(pecarn_df['GCSMotor'].isna().sum().sum())

    gcs_fill = pecarn_df['GCSTotal'].eq(15) & (pecarn_df['GCSEye'].isna() | pecarn_df['GCSVerbal'].isna() | pecarn_df['GCSMotor'].isna())
    pecarn_df.loc[gcs_fill, 'GCSEye'] = 4
    pecarn_df.loc[gcs_fill, 'GCSVerbal'] = 5
    pecarn_df.loc[gcs_fill, 'GCSMotor'] = 6

    # this code is not working see why
    if pecarn_df['GCSEye'].empty:
        if not (pecarn_df['GCSVerbal'].empty & pecarn_df['GCSMotor'].empty):
            pecarn_df['GCSEye'] = pecarn_df['GCSTotal'] - (pecarn_df['GCSVerbal']+pecarn_df['GCSMotor'])
    if pecarn_df['GCSVerbal'].empty:
        if not (pecarn_df['GCSVerbal'].empty & pecarn_df['GCSMotor'].empty):
            pecarn_df['GCSVerbal'] = pecarn_df['GCSTotal'] - (pecarn_df['GCSEye']+pecarn_df['GCSMotor'])
    if pecarn_df['GCSMotor'].empty:
        if not (pecarn_df['GCSVerbal'].empty & pecarn_df['GCSEye'].empty):
            pecarn_df['GCSMotor'] = pecarn_df['GCSTotal'] - (pecarn_df['GCSVerbal']+pecarn_df['GCSEye'])\

    pecarn_df = pecarn_df[pd.notnull(pecarn_df['GCSEye'])]
    pecarn_df = pecarn_df[pd.notnull(pecarn_df['GCSVerbal'])]
    pecarn_df = pecarn_df[pd.notnull(pecarn_df['GCSMotor'])]

    pecarn_df.drop(columns='GCSTotal', inplace=True)

    #print(pecarn_df.dtypes)
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

