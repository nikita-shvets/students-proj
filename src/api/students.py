
from sqlalchemy import select,update,delete

from src.api.dependencies import SessionDep
from src.models.Students import Student
from src.schema.students import StudentsaddSchema, StudentsSchema
from fastapi import APIRouter

router = APIRouter()

@router.post(
    "/add_students",
    tags=["Ученики"],
    summary="добавить учеников в базу"
)
async def add_students(data: StudentsaddSchema, session:SessionDep):
    new_student = Student(tg_id=data.tg_id, tg_name=data.tg_name)
    session.add(new_student)
    await session.commit()
@router.get('/get_students',
            tags=["Ученики"],
            summary="получить список учеников из базы"
            )
async def get_students(session:SessionDep)->list[StudentsSchema]:
    query= select(Student)
    result = await session.execute(query)
    print(query)
    return result.scalars().all()
@router.put('/put_students/{student_id}',
            tags=["Ученики"],
            summary="заменить ученика в базе"
            )
async def put_students(student_id:int,data: StudentsaddSchema, session:SessionDep):
    query = update(Student).where(Student.id==student_id).values(tg_name=data.tg_name, tg_id=data.tg_id)
    res = await session.execute(query)
    await session.commit()
    return "ok"
@router.delete('/delete_students/{student_id}',
               tags=["Ученики"],
               summary="удалить ученика из базы"
               )
async def delete_students(student_id:int,session:SessionDep):
    query = delete(Student).where(Student.id==student_id)
    await session.execute(query)
    await session.commit()
    return "ok"