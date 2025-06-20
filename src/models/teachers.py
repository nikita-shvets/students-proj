from fastapi import FastAPI,Depends
from sqlalchemy.ext.asyncio import create_async_engine ,async_sessionmaker ,async_session
from sqlalchemy import Column, Integer, Text, String, Boolean, DateTime, ForeignKey ,select
from sqlalchemy.orm import DeclarativeBase ,Mapped, mapped_column

from src.database import Base


class teachers(Base):
    __tablename__ = "teachers.db"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    subject = Column(String, nullable=False)