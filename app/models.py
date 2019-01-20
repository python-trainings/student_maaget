from lib import db
from flask_login import UserMixin
from app import login

def get_student_details():
    d = db.DB()
    data = d.fetch("SELECT * from student;")
    student_data = {"students" : []}
    for student in data:
        info = {}
        info["id"] = student[0]
        info["name"] = student[1]
        info["age"] = student[2]
        info["gender"] = student[3]
        info["mobile"] = student[4]
        info["course"] = student[5]
        info["address"] = student[6]
        info["10th"] = student[7]
        info["12th"] = student[8]
        student_data["students"].append(info)
    print student_data
    print "In get_student_details..........."
    d.close()
    return student_data

def add_student_details(name,age, gender, contact_no, course, address, qualification_10, qualification_12):
    print "Adding students................."
    print "insert into student(name,age, gender, contact_no, course, address, qualification_10, qualification_12) values ('%s', %s, '%s', '%s', '%s', '%s', %s, %s);" % (name,age, gender, contact_no, course, address, qualification_10, qualification_12)
    d = db.DB()
    data = d.insert("insert into student(name,age, gender, contact_no, course, address, qualification_10, qualification_12) values ('%s', %s, '%s', '%s', '%s', '%s', %s, %s);" % (name,age, gender, contact_no, course, address, qualification_10, qualification_12))
    d.close()

def get_teacher_details():
    d = db.DB()
    data = d.fetch("SELECT * from teacher;")
    teacher_data = {"teachers" : []}
    for teacher in data:
        info = {}
        info["id"] = teacher[0]
        info["name"] = teacher[1]
        info["age"] = teacher[2]
        info["gender"] = teacher[3]
        info["mobile"] = teacher[4]
        info["course"] = teacher[5]
        teacher_data["teachers"].append(info)
    print teacher_data
    print "In get_teacher_details..........."
    d.close()
    return teacher_data
    
class User(UserMixin):
    id = 1234
    username = ""
    # email = db.Column(db.String(120), index=True, unique=True)
    # password_hash = db.Column(db.String(128))
    # posts = db.relationship('Post', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


@login.user_loader
def load_user(id):
    user = User()
    user.id = id
    return user