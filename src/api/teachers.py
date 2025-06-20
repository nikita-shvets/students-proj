
from sqlalchemy import select

from src.api.dependencies import SessionDep
from src.models.teachers import teachers
from src.schema.teachers import teachersaddSchema
from fastapi import APIRouter

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
async def get_teachers(session:SessionDep)->list[teachersaddSchema]:
    query= select(teachers)
    result = await session.execute(query)
    return result.scalars().all()