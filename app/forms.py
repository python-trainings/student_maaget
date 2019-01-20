from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
# from app.models import User


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class StudentRegForm(FlaskForm):
    student_name = StringField('Student Name', validators=[DataRequired()])
    student_age = StringField('Age', validators=[DataRequired()])
    student_gender = StringField('Gender', validators=[DataRequired()])
    student_contact_no = StringField('Mobile', validators=[DataRequired()])
    student_course = StringField('Course', validators=[DataRequired()])
    student_address = StringField('Address', validators=[DataRequired()])
    student_qualification_10 = StringField('10th Marks', validators=[DataRequired()])
    student_qualification_12 = StringField('12th Marks', validators=[DataRequired()])
    submit = SubmitField('Add')    

class A():
    pass

# class RegistrationForm(FlaskForm):
#     username = StringField('Username', validators=[DataRequired()])
#     email = StringField('Email', validators=[DataRequired(), Email()])
#     password = PasswordField('Password', validators=[DataRequired()])
#     password2 = PasswordField(
#         'Repeat Password', validators=[DataRequired(), EqualTo('password')])
#     submit = SubmitField('Register')

#     def validate_username(self, username):
#         user = User.query.filter_by(username=username.data).first()
#         if user is not None:
#             raise ValidationError('Please use a different username.')

#     def validate_email(self, email):
#         user = User.query.filter_by(email=email.data).first()
#         if user is not None:
#             raise ValidationError('Please use a different email address.')