# this script builds an xgboost classifier
import os
import pandas as pd
import neptune 
import pickle

from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import f1_score, accuracy_score, average_precision_score
from xgboost import XGBClassifier
from sklearn.pipeline import Pipeline

from data import pecarn

if __name__ == "__main__":

    # bring the pecarn data in
    df = pecarn.clean(pecarn.load(fromCsv=True))
    X = df.drop(columns='PosIntFinal')
    y = pecarn.preprocess(df[['PosIntFinal']])

    # configure training and test datasets
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.75, test_size=0.25, stratify=y, random_state=1234)

    # create the pipeline/classifier
    clf = XGBClassifier()
    pipeline = Pipeline(steps=[
        ('data.pecarn.preprocess', pecarn.make_preprocess_pipeline()),
        ('xgboost', clf)
    ])

    # save the feature names for use later in prediction
    pipeline.input_features = X[0:0]

    # neptune initialization - NEPTUNE_API_TOKEN and NEPTUNE_PROJECT environment variables must be set
    neptune.init()

    # create a neptune experiment to log to
    with neptune.create_experiment(name='xgboost.XGBClassifier',
        params=clf.get_params(),
        upload_source_files=[__file__,'src/data/pecarn/*.py'],
        send_hardware_metrics=False) as exp:
        
        # train the classifier
        pipeline.fit(X_train, y_train)

        # calculate scores on train set
        y_train_pred = pipeline.predict(X_train)
        train_scores = {
            'accuracy': accuracy_score(y_train, y_train_pred),
            'f1': f1_score(y_train, y_train_pred),
            'f1_weighted': f1_score(y_train, y_train_pred, average='weighted'),
            'avg_precision': average_precision_score(y_train, y_train_pred)
        }

        # calculate scores on test set
        y_pred = pipeline.predict(X_test)
        test_scores = {
            'accuracy': accuracy_score(y_test, y_pred),
            'f1': f1_score(y_test, y_pred),
            'f1_weighted': f1_score(y_test, y_pred, average='weighted'),
            'avg_precision': average_precision_score(y_test, y_pred)
        }

        # log the scores
        for metric_name, score in train_scores.items():
            exp.send_metric('train_' + metric_name, score)
        for metric_name, score in test_scores.items():
            exp.send_metric('test_' + metric_name, score)

        # log the model
        pickle_file = exp.name + '.pkl'
        with open(pickle_file, "wb") as f:
            pickle.dump(pipeline, f)
        exp.log_artifact(pickle_file)
        os.remove(pickle_file)       
