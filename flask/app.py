from flask import Flask, jsonify
import requests

url = 'http://localhost:5000/courses'


app = Flask(__name__)

courses = [{'id': 1, 'title': 'Python', 'description': 'Python is a programming language', 'done': False, 'price': 100},
           {'id': 2, 'title': 'Java', 'description': 'Java is a programming language',
               'done': False, 'price': 100},
           {'id': 3, 'title': 'C++', 'description': 'C++ is a programming language',
               'done': False, 'price': 100}
           ]


@app.route('/')
def index():
    return jsonify({'courses': ['Python', 'Java', 'C++']})


@app.route('/<int:id>', methods=['GET'])
def get_course(id):
    return jsonify({'course': courses[id]})


@app.route('/courses', methods=['GET'])
def get_courses():
    return jsonify({'courses': courses})


@app.route('/courses', methods=['POST'])
def add_course():
    course = {'id': 4, 'title': 'C#',
              'description': 'C# is a programming language', 'done': False, 'price': 100}
    courses.append(course)
    return jsonify({'created': course})


if __name__ == '__main__':
    app.run(debug=True)
