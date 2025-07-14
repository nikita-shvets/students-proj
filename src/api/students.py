from Demos.win32ts_logoff_disconnected import session
from sqlalchemy import select,update,delete

from src.api.dependencies import SessionDep
from src.models.students import students
from src.schema.students import studentsaddSchema, studentsSchema
from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.post(
    "/add_students",
    tags=["Ученики"],
    summary="добавить учеников в базу"
)
async def add_students(data: studentsaddSchema, session:SessionDep):
    new_student = students(tg_id=data.tg_id, tg_name=data.tg_name)
    session.add(new_student)
    await session.commit()
@router.get('/get_students',
            tags=["Ученики"],
            summary="получить список учеников из базы"
            )
async def get_students(session:SessionDep)->list[studentsSchema]:
    query = select(students)
    result = await session.execute(query)
    return result.scalars().all()
@router.get('/get_students/{student_id}',
            tags=["Ученики"],
            summary="получить список учеников из базы"
            )
async def get_students_id(session:SessionDep, student_id : int)->list[studentsaddSchema]:
    query = select(students).where(students.id==student_id)
    result = await session.execute(query)
    return result.scalars().all()
@router.put('/put_students/{student_id}',
            tags=["Ученики"],
            summary="заменить ученика в базе"
            )
async def put_students(student_id:int,data: studentsaddSchema, session:SessionDep):

    item = await session.get(students, student_id)

    if not item :
        raise HTTPException(status_code=404, detail="Student not found")

    item.tg_name = data.tg_name
    item.tg_id = data.tg_id

    session.add(item)
    await session.commit()
    await session.refresh(item)

    return item
@router.patch('/patch_students/{student_id}',
            tags=["Ученики"],
            summary="заменить данные ученика в базе"
            )
async def patch_students(student_id:int,data: studentsaddSchema, session:SessionDep):
    item = await session.get(students, student_id)
    if not item :
        raise HTTPException(status_code=404, detail="Student not found")
    for field, value in data.dict(exclude_unset=True).items():
        setattr(item, field, value)
    session.add(item)
    await session.commit()
    await session.refresh(item)

    return item
@router.delete('/delete_students/{student_id}',
               tags=["Ученики"],
               summary="удалить ученика из базы"
               )
async def delete_students(student_id:int,session:SessionDep):
    item = await session.get(students, student_id)
    if not item:
        raise HTTPException(status_code=404, detail="Student not found")
    await session.delete(item)
    await session.commit()
    return "ok"