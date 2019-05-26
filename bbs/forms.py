from flask_ckeditor import CKEditorField
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, TextAreaField, ValidationError, HiddenField, BooleanField, PasswordField
from wtforms.validators import DataRequired, Email, Length, Optional, URL

from bbs.models import Subcategory
# import categoryid

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(1, 20)])
    password = PasswordField('Password', validators=[DataRequired(), Length(6, 32)])
    remember = BooleanField('Remember me')
    submit = SubmitField('Log in')


class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(8, 64)])
    # category = SelectField('Category', coerce=int)
    subcategory = SelectField('Subcategory', coerce=int)
    body = CKEditorField('Body', validators=[DataRequired()])
    submit = SubmitField()

    def __init__(self, categoryid, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.subcategory.choices = [(subcategory.id, subcategory.name)
                                 for subcategory in Subategory.query.filter_by(category_id=categoryid).all()]


class CommentForm(FlaskForm):
    body = TextAreaField('Comment', validators=[DataRequired()])
    submit = SubmitField()
