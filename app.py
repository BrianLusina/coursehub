from course.app import create_course_app

course_app = create_course_app()

if __name__ == "__main__":
    course_app.run(debug=True, host='0.0.0.0', port=5001)
