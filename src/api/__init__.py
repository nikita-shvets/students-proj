from fastapi import APIRouter

from src.api.teachers import router as teachers_router
from src.api.database import router as database_router
from src.api.students import router as students_router
from src.api.tasks import router as tasks_router
from src.api.groups import router as groups_router

main_router = APIRouter()

main_router.include_router(students_router)
main_router.include_router(database_router)
main_router.include_router(tasks_router)
main_router.include_router(teachers_router)
main_router.include_router(groups_router)