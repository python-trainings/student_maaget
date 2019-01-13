from lib import db

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