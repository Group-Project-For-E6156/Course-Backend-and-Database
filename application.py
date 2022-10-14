from flask import Flask, Response, request
from flask import Flask, request, render_template, g, redirect, Response, session
from datetime import datetime
import json
from courses_resource import CourseResource
from flask_cors import CORS


# Create the Flask application object.
app = Flask(__name__)

CORS(app)

@app.route("/course/", methods=["GET"])
def get_all_courses():
    result = CourseResource.get_all_courses()
    if result:
        rsp = Response(json.dumps(result), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")
    return rsp

@app.route("/course/<course_id>/", methods=["GET"])
def get_course_by_id(course_id):
    result = CourseResource.get_course_id(course_id)
    if result:
        rsp = Response(json.dumps(result), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")
    return rsp

@app.route("/course/add/course_name=<course_name>&department=<department>&introduction=<introduction>",
           methods=["POST", "GET"])
def insert_courses(course_name, department, introduction = 'NA'):
    print(course_name, department, introduction)
    result = CourseResource.add_course(course_name, department, introduction)
    if result:
        rsp = Response("COURSE CREATED", status=200, content_type="text/plain")
    else:
        rsp = Response("CREATION FAILED", status=404, content_type="text/plain")
    return rsp


@app.route("/course/student_preference/add/uni=<uni>&course_id=<course_id>&timezone=<timezone>&dept=<dept>&message=<message>",
           methods=["POST", "GET"])
def add_course_preference(uni, course_id, timezone = 'NA', dept = 'NA', message = 'NA'):
    result = CourseResource.add_student_preference(uni, course_id, timezone, dept, message)
    if result:
        rsp = Response("Course Preferences CREATED", status=200, content_type="text/plain")
    else:
        rsp = Response("CREATION FAILED", status=404, content_type="text/plain")
    return rsp

@app.route("/course/student_preference/edit/uni=<uni>&course_id=<course_id>&timezone=<timezone>&dept=<dept>&message=<message>",
           methods=["POST", "GET"])
def edit_course_preference(uni, course_id, timezone = 'NA', dept = 'NA', message = 'NA'):
    result = CourseResource.edit_student_preference(uni, course_id, timezone, dept, message)
    if result:
        rsp = Response("Course Preferences CREATED", status=200, content_type="text/plain")
    else:
        rsp = Response("CREATION FAILED", status=404, content_type="text/plain")
    return rsp


@app.route("/course/student_preference/<course_id>/<uni>", methods=["GET"])
def get_course_preference_by_id_and_uni(course_id, uni):
    result = CourseResource.get_course_preference_by_id_and_uni(course_id, uni)
    if result:
        rsp = Response(json.dumps(result), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")
    return rsp

@app.route("/course/student_preference/<uni>", methods=["GET"])
def get_course_preference_by_uni(uni):
    result = CourseResource.get_course_preference_by_uni(uni)
    if result:
        rsp = Response(json.dumps(result), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")
    return rsp

@app.route("/course/student_preference/delete/uni=<uni>&course_id=<course_id>",
           methods=["POST", "GET"])
def delete_course_preference_by_id_and_uni(uni, course_id):
    result = CourseResource.delete_course_preference_by_id_and_uni(uni, course_id)
    if result:
        rsp = Response("DELETE SUCCESS", status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")
    return rsp

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5011)