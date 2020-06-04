""" A Flask application to deploy the PECARN TBI prediction models """
from flask import Flask

def create_app():
    """ Flask factory """
    app = Flask(__name__, template_folder='templates')

    # enable some Jinja2 extensions
    app.jinja_options['extensions'].append('jinja2.ext.do')

    with app.app_context():
        import os
        from flask import redirect, url_for
        from ui.views import caseView, recordsView, dashboardView, interpretView
        from ui.api import model_management, db_management

        # register the view blueprints
        app.register_blueprint(caseView.bp)
        app.register_blueprint(recordsView.bp)
        app.register_blueprint(dashboardView.bp)
        app.register_blueprint(interpretView.bp)

        # register the models API blueprints
        app.register_blueprint(model_management.bp)
        
        # register the DB management API
        app.register_blueprint(db_management.bp)
        
        # add a random secrets key
        app.config['SECRET_KEY'] = os.urandom(32)

        # redirect base URL to a new empty Case
        @app.route('/')
        def index():
            return redirect(url_for('case.newCase'))

        # hook SQLAlchemy and remove database sessions as required
        from ui.database import db_session
        @app.teardown_appcontext
        def shutdown_session(exception=None):
            db_session.remove()

    return app
