from fastapi import FastAPI, HTTPException
from fastapi.params import Depends
from starlette.staticfiles import StaticFiles

from app.students.router import router as router_students
from app.majors.router import router as router_majors
from app.users.router import router as router_users
from app.pages.router import router as router_pages

from app.json_db import add_student, upd_student, dell_student
from app.students.pydantic_models import SStudent, Major, SUpdateFilter, SStudentUpdate, SDeleteFilter
from app.students.router import router
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


# class RBStudent:
#     def __init__(self, course: int, major: Optional[Major] = None, enrollment_year: Optional[int] = 2018):
#         self.course: int = course
#         self.major: Optional[Major] = major
#         self.enrollment_year: Optional[int] = enrollment_year


@app.get("/")
def home_page():

    return {"message": "Привет, Хабр!"}
app.mount('/static', StaticFiles(directory='static'), 'static')
app.include_router(router=router_users)
app.include_router(router=router_students)
app.include_router(router=router_majors)
app.include_router(router=router_pages)

# @app.get("/students")
# def get_all_students():
#     return json_to_dict_list(path_to_json)
#
#
# @app.get("/students")
# def get_all_students(course: Optional[int] = None):
#     students = json_to_dict_list(path_to_json)
#     if course is None:
#         return students
#     else:
#         return_list = []
#         for student in students:
#             if student["course"] == course:
#                 return_list.append(student)
#         return return_list
#
#
# #
#
# #
# # @app.get("/students/{course}")
# # def get_all_students_course(course: int):
# #     students = json_to_dict_list(path_to_json)
# #     return_list = []
# #     for student in students:
# #         if student["course"] == course:
# #             return_list.append(student)
# #     return return_list
#
#
# @app.get("/students/{course}", response_model=list[SStudent])
# def get_all_students_course(request_body: RBStudent = Depends()):
#     students = json_to_dict_list(path_to_json)
#     filtered_students = []
#     for student in students:
#         if student["course"] == request_body.course:
#             filtered_students.append(student)
#
#     if request_body.major:
#         filtered_students = [student for student in filtered_students if
#                              student['major'].lower() == request_body.major.lower()]
#
#     if request_body.enrollment_year:
#         filtered_students = [student for student in filtered_students if
#                              student['enrollment_year'] == request_body.enrollment_year]
#
#     return filtered_students
#
#
# @app.get("/info")
# def get_students_id_param(id: Optional[int] = None):
#     """Получения студента по его id (параметр запроса)"""
#     print(id)
#     print(type(id))
#     if id:
#         students = json_to_dict_list(path_to_json)
#         for student in students:
#             if student['student_id'] == id:
#                 return student
#     return 'Ничего не указывалось'
#
#
# @app.get("/info/{id}")
# def get_students_id(id: int):
#     """Получения студента по его id (параметр пути)"""
#     students = json_to_dict_list(path_to_json)
#     for student in students:
#         if student['student_id'] == id:
#             return student
#
#
# @app.get("/student", response_model=SStudent)
# def get_student_from_param_id(student_id: int):
#     students = json_to_dict_list(path_to_json)
#     for student in students:
#         if student["student_id"] == student_id:
#             return student
#
#
# @app.post("/add_student")
# def add_student_handler(student: SStudent):
#     student_dict = student.model_dump()
#     check = add_student(student_dict)
#     if check:
#         return {"message": "Студент успешно добавлен!"}
#     else:
#         return {"message": "Ошибка при добавлении студента"}
#
#
# @app.put("/update_student")
# def update_student_handler(filter_student: SUpdateFilter, new_data: SStudentUpdate):
#     check = upd_student(filter_student.model_dump(), new_data.model_dump())
#     if check:
#         return {"message": "Информация о студенте успешно обновлена!"}
#     else:
#         raise HTTPException(status_code=400, detail="Ошибка при обновлении информации о студенте")
#
#
# @app.delete("/delete_student")
# def delete_student_handler(filter_student: SDeleteFilter):
#     check = dell_student(filter_student.key, filter_student.value)
#     if check:
#         return {"message": "Студент успешно удален!"}
#     else:
#         raise HTTPException(status_code=400, detail="Ошибка при удалении студента")


if __name__ == '__main__':
    run(app="main:app", reload=True)
