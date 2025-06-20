from fastapi import FastAPI,Depends
from sqlalchemy.ext.asyncio import create_async_engine ,async_sessionmaker ,async_session
from sqlalchemy import Column, Integer, Text, String, Boolean, DateTime, ForeignKey ,select
from sqlalchemy.orm import DeclarativeBase ,Mapped, mapped_column
from src.database import Base


class groups(Base):
    __tablename__ = "groups.db"

    id = Column(Integer, primary_key=True)
    teachers_id = Column(Integer, nullable=False)
    students_ids = Column(String,nullable=False)