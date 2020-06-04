from flask import Blueprint, abort, jsonify, redirect, url_for
from ui.database import init_db

# create the blueprint
bp = Blueprint('db_management', __name__, url_prefix='/api/db')

@bp.route('/init')
def initialize_database():
    """ Initialize the database """
    init_db()
    return redirect(url_for('case.emptyCase'))