import requests


def get_all_students():
    url = "http://127.0.0.1:8000/students"
    response = requests.get(url)
    return response.json()


students = get_all_students()
for i in students:
    print(i)
assert len(students) == 10

print('*' * 50)


def get_students_with_param_requests(course: int):
    url = "http://127.0.0.1:8000/students"
    response = requests.get(url, params={"course": course})
    return response.json()


students = get_students_with_param_requests(course=2)
for student in students:
    print(student)
assert len(students) == 2
print('*' * 50)


def get_students_with_param_mix(course: int, major: str|None, enrollment_year: int):
    url = f"http://127.0.0.1:8000/students/{course}"
    response = requests.get(url, params={"major": major, "enrollment_year": enrollment_year})
    return response.json()


students = get_students_with_param_mix(2, major=None, enrollment_year=2018)
print(students)
assert  len(students)==1