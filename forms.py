from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, TextAreaField, BooleanField
from wtforms.validators import InputRequired, Optional, Length, URL, NumberRange

class AddPetForm(FlaskForm):
    """Form for adding a pet for adoption."""
    
    name = StringField("Name:", validators=[InputRequired()])
    species = SelectField("Species:", choices=[("cat", "cat"), ("dog", "dog"), ("porcupine", "porcupine")])
    photo_url = StringField("Photo URL:", validators=[Optional(), URL()])
    age = IntegerField("Age:", validators=[Optional(), NumberRange(min=0, max=30)])
    notes = TextAreaField("Pet Notes (quirks):", validators=[Optional(), Length(min=10)])
    
class EditPetForm(FlaskForm):
    """Form for edit an existing pet."""
    
    photo_url = StringField("Photo URL:", validators=[Optional(), URL()])
    notes = TextAreaField("Pet Notes (quirks):", validators=[Optional(), Length(min=10)])
    available = BooleanField("Available to Adopt?")