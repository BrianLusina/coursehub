from flask import Blueprint, jsonify
from flask_injector import inject
from .repository import CourseRepository

routes = Blueprint('routes', __name__)

@routes.route('/')
@inject
def courses(course_repository = CourseRepository):
    courses = course_repository.find_all()
    data = []
    for course in courses:
        data.append(course.toDict())
    return jsonify({"courses": data})
