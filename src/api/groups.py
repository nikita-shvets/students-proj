
from sqlalchemy import select

from src.api.dependencies import SessionDep
from src.models.groups import groups
from src.schema.groups import groupsaddSchema, groupsSchema
from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.post(
    "/add_groups",
    tags=["Группы"],
    summary="добавить группы в базу"
)
async def add_groups(data: groupsaddSchema, session:SessionDep):
    new_groups = groups(teachers_id=data.teachers_id, students_names=data.students_names)
    session.add(new_groups)
    await session.commit()
    return "ok"
@router.get('/get_groups',
            tags=["Группы"],
            summary="получить список груп из базы"
            )
async def get_groups(session:SessionDep)->list[groupsSchema]:
    query= select(groups)
    result = await session.execute(query)
    return result.scalars().all()
@router.get('/get_groups/{group_id}',
            tags=["Группы"],
            summary="получить список групп из базы"
            )
async def get_groups_id(session:SessionDep, group_id : int)->list[groupsaddSchema]:
    query = select(groups).where(groups.id==group_id)
    result = await session.execute(query)
    return result.scalars().all()
@router.put('/put_groups/{group_id}',
            tags=["Группы"],
            summary="заменить группу в базе"
            )
async def put_groups(group_id:int,data: groupsaddSchema, session:SessionDep):

    item = await session.get(groups, group_id)

    if not item :
        raise HTTPException(status_code=404, detail="Student not found")

    item.teacher_id = data.teachers_id
    item.student_names = data.student_names

    session.add(item)
    await session.commit()
    await session.refresh(item)

    return item
@router.patch('/patch_groups/{group_id}',
            tags=["Группы"],
            summary="заменить данные группы в базе"
            )
async def patch_groups(group_id:int,data: groupsaddSchema, session:SessionDep):
    item = await session.get(groups, group_id)
    if not item :
        raise HTTPException(status_code=404, detail="Student not found")
    for field, value in data.dict(exclude_unset=True).items():
        setattr(item, field, value)
    session.add(item)
    await session.commit()
    await session.refresh(item)

    return item
@router.delete('/delete_groups/{group_id}',
               tags=["Группы"],
               summary="удалить группу из базы"
               )
async def delete_groups(group_id:int,session:SessionDep):
    item = await session.get(groups, group_id)
    if not item:
        raise HTTPException(status_code=404, detail="Student not found")
    await session.delete(item)
    await session.commit()
    return "ok"
