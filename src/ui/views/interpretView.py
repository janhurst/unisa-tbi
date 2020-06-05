from os import listdir, path
import fnmatch
import json
from flask import Blueprint, request, render_template, redirect, url_for, Response
from flask_wtf import FlaskForm
from wtforms import SelectField
from ui.forms.caseForm import CaseForm
from ui.api.model_management import ARTIFACTS_DIR

from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg

import random
import io
from ui.predict.prediction import Prediction



bp = Blueprint('interpret', __name__, url_prefix='/interpret')

@bp.route('/<int:case_id>/<string:experiment_id>/<string:model>', methods=['GET', 'POST'])
def model(case_id, experiment_id, model):
    """ Information about the prediction """


    # grab the model and redo the prediction
    

    # depending upon the type of model we may wish to show a different template
    return render_template('interpret.html', case_id=case_id, experiment_id=experiment_id, model=model)


@bp.route('/<int:case_id>/<string:experiment_id>/<string:model>/important_features.png')
def important_features(case_id, experiment_id, model):
    caseform = CaseForm()
    caseform.readFromDatabase(case_id)
    prediction = Prediction(experiment_id + path.sep + model, caseform)
    output = prediction.feature_importance()
    return Response(output, mimetype='image/png')

@bp.route('/<int:case_id>/<string:experiment_id>/<string:model>/shap.png')
def shap(case_id, experiment_id, model):
    caseform = CaseForm()
    caseform.readFromDatabase(case_id)
    prediction = Prediction(experiment_id + path.sep + model, caseform)
    output = prediction.shap()
    return Response(output, mimetype='image/png')    