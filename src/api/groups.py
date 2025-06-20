
from sqlalchemy import select

from src.api.dependencies import SessionDep
from src.models.groups import groups
from src.schema.groups import groupsaddSchema
from fastapi import APIRouter

router = APIRouter()

@router.post(
    "/add_groups",
    tags=["Группы"],
    summary="добавить группы в базу"
)
async def add_teachers(data: groupsaddSchema, session:SessionDep):
    new_groups = groups(teachers_id=data.teachers_id, students_ids=data.students_ids)
    session.add(new_groups)
    await session.commit()
    return "ok"
@router.get('/get_roups',
            tags=["Группы"],
            summary="получить список груп из базы"
            )
async def get_teachers(session:SessionDep)->list[groupsaddSchema]:
    query= select(groups)
    result = await session.execute(query)
    return result.scalars().all()