import asyncio
import httpx


async def add_major(major_name: str, major_description: str):
    url = 'http://127.0.0.1:8000/majors/add/'
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json'
    }
    data = {
        "major_name": major_name,
        "major_description": major_description,
        "count_students": 0
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(url, headers=headers, json=data)
        return response.json()


# вызов функции
response = asyncio.run(add_major(major_name='Философия', major_description='Тут мы обучаем философов'))
print(response)
response = asyncio.run(add_major(major_name='Математика', major_description='Царица всех наук'))
print(response)
response = asyncio.run(add_major(major_name='Литература', major_description='Тут мы обучаем чтению и анализу книг'))
print(response)
