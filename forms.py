from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, DateTimeField, SubmitField, SelectField
from wtforms.validators import DataRequired, Optional, NumberRange
from datetime import datetime

class ClubForm(FlaskForm):
    name = StringField('Club name', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[Optional()])
    submit = SubmitField('Save')

class EventForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[Optional()])
    location = StringField('Location', validators=[Optional()])
    start_time = StringField('Start time (YYYY-mm-dd HH:MM)', validators=[Optional()])
    end_time = StringField('End time (YYYY-mm-dd HH:MM)', validators=[Optional()])
    capacity = IntegerField('Capacity', validators=[Optional(), NumberRange(min=0)])
    club_id = SelectField('Club', coerce=int, validators=[Optional()])
    submit = SubmitField('Save')

    def parse_dt(self, value):
        if not value:
            return None
        try:
            return datetime.strptime(value, '%Y-%m-%d %H:%M')
        except Exception:
            return None

class RegistrationForm(FlaskForm):
    attendee_name = StringField('Your name', validators=[DataRequired()])
    submit = SubmitField('Register')
