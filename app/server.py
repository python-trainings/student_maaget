from flask import Flask
from flask import jsonify
from flask import render_template


app = Flask(__name__)

student_data = {
    "students" : [
    {"fname" : "pradip",
     "lname" : "das",
     "email" : "pradip@gmail.com"},
    {"fname" : "pragyan",
     "lname" : "barik",
     "email" : "pragyan@gmail.com"},
     {"fname" : "sharat",
     "lname" : "b",
     "email" : "pragyan@gmail.com"},
     {"fname" : "sharat",
     "lname" : "b",
     "email" : "pragyan@gmail.com"}
    ]
}

def get_details_from_db():
    
    return student_data

@app.route('/students')
def welcome():
    return jsonify(student_data)

@app.route('/welcome/home')
def welcome_home():
    return "Home Page"

@app.route('/')
def index():
    student_data = get_details_from_db()
    header_text = "Student Details"
    return render_template('students.html',header_text = header_text, student_data = student_data)

app.run(debug = True)