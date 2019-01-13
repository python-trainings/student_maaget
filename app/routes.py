from flask import render_template
from app import app
import models


@app.route('/')
def welcome_home():
    return "Home Page"

@app.route('/students')
def index():
    student_data = models.get_student_details()
    header_text = "Student Details"
    return render_template('students.html',header_text = header_text, student_data = student_data)


