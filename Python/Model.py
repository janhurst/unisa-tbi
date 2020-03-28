#!/usr/bin/env python
# coding: utf-8

import pandas as pd 
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import FeatureEngineering
import matplotlib.pyplot as plt
# use feature importance for feature selection, with fix for xgboost 1.0.2
from numpy import loadtxt
from numpy import sort
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
from sklearn.feature_selection import SelectFromModel


# define custom class to fix bug in xgboost 1.0.2
class MyXGBClassifier(XGBClassifier):
    @property
    def coef_(self):
        return None

def getModel(pecarn_df):
    # load data
    length_df = pecarn_df.shape[1] - 1
    X = pecarn_df.iloc[:, 0:length_df].astype('int64')  # independent columns
    Y = pecarn_df.iloc[:, -1].astype('int64')  # target column

    # split data into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(X.to_numpy(), Y.to_numpy(), test_size=0.33, random_state=7)

    # fit model on all training data
    model = MyXGBClassifier()
    model.fit(X_train, y_train)
    # make predictions for test data and evaluate
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    # print("Accuracy: %.2f%%" % (accuracy * 100.0))
    # Fit model using each importance as a threshold
    thresholds = sort(model.feature_importances_)
    # In[10]:
    thresholds = thresholds[thresholds != 0.0]
    thresholds = list(dict.fromkeys(thresholds))


    # Manually choosing Number and Threshold
    last_thresholds = thresholds[-50:]
    thresh = last_thresholds[0]
    # print(thresh)

    # select features using threshold
    selection = SelectFromModel(model, threshold=thresh, prefit=True)
    select_X_train = selection.transform(X_train)
    n = select_X_train.shape[1]
    # train model
    selection_model = XGBClassifier(scale_pos_weight=1)
    selection_model.fit(select_X_train, y_train)
    # eval model
    select_X_test = selection.transform(X_test)
    predictions = selection_model.predict(select_X_test)
    accuracy = accuracy_score(y_test, predictions)
    f1 = f1_score(y_test, predictions)
    print("Thresh=%.3f, n=%d, Accuracy: %.2f%%, F1 score: %.2f" % (thresh, n, accuracy * 100.0, f1))

    X = pecarn_df.iloc[:, 0:length_df].astype('int64')  # independent columns
    # plot graph of feature importances for better visualization
    feat_importances = pd.Series(model.feature_importances_, index=X.columns)
    feat_importances.nlargest(n).plot(kind='barh')
    # plt.show()

    features = pd.DataFrame(model.feature_importances_, columns=['Importance'], index=X.columns)
    features['Feature'] = features.index
    selected_features = features[features.Importance >= thresh]
    #print(selected_features.sort_values(by='Importance', ascending=False))
    return selected_features['Feature'].tolist(),selection_model
