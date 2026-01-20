from sqlalchemy import Column, Integer, String
from app.database.base import Base

class Login(Base):
    __tablename__ = "login"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=False, unique=True, index=True)
    password = Column(String, nullable=False)
    user_id = Column(Integer, nullable=False, index=True)
