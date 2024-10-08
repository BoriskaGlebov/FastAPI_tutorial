from fastapi import FastAPI

from utils import json_to_dict_list
import os
from typing import Optional
from uvicorn import run

# Получаем путь к директории текущего скрипта
script_dir = os.path.dirname(os.path.abspath(__file__))

# Переходим на уровень выше
parent_dir = os.path.dirname(script_dir)

# Получаем путь к JSON
path_to_json = os.path.join(parent_dir, 'students.json')

app = FastAPI()


@app.get("/")
def home_page():
    return {"message": "Привет, Хабр!"}


# @app.get("/students")
# def get_all_students():
#     return json_to_dict_list(path_to_json)
#
#
@app.get("/students")
def get_all_students(course: Optional[int] = None):
    students = json_to_dict_list(path_to_json)
    if course is None:
        return students
    else:
        return_list = []
        for student in students:
            if student["course"] == course:
                return_list.append(student)
        return return_list


#

#
# @app.get("/students/{course}")
# def get_all_students_course(course: int):
#     students = json_to_dict_list(path_to_json)
#     return_list = []
#     for student in students:
#         if student["course"] == course:
#             return_list.append(student)
#     return return_list


@app.get("/students/{course}")
def get_all_students_course(course: int, major: Optional[str] = None, enrollment_year: Optional[int] = 2018):
    students = json_to_dict_list(path_to_json)
    filtered_students = []
    for student in students:
        if student["course"] == course:
            filtered_students.append(student)

    if major:
        filtered_students = [student for student in filtered_students if student['major'].lower() == major.lower()]

    if enrollment_year:
        filtered_students = [student for student in filtered_students if student['enrollment_year'] == enrollment_year]

    return filtered_students


@app.get("/info")
def get_students_id_param(id: Optional[int]= None):
    """Получения студента по его id (параметр запроса)"""
    print(id)
    print(type(id))
    if id:
        students = json_to_dict_list(path_to_json)
        for student in students:
            if student['student_id'] == id:
                return student
    return 'Ничего не указывалось'

@app.get("/info/{id}")
def get_students_id(id: int):
    """Получения студента по его id (параметр пути)"""
    students = json_to_dict_list(path_to_json)
    for student in students:
        if student['student_id'] == id:
            return student





if __name__ == '__main__':
    run(app="main:app", reload=True)
