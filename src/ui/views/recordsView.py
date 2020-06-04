from flask import Blueprint, request, render_template, redirect, url_for, request
from ui.database import db_session
from ui.models.case import Case
from ui.database import db_session
from math import ceil

bp = Blueprint('records', __name__, url_prefix='/records')

_RECORDS_PER_PAGE = 10

@bp.route('/', methods=['GET', 'POST'])
def table():

    # get the page from the request, defaulting to the first page
    page = int(request.args.get('page', 1))

    n_cases = Case.query.count()
    n_pages = ceil(n_cases/_RECORDS_PER_PAGE)

    if request.method == 'GET':
        cases = Case.query.order_by(Case.id).limit(_RECORDS_PER_PAGE).offset((page-1)*_RECORDS_PER_PAGE).all()

    if request.method == 'POST':
        id = request.form.get('filter')
        if id != '':
            cases = Case.query.order_by(Case.id).filter(Case.id == id).all()
        else:
            cases = Case.query.order_by(Case.id).limit(_RECORDS_PER_PAGE).offset((page-1)*_RECORDS_PER_PAGE).all()

    if not cases:
        return render_template("records.html")
    else:
        return render_template("records.html", page=page, n_pages=n_pages, cases=cases, n_cases=n_cases)

@bp.route("/edit/<int:id>", methods = ['GET', 'POST'])
def edit(id):
    if request.method == 'GET':
        # patient = crudDB.getPatientById(int(id))
        return render_template('editRecord.html', case_id=id)

    if request.method == 'POST':
        # crudDB.editPatient(request.form.to_dict(), int(id))
        # page = crudDB.totalPages()
        # patients =  crudDB.patientdBypage(1)
        return redirect(url_for('.table'))

@bp.route("/<int:id>/delete/", methods = ['GET'])
def delete(id):
    case = Case.query.filter(Case.id == id).first()
    db_session.delete(case)
    db_session.commit()
    return redirect(url_for('.table'))