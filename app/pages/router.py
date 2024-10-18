from fastapi import APIRouter, Request, Depends, UploadFile
from fastapi.templating import Jinja2Templates
import shutil

from app.students.router import get_all_students, get_student_by_id

router = APIRouter(prefix='/pages', tags=['Фронтенд'])
templates = Jinja2Templates(directory='templates')  # если запускать из консоли то нудно менять путь


@router.get('/students')
async def get_students_html(request: Request, students=Depends(get_all_students)):
    return templates.TemplateResponse(name='students.html', context={'request': request, 'students': students})


@router.post('/add_photo')
async def add_student_photo(file: UploadFile, image_name: int):
    with open(f"static/images/{image_name}.webp", "wb+") as photo_obj:
        shutil.copyfileobj(file.file, photo_obj)

@router.get('/students/{id}')
async def get_students_html(request: Request, student=Depends(get_student_by_id)):
    return templates.TemplateResponse(name='student.html',
                                      context={'request': request, 'student': student})
