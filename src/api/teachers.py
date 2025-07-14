
from sqlalchemy import select

from src.api.dependencies import SessionDep
from src.models.teachers import teachers
from src.schema.teachers import teachersaddSchema, teacherSchema
from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.post(
    "/add_teachers",
    tags=["Учителя"],
    summary="добавить учителей в базу"
)
async def add_teachers(data: teachersaddSchema, session:SessionDep):
    new_teachers = teachers(name=data.name, subject=data.subject)
    session.add(new_teachers)
    await session.commit()
    return "ok"
@router.get('/get_teachers',
            tags=["Учителя"],
            summary="получить список учителей из базы"
            )
async def get_teachers(session:SessionDep)->list[teacherSchema]:
    query= select(teachers)
    result = await session.execute(query)
    return result.scalars().all()
@router.get('/get_teachers/{teacher_id}',
            tags=["Учителя"],
            summary="получить список учителей из базы"
            )
async def get_teachers_id(session:SessionDep, teacher_id : int)->list[teachersaddSchema]:
    query = select(teachers).where(teachers.id==teacher_id)
    result = await session.execute(query)
    return result.scalars().all()
@router.put('/put_teachers/{teachers_id}',
            tags=["Учителя"],
            summary="заменить учителя в базе"
            )
async def put_teachers(teachers_id:int,data: teachersaddSchema, session:SessionDep):

    item = await session.get(teachers, teachers_id)

    if not item :
        raise HTTPException(status_code=404, detail="teacher not found")

    item.name = data.name
    item.subject = data.subject

    session.add(item)
    await session.commit()
    await session.refresh(item)

    return item
@router.patch('/patch_teachers/{teacher_id}',
            tags=["Учителя"],
            summary="заменить данные учителя в базе"
            )
async def patch_teachers(teacher_id:int,data: teachersaddSchema, session:SessionDep):
    item = await session.get(teachers, teacher_id)
    if not item :
        raise HTTPException(status_code=404, detail="teacher not found")
    for field, value in data.dict(exclude_unset=True).items():
        setattr(item, field, value)
    session.add(item)
    await session.commit()
    await session.refresh(item)

    return item
@router.delete('/delete_teachers/{teacher_id}',
               tags=["Учителя"],
               summary="удалить учителя из базы"
               )
async def delete_teachers(teacher_id:int,session:SessionDep):
    item = await session.get(teachers, teacher_id)
    if not item:
        raise HTTPException(status_code=404, detail="teacher not found")
    await session.delete(item)
    await session.commit()
    return "ok"