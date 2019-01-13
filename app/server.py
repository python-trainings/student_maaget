from flask import Flask
from flask import jsonify
from flask import render_template


app = Flask(__name__)



# @app.route('/students')
# def welcome():
#     return jsonify(student_data)

@app.route('/')
def welcome_home():
    return "Home Page"

@app.route('/students')
def index():
    student_data = get_details_from_db()
    header_text = "Student Details"
    return render_template('students.html',header_text = header_text, student_data = student_data)

app.run(debug = True)