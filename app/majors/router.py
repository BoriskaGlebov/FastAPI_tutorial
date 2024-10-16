from fastapi import APIRouter
from fastapi.params import Depends

from app.majors.dao import MajorsDAO
from app.majors.schemas import SMajorsAdd, SMajorsUpdDesc, SMajors

router = APIRouter(prefix='/majors', tags=['Работа с факультетами'])

@router.get("/")
async def get_all_majors()->list[SMajors]:
    return await MajorsDAO.find_all()

@router.post("/add/")
async def register_user(major: SMajorsAdd) -> dict:
    check = await MajorsDAO.add(**major.model_dump())
    print(check)
    if check:
        return {"message": "Факультет успешно добавлен!", "major": major}
    else:
        return {"message": "Ошибка при добавлении факультета!"}

@router.put("/update_description/")
async def update_major_description(major: SMajorsUpdDesc) -> dict:
    check = await MajorsDAO.update(filter_by={'major_name': major.major_name},
                                   major_description=major.major_description)
    if check:
        return {"message": "Описание факультета успешно обновлено!", "major": major}
    else:
        return {"message": "Ошибка при обновлении описания факультета!"}

@router.delete("/delete/{major_id}")
async def delete_major(major_id: int) -> dict:
    check = await MajorsDAO.delete(id=major_id)
    if check:
        return {"message": f"Факультет с ID {major_id} удален!"}
    else:
        return {"message": "Ошибка при удалении факультета!"}