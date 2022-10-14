import pymysql
import os
from flask import Flask, request, render_template, g, redirect, Response, session
class CourseResource:
    @classmethod
    def __init__(self):
        pass

    @staticmethod
    def _get_connection():
        #user = "admin"
        #password = "han990219"
        #h = 'e5156-database-1.coxz1yzswsen.us-east-1.rds.amazonaws.com'
        user = "root"
        password = "han990219"
        h = "localhost"
        conn = pymysql.connect(
            user = user,
            password = password,
            host = h,
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True
        )
        return conn

    @staticmethod
    def get_all_courses():
        sql = "SELECT * FROM courseswork_6156.courses";
        conn = CourseResource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql)
        records = cur.fetchall()
        #result = cur.fetchone()
        return records

    @staticmethod
    def get_course_id(course_id):
        sql = "SELECT * FROM courseswork_6156.Courses where Course_id=%s";
        conn = CourseResource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, args = course_id)
        records = cur.fetchall()
        #result = cur.fetchone()
        return records

    @staticmethod
    def add_course(course_name, department, introduction = "NA"):
        if not (course_name and department):
            return False
        conn = CourseResource._get_connection()
        cur = conn.cursor()
        #####judge if the course exists#####
        sql1 = """
        SELECT * From courseswork_6156.Courses 
        WHERE course_name = %s and department = %s
        """
        cur.execute(sql1, args=(course_name, department))
        records = cur.fetchall()
        print(records)
        if len(records) >= 1:
            return False
        #####################################
        sql2 = """
         insert into courseswork_6156.Courses (Course_Name, Department, CourseIntroduction)
         values (%s, %s, %s);
        """
        cur.execute(sql2, args = (course_name, department, introduction))
        result = cur.rowcount
        return True if result == 1 else False

    @staticmethod
    def add_student_preference(uni, course_id, timezone = "NA", dept = "NA", message = "NA"):
        if not (uni and course_id) or not (timezone != "NA" or dept != "NA" or message != "NA"):
            return False
        conn = CourseResource._get_connection()
        cur = conn.cursor()
        #####judge if the preference exists#####
        sql1 = """
        SELECT * From courseswork_6156.student_preferences 
        WHERE uni = %s and Course_id = %s
        """
        cur.execute(sql1, args=(uni, int(course_id)))
        records = cur.fetchall()
        if len(records) >= 1:
            return False
        ########################################
        sql2 = """
             insert into courseswork_6156.student_preferences 
             (uni, Course_id, prefered_Dept, prefered_Timezone, prefered_message)
             values (%s, %s, %s, %s, %s);
            """
        cur.execute(sql2, args=(uni, int(course_id), dept, timezone, message))
        result = cur.rowcount
        return True if result == 1 else False

    @staticmethod
    def edit_student_preference(uni, course_id, timezone = "NA", dept = "NA", message = "NA"):
        if not (course_id and uni) or not (timezone != "NA" or dept != "NA" or message != "NA"):
            return False
        sql1 = """
        SELECT * FROM courseswork_6156.student_preferences where Course_id = %s and uni = %s
        """
        conn = CourseResource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql1, args=(course_id, uni))
        records = cur.fetchall()
        if len(records) < 1:
            return False
        sql2 = """
        UPDATE courseswork_6156.student_preferences 
        set prefered_Dept = %s, prefered_Timezone = %s, prefered_message = %s
        where uni = %s and Course_id = %s
        """;
        cur.execute(sql2, args=(dept, timezone, message, uni, int(course_id)))
        return True


    @staticmethod
    def get_course_preference_by_id_and_uni(course_id, uni):
        sql = "SELECT * FROM courseswork_6156.student_preferences where Course_id = %s and uni = %s";
        conn = CourseResource._get_connection()
        cur = conn.cursor()
        key = (course_id, uni)
        res = cur.execute(sql, args=key)
        records = cur.fetchall()
        # result = cur.fetchone()
        return records

    @staticmethod
    def get_course_preference_by_uni(uni):
        sql = "SELECT * FROM courseswork_6156.student_preferences where uni = %s";
        conn = CourseResource._get_connection()
        cur = conn.cursor()
        key = uni
        res = cur.execute(sql, args=key)
        records = cur.fetchall()
        # result = cur.fetchone()
        return records


    @staticmethod
    def delete_course_preference_by_id_and_uni(uni, course_id):
        if not (course_id and uni):
            return False
        sql1 = """
        SELECT * FROM courseswork_6156.student_preferences where Course_id = %s and uni = %s
        """
        conn = CourseResource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql1, args=(course_id, uni))
        records = cur.fetchall()
        if len(records) < 1:
            return False
        sql2 = "DELETE FROM courseswork_6156.student_preferences where Course_id = %s and uni = %s";
        cur.execute(sql2, args=(course_id, uni))
        return True
