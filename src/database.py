from fastapi import FastAPI,Depends
from sqlalchemy.ext.asyncio import create_async_engine ,async_sessionmaker ,async_session
from sqlalchemy import Column, Integer, Text, String, Boolean, DateTime, ForeignKey ,select
from sqlalchemy.orm import DeclarativeBase ,Mapped, mapped_column



engine = create_async_engine('sqlite+aiosqlite:///students.db')

new_session = async_sessionmaker(engine,expire_on_commit=False)

async def get_session():
    async with new_session() as session:
        yield session

class Base(DeclarativeBase): pass