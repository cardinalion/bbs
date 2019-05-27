

from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from flask_debugtoolbar import DebugToolbarExtension
from flask_ckeditor import CKEditor

db = SQLAlchemy()
csrf = CSRFProtect()
toolbar = DebugToolbarExtension()
ckeditor = CKEditor()
