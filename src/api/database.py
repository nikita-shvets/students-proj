from fastapi import APIRouter


from src.database import Base,engine

router = APIRouter()
@router.post('/setup_database',
             tags=["база данных"],
             summary='удалить базу и создать заново'
             )
async def setup_database():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
        return "ok"