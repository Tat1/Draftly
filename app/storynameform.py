from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    storyname = StringField('Name', validators=[DataRequired()])
    submit = SubmitField('Submit')
