from course.app import create_course_app
from course.di import configure
from flask_injector import FlaskInjector

course_app = create_course_app()

if __name__ == "__main__":
    FlaskInjector(app=course_app, modules=[configure])
    course_app.run(debug=True, host='0.0.0.0', port=5001)
