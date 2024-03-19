from . import db
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, SelectField, FileField
from wtforms.validators import DataRequired
from flask_wtf.file import FileAllowed
from flask_wtf.file import FileRequired, FileAllowed

class Property(db.Model):
    __tablename__ = "properties"
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    bedrooms = db.Column(db.Integer, nullable=False)
    bathrooms = db.Column(db.Integer, nullable=False)
    location = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    property_type = db.Column(db.String(50), nullable=False)
    photo = db.Column(db.String(120), nullable=False)

    def __init__(self, title, description, bedrooms, bathrooms, location, price, property_type, photo):
        self.title = title
        self.description = description
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        self.location = location
        self.price = price
        self.property_type = property_type
        self.photo = photo
    
    def get_id(self):
        try:
            return unicodedata(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support 

class PropertyForm(FlaskForm):
    title = TextAreaField('Property Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    no_bedroom = TextAreaField('No. of Bedrooms', validators=[DataRequired()])
    no_bathroom = TextAreaField('No. of Bathrooms', validators=[DataRequired()])
    location = TextAreaField('Location', validators=[DataRequired()])
    price = TextAreaField('Price', validators=[DataRequired()])
    type = SelectField('Type', choices=[('House', 'House'), ('Apartment', 'Apartment')])
    photo = FileField('Photo', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png', 'jpeg'], 'Images only!')])