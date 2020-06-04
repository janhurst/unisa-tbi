from flask import Blueprint, render_template
from ui.forms.caseForm import CaseForm

bp = Blueprint('dashboard', __name__, url_prefix='/dashboard')

@bp.route('/', methods=['GET'])
def dashboard():
    caseForm = CaseForm()
    return (render_template('dashboard.html', caseForm=caseForm))