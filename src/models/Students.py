from fastapi import FastAPI,Depends
from sqlalchemy.ext.asyncio import create_async_engine ,async_sessionmaker ,async_session
from sqlalchemy import Column, Integer, Text, String, Boolean, DateTime, ForeignKey ,select
from sqlalchemy.orm import DeclarativeBase ,Mapped, mapped_column

from src.database import Base


class Student(Base):
    __tablename__ = "students.db"

    id = Column(Integer, primary_key=True)
    tg_id = Column(Integer, nullable=False)
    tg_name = Column(String, nullable=False)