from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import OperationalError, ProgrammingError
from os import path, mkdir, getenv, environ

#engine = create_engine('sqlite:///tbi.db', convert_unicode=True)
#engine = create_engine('postgresql://tbi:tbi@localhost/tbi', convert_unicode=True)
if 'SQLALCHEMY_DATABASE_URI' in environ:
    engine = create_engine(getenv('SQLALCHEMY_DATABASE_URI'), convert_unicode=True)
else:
    engine = create_engine('sqlite:///tbi.db', convert_unicode=True)

db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    from ui.models.case import Case
    db_session.close_all()
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

# try and initialize the database if it doesn't exist - this is a little brittle
try:
    from ui.models.case import Case
    Case.query.first()
except (OperationalError, ProgrammingError) as e:
    init_db()
