# models.py
from sqlalchemy import Column, Integer, String
from .base import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    full_name = Column(String)
    hashed_password = Column(String)
    phone_number = Column(String)
    role = Column(String, server_default="user", nullable=False)
