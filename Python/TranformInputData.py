#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd 
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import Imputation

def transform(imd,selected_feature):
    disc = imd.to_dict(flat=False)
    input_variables = pd.DataFrame(disc)

    input_variables['GCSTotal'] = pd.to_numeric(input_variables['GCSTotal'])
    for col in list(input_variables):
        if col not in ['GCSTotal']:
            input_variables[col] = input_variables[col].astype('category')
    # Convert into Binary
    input_variables = pd.get_dummies(input_variables.loc[:, ])

    print("Binarization Done")

    colsname = list(input_variables.columns.values)
    availCol = list(set(selected_feature).intersection(colsname))
    notAvailCol = list(set(selected_feature) - set(availCol))

    subset1 = input_variables[input_variables.columns.intersection(availCol)]
    subset2 = pd.DataFrame(columns=notAvailCol)
    subset2.loc[0] = 0

    testData = pd.concat([subset1, subset2], axis=1)
    testData = testData[selected_feature]
    print("Transformation Done")
    return testData

