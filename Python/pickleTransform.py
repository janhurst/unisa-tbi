import flask
import pickle
import pandas as pd
import numpy as np
import DataCleaning
import Imputation
import FeatureEngineering
import Model

pecarn_data = pd.read_csv('TBI PUD 10-08-2013.csv', index_col=0)
clean_data = DataCleaning.datacleaning(pecarn_data)
imputed_data = Imputation.impute(clean_data)
binary_data = FeatureEngineering.binarized(imputed_data)
features,clf,xTrain,yTrain = Model.getModel(binary_data)
clf.features = features
clf.xTrain = xTrain
clf.yTrain = yTrain
# log the model
pickle_file = 'sklearn.model.pkl'
with open(pickle_file, "wb") as f:
        pickle.dump(clf, f)