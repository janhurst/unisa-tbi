from flask import Blueprint, request, render_template, redirect, url_for

from ui.database import db_session
from ui.models.case import Case
from ui.forms.caseForm import CaseForm
from ui.forms.modelForm import ModelForm
from ui.predict.prediction import Prediction

bp = Blueprint('case', __name__, url_prefix='/case')

@bp.route('/', methods=['GET'])
def emptyCase():
    return render_template('case.html', modelform=ModelForm.get(), case=CaseForm())

@bp.route('/<int:id>', methods=['GET'])
def getExistingCase(id):
    """ Show the form with data from the database """
    caseForm, modelForm, update = _init()

    caseForm.readFromDatabase(id)
    return render_template('case.html', modelform=modelForm, case=caseForm, update=update)

@bp.route('/', methods=['POST'])
def newCase():
    """ Create a new case, validate the form, and call prediction """
    caseForm, modelForm, update = _init()    

    # create the new case in the database
    caseForm.createInDatabase()

    # try and predict
    if caseForm.validate_on_submit():
        return _predict(modelForm, caseForm)
    else:
        return render_template('case.html', modelform=modelForm, case=caseForm, update=update)

@bp.route('/<int:id>', methods=['POST'])
def updateExistingCase(id):
    caseForm, modelForm, update = _init()

    # update the case in the database
    caseForm.updateInDatabase()

    # try and predict
    if caseForm.validate_on_submit():
        return _predict(modelForm, caseForm)
    else:
        return render_template('case.html', modelform=modelForm, case=caseForm, update=update)

def _init():
    return CaseForm(), ModelForm.get(), request.args.get('update', False)

def _predict(modelForm, caseForm):
    try: 
        prediction = Prediction(modelForm.data['model'], caseForm)

        # store the prediction
        caseForm.Evaluation.Prediction.data = prediction.result
        caseForm.updateInDatabase()

        return render_template('case.html', case=caseForm, modelform=modelForm, prediction=prediction.result, update=True)
    except Exception as e:
        return render_template('case.html', case=caseForm, modelform=modelForm, error=e)
