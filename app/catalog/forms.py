from flask import request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, IntegerField
from wtforms.validators import ValidationError, DataRequired, Length


class EditCategoryForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    submit = SubmitField('Update')


class EditItemForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    category_id = IntegerField('Category id', validators=[DataRequired()])
    submit = SubmitField('Update')


class CreateCategoryForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    submit = SubmitField('Submit')


class CreateItemForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    description = StringField('Desription')
    category_id = StringField('category_id', validators=[DataRequired()])
    submit = SubmitField('Submit')
