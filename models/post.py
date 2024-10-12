from sqlalchemy import Column, Integer, String
from config.db import Base

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    content = Column(String(255), nullable=False)
    user_id = Column(Integer, nullable=False)