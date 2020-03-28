#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd 
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import Imputation

def binarized(pecarn_df):
    # Convert into Category
    pecarn_df['AgeinYears'] = pd.to_numeric(pecarn_df['AgeinYears'])
    pecarn_df['GCSTotal'] = pd.to_numeric(pecarn_df['GCSTotal'])
    for col in list(pecarn_df):
        if col not in ['AgeinYears']:
            if col not in ['GCSTotal']:
                pecarn_df[col] = pecarn_df[col].astype('category')
    # Convert into Binary

    pecarn_df1 = pd.get_dummies(pecarn_df.loc[:, pecarn_df.columns != 'PosIntFinal'])
    pecarn_df1['PosIntFinal'] = pecarn_df['PosIntFinal']

    # Removed 90/91/92

    pecarn_df1 = pecarn_df1[pecarn_df1.columns.drop(list(pecarn_df1.filter(regex='90')))]
    pecarn_df1 = pecarn_df1[pecarn_df1.columns.drop(list(pecarn_df1.filter(regex='91')))]
    pecarn_df1 = pecarn_df1[pecarn_df1.columns.drop(list(pecarn_df1.filter(regex='92')))]

    pecarn_df = pecarn_df1

    print("Binarisation Done")
    return pecarn_df
