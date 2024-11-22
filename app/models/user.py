from fastapi_users.db import SQLAlchemyBaseUserTable
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String

Base = declarative_base()

class User(SQLAlchemyBaseUserTable, Base):
    role = Column(String, default="executor")  # Роль: admin, manager, executor
