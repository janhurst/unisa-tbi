from os import path
import pickle
import pandas as pd
from flask_wtf import FlaskForm
from wtforms import FormField
from ..forms.caseForm import CaseForm
from ui.api.model_management import ARTIFACTS_DIR
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg
import io
import matplotlib as plt

import shap

class Prediction:
    
    model_file: None
    pipeline: None
    df: None
    result: None

    def __init__(self, model, caseform: CaseForm):

        # pick and load the requested model
        self.model_file = path.join(ARTIFACTS_DIR, model + '.pkl')
        self.pipeline = pickle.load(open(self.model_file, 'rb'))

        # create the inputs
        self.df = self._load_features_from_caseform(caseform)

        # call the model
        self.call_model()
    
    def call_model(self):
        """ Call the model """
        result = self.pipeline.predict(self.df)
        self.result = int(result[0])

    def _load_features_from_caseform(self, caseform: CaseForm):

        df = self.pipeline.input_features

        # we need to unwrap the FormField (subforms)
        data = caseform.data
        fieldForms = [field for field in caseform if isinstance(field, FormField)]
        for fieldForm in fieldForms:
            data = {**data, **fieldForm.data}

        try:
            for col in df:
                if col in data.keys():
                    # need to change false to zeros
                    if data[col] == False:
                        df[col] = [0]
                    else:
                        df[col] = [data[col]]
        except Exception as e:
            raise e

        return df

    def feature_importance(self):
        plt.use('agg')

        feat_importances = None
        clf = self.pipeline.steps[-1][1]
        if hasattr(clf, 'feature_importances_'):
            importances = clf.feature_importances_
            # figure out indices then names
            names = self.pipeline.input_features.columns[self.pipeline.steps[-2][1].get_support()]

            feat_importances = pd.Series(importances, index=names)
        
        fig = Figure()
        ax = fig.add_subplot(1,1,1)

        feat_importances.nlargest(10).plot.barh(ax=ax)
        
        # create output stream
        output = io.BytesIO()

        # "print" as PNG to the output stream
        FigureCanvasAgg(fig).print_png(output)

        # need to rewind the stream
        output.seek(0)

        return output

    def shap(self):
        plt.use('agg')

        shap.initjs()

        explainer = shap.TreeExplainer(self.pipeline.steps[-1][1])
        shap_values = explainer.shap_values(self.df.loc[:, self.pipeline.steps[-2][1].get_support()])
        
        fig = Figure()
        fig.add_axes(shap.decision_plot(explainer.expected_value, shap_values[0]))

        output = io.BytesIO()
        FigureCanvasAgg(fig).print_png(output)
        output.seek(0)

        return output