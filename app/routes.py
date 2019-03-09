from flask import render_template, url_for, redirect, flash
from app import app
import models
from flask_wtf import FlaskForm
from flask_login import current_user, login_user, login_required
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from flask_login import logout_user

from forms import LoginForm , StudentRegForm



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/students')
@login_required
def students():
    student_data = models.get_student_details()
    header_text = "Student Details"
    return render_template('students.html',header_text = header_text, student_data = student_data, loggedin =True)

@app.route('/teachers')
@login_required
def teachers():
    teacher_data = models.get_teacher_details()
    header_text = "Teacher Details"
    return render_template('teachers.html',header_text = header_text, teacher_data = teacher_data, loggedin =True)

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
        return redirect(url_for('login'))
    return render_template('add_student.html', title='Add Student', form=form, loggedin =False)



@app.route('/add_teacher', methods=['GET', 'POST'])
def add_teacher():
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
        return redirect(url_for('login'))
    return render_template('add_teacher.html', title='Add Student', form=form, loggedin =False)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('students'))

    form = LoginForm()
    next_page = url_for('login')
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = models.User()
        user.username = username
        user.id = 123456
        if username == "teacher" and password == "1234":
            next_page = url_for('teachers')
            login_user(user, remember=form.remember_me.data)

        elif models.check_user_cred(username, password ):
            next_page = url_for('students')
            login_user(user, remember=form.remember_me.data)
        else:
            flash('Invalid username or password')
            return redirect(url_for('login'))
        # user = User.query.filter_by(username=form.username.data).first()
        # if user is None or not user.check_password(form.password.data):
        #     flash('Invalid username or password')
        #     return redirect(url_for('login'))
        # login_user(user, remember=form.remember_me.data)
        # next_page = request.args.get('next')
        # if not next_page or url_parse(next_page).netloc != '':
        #     next_page = url_for('index')
        # return redirect(next_page)
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form, loggedin =False)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))
