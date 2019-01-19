from flask import render_template
from app import app
import models
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired



@app.route('/')
def welcome_home():
    return "Home Page"

@app.route('/students')
def students():
    student_data = models.get_student_details()
    header_text = "Student Details"
    return render_template('students.html',header_text = header_text, student_data = student_data)

@app.route('/teachers')
def teachers():
    teacher_data = models.get_teacher_details()
    header_text = "Teacher Details"
    return render_template('teachers.html',header_text = header_text, teacher_data = teacher_data)

@app.route('/add_student', methods=['GET', 'POST'])
def add_student():
    form = StudentRegForm()
    if form.validate_on_submit():
        print form.student_name.data, form.student_age.data
        student_data = models.add_student_details(
            form.student_name.data, 
            form.student_age.data, 
            form.student_gender.data,
            form.student_contact_no.data,
            form.student_course.data,
            form.student_address.data,
            form.student_qualification_10.data,
            form.student_qualification_12.data
            )
        header_text = "Student Details"
        student_data = models.get_student_details()
        return render_template('students.html',header_text = header_text, student_data = student_data)
    return render_template('add_student.html', title='Add Student', form=form)

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




