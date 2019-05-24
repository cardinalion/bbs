

from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from flask_debugtoolbar import DebugToolbarExtension

db = SQLAlchemy()
csrf = CSRFProtect()
toolbar = DebugToolbarExtension()
