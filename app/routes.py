from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    text = "This is a flask app"
    return text
    # user = {'username': 'Admin'}
    # students = [
    #     {
    #         'name': 'Pragyan',
    #         'details': '70%'
    #     },
    #     {
    #         'name': 'Sarath',
    #         'details': '75%'
    #     },
    #     {
    #         'name': 'Subham',
    #         'details': '65%'
    #     },
    #     {
    #         'name': 'Sayan',
    #         'details': '70%'
    #     }
    # ]
    # return render_template('index.html', title='Home', user=user, students=students)
