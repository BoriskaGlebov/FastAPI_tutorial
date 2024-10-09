import pytest
import requests

from tests.conftest import api_client


def test_get_all_students(api_client):
    url = "http://127.0.0.1:8000/students"
    response = api_client.get(url)
    assert len(response.json()) == 10


@pytest.mark.parametrize("course, result", [(2, 2), (1, 2), (3, 3), (4, 3), ], ids=['two', 'one', 'three', 'four'])
def test_get_students_with_param_requests(api_client, course, result):
    url = "http://127.0.0.1:8000/students"

    response = api_client.get(url, params={"course": course})
    assert len(response.json()) == result


@pytest.mark.parametrize("course, major, enrollment_year, result",
                         [(2, None, 2018, 1), (2, 'Экология', 2020, 0), ],
                         ids=['NONE', 'ЭКололгия'])
def test_get_students_with_param_mix(api_client, course, major, enrollment_year, result):
    url = f"http://127.0.0.1:8000/students/{course}"
    response = api_client.get(url, params={"major": major, "enrollment_year": enrollment_year})
    assert len(response.json()) == result


@pytest.mark.parametrize("id", [el for el in range(1, 11)], ids=[str(num) for num in range(1, 11)])
def test_students_id_param(api_client, id):
    url = f"http://127.0.0.1:8000/info"
    responses = api_client.get(url, params={'id': id})
    assert responses.json()['student_id'] == id


@pytest.mark.parametrize("id", [el for el in range(1, 11)], ids=[str(num) for num in range(1, 11)])
def test_students_id_param(api_client, id):
    url = f"http://127.0.0.1:8000/info/{id}"
    responses = api_client.get(url)
    assert responses.json()['student_id'] == id
