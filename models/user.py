from sqlalchemy import Column, Integer, String
from config.db import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    # email = Column(String(50), nullable=False, unique=True)
    # password = Column(String(50), nullable=False)