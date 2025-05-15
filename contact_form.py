from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, EmailField, TextAreaField
from wtforms.validators import DataRequired, Length, Email
from wtforms.validators import ValidationError

class ContactForm(FlaskForm):
    """
    Form for the Contact page that handles input errors
    """
    name = StringField('Name',
                       validators=[DataRequired(message="Field is empty"),
                                   Length(min=3,message="Name field must have at least 3 characters")])
    email = EmailField('Email',validators=[DataRequired(message="Field is empty"),Email(message="Invalid email format")])
    message = TextAreaField('Message',validators=[DataRequired(message="Field is empty")])

    submit = SubmitField('Submit')